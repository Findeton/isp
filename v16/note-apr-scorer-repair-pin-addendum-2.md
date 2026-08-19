# APR Paper 12 — bounded scorer repair: reconstructible mutation evidence

**Date:** 2026-08-19  
**Status:** BINDING PRE-FREEZE SCHEMA ADDENDUM  
**Parents:** `v16/note-apr-scorer-repair-pin.md`,
`v16/note-apr-scorer-repair-pin-addendum.md`

An independent verifier must be able to reconstruct each changed object from
the receipt without reading scorer internals. Prose plus pre/post hashes is
insufficient. Therefore every transformation row other than `UNAVAILABLE`
must include a machine-readable mutation descriptor with:

1. `target_root` and `target_object`;
2. a typed object path or constructor schema locating the mutation;
3. exact old and new semantic values, or complete canonical pre/post payloads;
4. every reference update needed to keep or deliberately sever reachability;
5. canonical pre/post payload SHA-256 values;
6. the generic measurement function/type rerun and its before/after result;
7. any shared-evidence link, so one changed object is not counted twice.

For ancestry-only M35, the scientific object is intentionally byte-identical.
Its row must therefore include distinct pre/post provenance-envelope payloads
and hashes, the deleted or redirected typed edge, root/path reachability before
and after, and the invariant scientific payload hash. A literal provenance
Boolean or an opaque internal mutation name is not evidence.

`ANALYTICAL-CONTROL`, `SCOPE-CONTROL`, and `REFUSED` rows obey the same schema
where an input object exists. `UNAVAILABLE` rows instead print the exact absent
baseline type/interface and the capability-census witness establishing that
absence. No row may rely on fixture identifiers or prose to tell a verifier
how its changed object was made.

