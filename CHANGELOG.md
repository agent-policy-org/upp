# Changelog

All notable changes to this project are documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning principles for spec milestones.

## [Unreleased]

### Added

- Community contribution guide in `CONTRIBUTING.md`
- Initial specification draft in `docs/spec-v1.0.md`
- Canonical JSON Schema in `docs/schema-v1.0.json`
- USA, EU, and India example policies in `examples/`
- Policy validation script in `scripts/validate_policies.py`
- CI workflow for policy/schema validation in `.github/workflows/validate.yml`
- GitHub issue templates and pull request template in `.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md`
- Repository governance and health files (`CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, `GOVERNANCE.md`, `CHANGELOG.md`, `.github/CODEOWNERS`)
- Repository hygiene defaults in `.editorconfig` and `.gitignore`
- Protocol wire draft in `docs/protocol-wire-v1.0.md`
- Audit envelope schema in `docs/audit-envelope-v1.0.json`

### Changed

- Strengthened policy action contract in `docs/schema-v1.0.json` with well-known and extension action namespaces
- Aligned metadata requirements between schema/spec (`authority` and `applies_to` now required)
- Hardened runtime evaluator in `upp_runtime/engine.py` with expression limits, safe normalization for `&&`/`||`/`!`, and non-crashing condition error capture
