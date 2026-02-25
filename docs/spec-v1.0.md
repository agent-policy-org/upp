# UPP Specification v1.0

## 1. Purpose

Universal Policy Protocol (UPP) defines a machine-readable format for ethical, legal, and behavioral policy enforcement in AI agents.

## 2. Scope

This version focuses on:

- Policy document structure
- Runtime rule evaluation semantics
- Policy distribution and update model
- Authenticity and trust metadata
- Audit decision envelope
- Enforcement levels
- Metadata for jurisdictional updates and compliance timing

## 3. Policy Document Structure

A policy document is a JSON object with the following required top-level fields:

- `policy_id` (string): Unique identifier for the policy
- `jurisdiction` (string): Region/country scope (e.g., `USA`, `EU`, `global`)
- `version` (string): Semantic-like version (e.g., `1.0`, `1.0.1`)
- `ethical_focus` (string): Primary ethics dimension
- `rules` (array): One or more executable policy rules
- `metadata` (object): Update authority/source and compliance metadata

Optional but recommended:

- `ethical_categories` (array): Additional ethics dimensions

## 4. Action Contract

`action` is a protocol-level contract value.

### 4.1 Well-known actions

- `block_request`
- `require_user_consent`
- `require_human_review`
- `redact_pii`
- `explain_decision`

### 4.2 Extensions

Custom actions MUST use one of:

- `x_*` namespace (for local/vendor extensions)
- `urn:upp:action:*` namespace (for portable extension identifiers)

## 5. Rule Model

Each rule supports:

- `condition` (string): Evaluatable expression against runtime context
- `action` (string): Action key for middleware/executor
- `enforcement` (enum): `block`, `warn`, or `log`
- `explanation` (string, optional): Human-readable reason
- `risk_level` (enum, optional): `low`, `medium`, `high`

### 5.1 Evaluation Order

- Rules are evaluated in listed order
- Multiple matching rules may fire
- Enforcement precedence is: `block` > `warn` > `log`
- If one or more `block` rules match, final decision MUST be `block`
- Matching rules accumulate actions, warnings, and logs

## 6. Enforcement Semantics

- `block`: Prevent action execution
- `warn`: Allow action with explicit warning/audit marker
- `log`: Allow action and persist decision trace

## 7. Metadata Requirements

`metadata` MUST include:

- `update_source`: URL/feed origin for policy updates
- `authority`: Issuing authority (e.g., NIST)
- `applies_to`: Domains such as `data_processing`, `decision_making`
- `compliance_date`: ISO-8601 date (`YYYY-MM-DD`)

`metadata` MAY include:

- `compatible_with`: minimum supported UPP version range
- `supersedes`: list of policy ids/versions replaced
- `deprecation_date`: date after which a policy should no longer be used
- `signature`: detached signature descriptor (`alg`, `key_id`, `sig`, `issued_at`)

## 8. Distribution and Wire Model

UPP policy distribution is HTTP-first. A deployment SHOULD expose:

- Manifest endpoint: `/.well-known/upp/manifest.json`
- Policy artifact endpoint: `/v1/policies/{jurisdiction}/{policy_id}/{version}.json`
- Update feed endpoint: `/v1/feeds/{jurisdiction}.ndjson`

Minimum manifest fields:

- `repository`: source URL
- `latest`: latest stable schema/protocol version
- `policies`: list of policy descriptors with digest + location

## 9. Authenticity and Trust Model

Policy artifacts SHOULD be signed and verifiable.

- Acceptable signature mechanisms: Sigstore/cosign-style attestations or JWS detached signatures
- `key_id` MUST map to a published trust root or key registry entry
- Clients SHOULD support key rotation and trust pinning
- Clients MUST verify signature before policy activation when signature metadata is present

## 10. Update Semantics

- Subscriptions are opt-in by jurisdiction/feed
- Clients SHOULD support staged rollout windows
- Clients SHOULD keep last-known-good policy snapshots for rollback
- Incompatible updates MUST be rejected outside declared compatibility windows

## 11. Audit Envelope

Every enforcement decision SHOULD emit a standard decision log envelope with at least:

- `decision_id`
- `timestamp`
- `policy_ref` (`policy_id`, `version`, `jurisdiction`)
- `input_fingerprint` (hash of normalized non-PII decision context)
- `final_enforcement`
- `matched_rules`
- `actions`
- `warnings`
- `errors`

PII MUST NOT be logged in clear text; only redacted or hashed forms should be recorded.

## 12. Validation

UPP policies should be validated against a JSON Schema (Draft 2020-12 recommended) before runtime loading.

## 13. Reference Example

See [examples/us-privacy-basic-v1.0.json](../examples/us-privacy-basic-v1.0.json).

## 14. Compatibility Notes

UPP is designed to be protocol-agnostic and interoperable with MCP/UCP integration layers.
