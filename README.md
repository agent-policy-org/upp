# Universal Policy Protocol (UPP)

## Elevator Pitch

Imagine AI agents — those autonomous powerhouses transforming everything from healthcare to finance — finally maturing into trustworthy partners.  
**UPP** is the open protocol that makes it happen: a universal standard for embedding ethical, legal, and behavioral policies directly into agents.

With machine-readable schemas, dynamic opt-in updates from country regulations (like NIST in the USA), and built-in ethics categories to combat bias and harm, UPP ensures agents comply without stifling innovation.  
Starting USA-focused and scaling globally, it is the governance layer AI agents need for **better humanity**.

Open-source • Interoperable with MCP & UCP • Build safer agents today.

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
} ```

