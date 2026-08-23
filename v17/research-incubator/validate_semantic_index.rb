# frozen_string_literal: true

require "digest"
require "yaml"

INCUBATOR = File.expand_path(__dir__)
REPOSITORY = File.expand_path("../..", INCUBATOR)
INDEX_PATH = File.join(INCUBATOR, "SEMANTIC_INDEX.yaml")
REQUIRED = %w[
  path sha256 created_at front status supersedes superseded_by depends_on
  source_audit_status authority promotion_readiness maximum_claim canonical
].freeze

def resolve_path(path)
  if path.start_with?("v17/")
    File.join(REPOSITORY, path)
  else
    File.join(INCUBATOR, path)
  end
end

index = YAML.load_file(INDEX_PATH)
artifacts = index.fetch("artifacts")
errors = []

paths = artifacts.map { |artifact| artifact.fetch("path") }
counts = Hash.new(0)
paths.each { |path| counts[path] += 1 }
counts.each do |path, count|
  errors << "duplicate artifact path: #{path}" if count > 1
end

discovered_paths = Dir.glob(File.join(INCUBATOR, "{active,snapshots}", "**", "*.md"))
  .map { |path| path.delete_prefix("#{INCUBATOR}/") }
  .sort
(discovered_paths - paths).each do |path|
  errors << "unindexed Markdown artifact: #{path}"
end
(paths - discovered_paths).each do |path|
  next if path.start_with?("v17/")

  errors << "indexed path lies outside the governed artifact tree: #{path}"
end

artifact_by_path = {}
artifacts.each { |artifact| artifact_by_path[artifact.fetch("path")] = artifact }

artifacts.each do |artifact|
  path = artifact.fetch("path")
  missing_keys = REQUIRED.reject { |key| artifact.key?(key) }
  errors << "#{path}: missing keys #{missing_keys.join(', ')}" unless missing_keys.empty?

  errors << "#{path}: authority must be none" unless artifact["authority"] == "none"

  full_path = resolve_path(path)
  if !File.file?(full_path)
    errors << "#{path}: artifact file is missing"
  elsif artifact["sha256"] != Digest::SHA256.file(full_path).hexdigest
    errors << "#{path}: stale sha256"
  end

  %w[depends_on supersedes superseded_by].each do |field|
    Array(artifact[field]).each do |target|
      errors << "#{path}: self-edge in #{field}" if target == path
      next if File.exist?(resolve_path(target))

      errors << "#{path}: missing #{field} target #{target}"
    end
  end

  archival = artifact["status"].to_s.match?(/\A(?:superseded|historical|deferred|future-review)/)
  if archival && artifact["promotion_readiness"] == "user-decision-ready"
    errors << "#{path}: archival status contradicts user-decision-ready promotion"
  end
end

# Detect directed cycles among exact artifact-to-artifact dependencies. Directory
# dependencies and official v17 files remain existence-checked but are not
# collapsed into invented graph nodes.
colour = Hash.new(:white)
stack = []
visit = lambda do |path|
  colour[path] = :grey
  stack << path
  Array(artifact_by_path.fetch(path)["depends_on"]).each do |dependency|
    next unless artifact_by_path.key?(dependency)

    if colour[dependency] == :grey
      start = stack.index(dependency) || 0
      errors << "dependency cycle: #{(stack[start..-1] + [dependency]).join(' -> ')}"
    elsif colour[dependency] == :white
      visit.call(dependency)
    end
  end
  stack.pop
  colour[path] = :black
end
paths.each { |path| visit.call(path) if colour[path] == :white }

canonical_fronts = index.fetch("canonical_fronts")
canonical_fronts.each do |front, path|
  errors << "canonical front #{front}: missing target #{path}" unless File.exist?(resolve_path(path))
  if artifact_by_path.key?(path) && !artifact_by_path.fetch(path)["canonical"]
    errors << "canonical front #{front}: indexed target is not marked canonical"
  end
end

canonical_paths = artifacts.select { |artifact| artifact["canonical"] }.map { |artifact| artifact["path"] }
canonical_paths.each do |path|
  unless canonical_fronts.value?(path)
    errors << "#{path}: canonical true but absent from canonical_fronts"
  end
end

if errors.empty?
  puts "semantic index valid: #{artifacts.length} artifacts, complete coverage, and no stale hashes, missing targets, self-edges, cycles, canonical contradictions, or promotion contradictions"
  exit 0
end

warn "semantic index invalid (#{errors.length} defects):"
errors.uniq.each { |error| warn "- #{error}" }
exit 1
