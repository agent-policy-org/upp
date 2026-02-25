Universal Policy Protocol (UPP)
Elevator Pitch
Imagine AI agents—those autonomous powerhouses transforming everything from healthcare to finance—finally maturing into trustworthy partners. UPP is the open protocol that makes it happen: a universal standard for embedding ethical, legal, and behavioral policies directly into agents. With machine-readable schemas, dynamic opt-in updates from country regs (like NIST in the USA), and built-in ethics categories to combat bias and harm, UPP ensures agents comply without stifling innovation. Starting USA-focused and scaling globally, it's the governance layer AI agents need for 'better humanity.' Open-source and interoperable with MCP/UCP—build safer agents today.
Overview
UPP standardizes how AI agents (autonomous systems that perceive, decide, and act) adhere to ethical, legal, and behavioral policies. It elevates agentic AI maturity by enabling dynamic, enforceable guidelines, with opt-in updates from jurisdictional sources. This fosters "better humanity" by mitigating risks like bias, harm, and non-compliance, drawing from global ethics discussions (e.g., fairness, transparency, accountability).

Key Features:
Machine-readable JSON/YAML schemas with ethical focus areas.
Dynamic updates via subscriptions (e.g., from NIST feeds).
Enforcement middleware for runtime checks.
Compliance dates to reduce version drift.
Interoperable with MCP (policies as context) and UCP.


For the full specification, see docs/spec-v1.0.md.
Specification Summary (v1.0)
Policy Schema
Policies are JSON documents validated against this schema:
JSON{
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
Example Policy
See examples/us-privacy-v1.0.json:
JSON{
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
Usage

Validate a Policy: Use JSON schema validators (e.g., in Python: jsonschema library).
Integrate in Agents: Query UPP endpoints in your agent code (prototype coming soon).
Updates: Subscribe to feeds for dynamic compliance.

Roadmap

Q1 2026: Spec + Prototype (USA focus).
Q2 2026: Beta testing; global examples.
Q3 2026: Full release; community features.
Q4 2026: Integrations (MCP/UCP); v2.0.

Contributing
We welcome contributions! See CONTRIBUTING.md for guidelines. Propose new ethical categories or policies via issues/PRs.
License
Licensed under Apache 2.0. See LICENSE.
