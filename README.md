# Universal Policy Protocol (UPP)

## Elevator Pitch

Imagine AI agents — those autonomous powerhouses transforming everything from healthcare to finance — finally maturing into trustworthy partners.  
**UPP** is the open protocol that makes it happen: a universal standard for embedding ethical, legal, and behavioral policies directly into agents.

With machine-readable schemas, dynamic opt-in updates from country regulations (like NIST in the USA), and built-in ethics categories to combat bias and harm, UPP ensures agents comply without stifling innovation.  
Starting USA-focused and scaling globally, it is the governance layer AI agents need for **better humanity**.

Open-source • Interoperable with MCP & UCP • Build safer agents today.

## Project Status

- Stage: Specification-first open-source protocol project
- Current focus: v1.0 schema hardening and multi-jurisdiction examples
- Quality gates: automated schema validation in CI for all policy examples

![Validate Policies](https://github.com/agent-policy-org/upp/actions/workflows/validate.yml/badge.svg)

Documentation source: [site/index.html](site/index.html)

Published docs site (after Pages deploy): https://agent-policy-org.github.io/upp/

## Overview

**UPP** (Universal Policy Protocol) standardizes how AI agents (autonomous systems that perceive, decide, and act) adhere to ethical, legal, and behavioral policies.  
It elevates agentic AI maturity by enabling dynamic, enforceable guidelines with opt-in updates from jurisdictional sources.

This fosters "better humanity" by mitigating risks like bias, harm, non-compliance, and ethical drift — drawing from global AI ethics discussions (fairness, transparency, accountability, privacy, etc.).

### Key Features

- Machine-readable JSON/YAML policy schemas with ethical focus categories
- Dynamic opt-in updates via secure subscriptions (e.g. NIST, EU AI Act feeds)
- Runtime enforcement middleware (block/warn/log)
- Compliance dates to prevent version drift
- Interoperable with Model Context Protocol (MCP) and commerce protocols (UCP)
- Built-in audit logging and human override support

Full specification → [docs/spec-v1.0.md](docs/spec-v1.0.md)

Canonical JSON Schema → [docs/schema-v1.0.json](docs/schema-v1.0.json)

## Specification Summary (v1.0)

### Policy Schema

Policies are validated JSON documents:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "policy_id": { "type": "string" },
    "jurisdiction": { "type": "string", "default": "global" },
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+(\\.[\\d]+)?$" },
    "ethical_focus": {
      "type": "string",
      "enum": ["bias_mitigation", "transparency", "accountability", "privacy_protection", "harm_prevention", "socioeconomic_impact", "sentience_consideration"]
    },
    "ethical_categories": {
      "type": "array",
      "items": { "type": "string", "enum": ["bias_mitigation", "transparency", "accountability", "privacy_protection", "harm_prevention", "socioeconomic_impact", "sentience_consideration"] }
    },
    "rules": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "condition": { "type": "string" },
          "action": { "type": "string" },
          "enforcement": { "type": "string", "enum": ["block", "warn", "log"] },
          "explanation": { "type": "string" },
          "risk_level": { "type": "string", "enum": ["low", "medium", "high"] }
        },
        "required": ["condition", "action", "enforcement"]
      },
      "minItems": 1
    },
    "metadata": {
      "type": "object",
      "properties": {
        "update_source": { "type": "string" },
        "authority": { "type": "string" },
        "applies_to": { "type": "array", "items": { "type": "string" } },
        "compliance_date": { "type": "string", "format": "date" }
      },
      "required": ["update_source", "compliance_date"]
    }
  },
  "required": ["policy_id", "jurisdiction", "version", "ethical_focus", "rules", "metadata"]
}
```

### Example Policy (USA Privacy)

```json
{
  "policy_id": "us-privacy-basic-v1.0",
  "jurisdiction": "USA",
  "version": "1.0",
  "ethical_focus": "privacy_protection",
  "ethical_categories": ["bias_mitigation", "transparency", "accountability"],
  "rules": [
    {
      "condition": "data_type == 'pii' && consent == false",
      "action": "anonymize_or_block",
      "enforcement": "block",
      "explanation": "Aligns with CCPA for consumer data rights, ensuring accountability in data handling",
      "risk_level": "high"
    },
    {
      "condition": "bias_score > 0.3",
      "action": "flag_for_review",
      "enforcement": "warn",
      "explanation": "Mitigates bias per NIST guidelines, promoting fairness",
      "risk_level": "medium"
    }
  ],
  "metadata": {
    "update_source": "https://api.nist.gov/ai/policies/feed",
    "authority": "NIST",
    "applies_to": ["data_processing", "decision_making"],
    "compliance_date": "2026-03-01"
  }
}
```

More examples in [examples/](examples/)

## Repository Structure

```
.
├── docs/
│   ├── spec-v1.0.md
│   └── schema-v1.0.json
├── examples/
│   ├── us-privacy-basic-v1.0.json
│   ├── eu-transparency-basic-v1.0.json
│   └── india-accountability-basic-v1.0.json
├── scripts/
│   └── validate_policies.py
└── .github/
    ├── workflows/validate.yml
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## Roadmap

| Quarter | Focus | Milestones |
| --- | --- | --- |
| Q1 2026 | Specification & Prototype | Final v1.0 spec, USA-focused prototype in Go, basic enforcement tests |
| Q2 2026 | Beta Testing & Global Expansion | Beta release, EU/India example policies, community feedback loop |
| Q3 2026 | Full Release & Community | v1.0 public release, GitHub Pages site, policy marketplace concept |
| Q4 2026 | Integrations & v2.0 | MCP/UCP compatibility, decentralized update feeds (exploration), v2.0 spec |
| 2027+ | Standardization & Adoption | OECD/IEEE submission, agent certification badges, enterprise partnerships |

## Usage

- Validate a policy: Use any JSON Schema validator (e.g. `jsonschema` in Python)
- Integrate in agents: Call UPP endpoints before actions (prototype SDK coming soon)
- Subscribe to updates: Register for country-specific feeds (opt-in only)

### Local Validation Quickstart

```bash
python3 -m pip install jsonschema
python3 scripts/validate_policies.py
```

The script validates every file in `examples/` against `docs/schema-v1.0.json`.

## Releases

- Tag format: `vMAJOR.MINOR.PATCH` (example: `v1.0.0`)
- Tags trigger automated GitHub Releases with packaged protocol artifacts
- Release workflow: `.github/workflows/release.yml`

See [VERSIONING.md](VERSIONING.md) for the complete policy and checklist.

## Contributing

We welcome contributions!

- Propose new ethical categories or jurisdiction policies via issues
- Submit pull requests for schema improvements, examples, or code
- See `CONTRIBUTING.md` for full guidelines

Related community and governance docs:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)
- [GOVERNANCE.md](GOVERNANCE.md)
- [SUPPORT.md](SUPPORT.md)
- [CHANGELOG.md](CHANGELOG.md)
- [VERSIONING.md](VERSIONING.md)

## License

Apache License 2.0  
See [LICENSE](LICENSE) file for details.

<img src="https://img.shields.io/github/stars/agent-policy-org/upp?style=social" alt="GitHub stars">
