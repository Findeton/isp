#!/usr/bin/env python3
"""Convert the v6/publishable papers (GitHub markdown) to LaTeX for tectonic.

Usage: md2tex.py input.md output.tex
Scope: exactly the feature set these nine papers use -- ATX headers, bold,
italic, inline code, fenced code blocks, $/$$ math, -/1. lists, > quotes.
Math and code segments are protected before any text escaping.
"""

import re
import sys

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage{fontspec}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage[margin=1.1in]{geometry}
\usepackage{microtype}
\usepackage{parskip}
\usepackage{lmodern}
\usepackage[colorlinks=true,linkcolor=blue!50!black,urlcolor=blue!50!black]{hyperref}
\providecommand{\tightlist}{}
"""


def esc(text):
    """Escape LaTeX specials in plain text (no math/code inside)."""
    text = text.replace("\\", r"\textbackslash{}")
    for ch, rep in [("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_"),
                    ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")]:
        text = text.replace(ch, rep)
    return text


def fmt_inline(text, stash):
    """Protect inline math/code, escape the rest, apply bold/italic."""
    tokens = []

    def stash_token(s):
        tokens.append(s)
        return f"\x00{len(tokens)-1}\x00"

    # inline code first (may contain $ or *)
    text = re.sub(r"`([^`]+)`",
                  lambda m: stash_token(r"\texttt{" + esc(m.group(1)) + "}"),
                  text)
    # inline math (non-greedy, no blank line)
    text = re.sub(r"\$([^$]+)\$",
                  lambda m: stash_token("$" + m.group(1) + "$"),
                  text)
    text = esc(text)
    text = re.sub(r"\*\*([^*]+(?:\*[^*]+)*)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*([^*]+)\*", r"\\emph{\1}", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: tokens[int(m.group(1))], text)
    return text


def convert(md):
    lines = md.split("\n")
    out = []
    title = author = date = None
    i = 0
    list_stack = []  # 'itemize' / 'enumerate'

    def close_lists():
        while list_stack:
            out.append(r"\end{" + list_stack.pop() + "}")

    para = []

    def flush_para():
        if para:
            out.append(fmt_inline(" ".join(para), None))
            out.append("")
            para.clear()

    while i < len(lines):
        ln = lines[i]

        # fenced code block
        if ln.startswith("```"):
            flush_para()
            close_lists()
            out.append(r"\begin{small}\begin{verbatim}")
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                out.append(lines[i])
                i += 1
            out.append(r"\end{verbatim}\end{small}")
            i += 1
            continue

        # display math
        if ln.strip() == "$$":
            flush_para()
            close_lists()
            out.append(r"\[")
            i += 1
            while i < len(lines) and lines[i].strip() != "$$":
                out.append(lines[i])
                i += 1
            out.append(r"\]")
            i += 1
            continue

        # headers
        m = re.match(r"^(#{1,3}) (.*)$", ln)
        if m:
            flush_para()
            close_lists()
            level, text = len(m.group(1)), m.group(2)
            if level == 1 and title is None:
                title = fmt_inline(text, None)
            elif level == 2:
                out.append(r"\section*{" + fmt_inline(text, None) + "}")
            else:
                out.append(r"\subsection*{" + fmt_inline(text, None) + "}")
            i += 1
            continue

        # author/status front matter
        m = re.match(r"^\*\*Author:\*\* (.*)$", ln)
        if m and author is None:
            author = fmt_inline(m.group(1), None)
            i += 1
            continue
        m = re.match(r"^\*\*Status:\*\* (.*)$", ln)
        if m and date is None:
            buf = [m.group(1)]
            while i + 1 < len(lines) and lines[i + 1].strip() and \
                    not lines[i + 1].startswith(("#", "**", "-", ">")):
                i += 1
                buf.append(lines[i].strip())
            date = fmt_inline(" ".join(buf), None)
            i += 1
            continue

        # blockquote
        if ln.startswith(">"):
            flush_para()
            close_lists()
            out.append(r"\begin{quote}")
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ").rstrip())
                i += 1
            out.append(fmt_inline(" ".join(buf), None))
            out.append(r"\end{quote}")
            continue

        # lists
        m = re.match(r"^(\s*)- (.*)$", ln)
        if m:
            if not list_stack or list_stack[-1] != "itemize":
                flush_para()
                close_lists()
                out.append(r"\begin{itemize}")
                list_stack.append("itemize")
            item = [m.group(2)]
            while i + 1 < len(lines) and re.match(r"^\s{2,}\S", lines[i + 1]) \
                    and not re.match(r"^\s*- ", lines[i + 1]):
                i += 1
                item.append(lines[i].strip())
            out.append(r"\item " + fmt_inline(" ".join(item), None))
            i += 1
            continue
        m = re.match(r"^(\s*)\d+\. (.*)$", ln)
        if m:
            if not list_stack or list_stack[-1] != "enumerate":
                flush_para()
                close_lists()
                out.append(r"\begin{enumerate}")
                list_stack.append("enumerate")
            item = [m.group(2)]
            while i + 1 < len(lines) and re.match(r"^\s{2,}\S", lines[i + 1]) \
                    and not re.match(r"^\s*\d+\. ", lines[i + 1]):
                i += 1
                item.append(lines[i].strip())
            out.append(r"\item " + fmt_inline(" ".join(item), None))
            i += 1
            continue

        if not ln.strip():
            close_lists()
            flush_para()
            i += 1
            continue

        para.append(ln.strip())
        i += 1

    close_lists()
    flush_para()
    body = "\n".join(out)
    tex = PREAMBLE
    tex += "\\title{" + (title or "Untitled") + "}\n"
    tex += "\\author{" + (author or "") + "}\n"
    tex += "\\date{\\small " + (date or "") + "}\n"
    tex += "\\begin{document}\n\\maketitle\n\n" + body + "\n\\end{document}\n"
    return tex


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src) as f:
        md = f.read()
    with open(dst, "w") as f:
        f.write(convert(md))
    print(f"wrote {dst}")
