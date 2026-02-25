# Versioning and Release Policy

UPP follows Semantic Versioning for protocol and schema releases.

## Version Format

- `MAJOR.MINOR.PATCH` (for example, `1.0.0`)
- Git tags use a `v` prefix (for example, `v1.0.0`)

## Meaning

- MAJOR: Breaking changes to policy schema semantics or required fields
- MINOR: Backward-compatible additions (new optional fields, docs, examples)
- PATCH: Backward-compatible fixes and clarifications

## Release Cadence

- Releases are cut from `main` after validation checks pass
- Every release must include changelog updates
- Tags trigger automated GitHub Release publishing

## Pre-release Labels

Use pre-release tags when needed:

- `v1.1.0-rc.1`
- `v2.0.0-beta.1`

## Release Checklist

1. Update `CHANGELOG.md` under a new version section
2. Ensure policy examples validate against `docs/schema-v1.0.json`
3. Confirm docs links and governance docs are current
4. Create and push tag (for example, `git tag v1.0.0 && git push origin v1.0.0`)
5. Verify generated GitHub Release assets and checksums
