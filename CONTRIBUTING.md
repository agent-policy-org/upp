# Contributing to UPP

Thanks for helping improve the Universal Policy Protocol (UPP).

## Ways to Contribute

- Propose new ethical categories
- Add or improve jurisdiction-specific policy examples
- Improve schema, validation, and enforcement documentation
- Submit bug reports and feature requests

## Before You Start

- Check existing issues to avoid duplicate work
- Keep changes focused and minimal per pull request
- For policy examples, prefer realistic and auditable rule explanations

## Development Scope (Current)

The project currently includes:

- Protocol documentation in `docs/`
- Example policy files in `examples/`
- Top-level documentation in `README.md`

## Reporting Issues

When opening an issue, include:

- Problem summary
- Expected behavior
- Current behavior
- Reproduction steps (if applicable)
- Suggested fix or direction (optional)

## Proposing a New Policy Example

Please include:

- `policy_id` and target `jurisdiction`
- Policy intent and ethical focus
- Rule rationale (`explanation`) for each rule
- Compliance assumptions (authority, source feed, compliance date)

Add new examples under `examples/` with clear, versioned filenames, for example:

- `examples/us-privacy-basic-v1.0.json`
- `examples/eu-transparency-basic-v1.0.json`

## Pull Request Guidelines

- Use a descriptive PR title
- Explain what changed and why
- Reference related issues
- Update docs when behavior or structure changes
- Keep formatting and style consistent with existing files

## Validation Expectations

Before submitting a PR:

- Validate JSON examples with a JSON Schema validator
- Ensure links in `README.md` remain valid
- Confirm new docs are clear and concise

## Code of Conduct

Be respectful, collaborative, and constructive in all discussions.

## License

By contributing, you agree that your contributions are licensed under Apache License 2.0.
