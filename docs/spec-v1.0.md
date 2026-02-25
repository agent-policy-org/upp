# UPP Specification v1.0

## 1. Purpose

Universal Policy Protocol (UPP) defines a machine-readable format for ethical, legal, and behavioral policy enforcement in AI agents.

## 2. Scope

This version focuses on:

- Policy document structure
- Runtime rule evaluation semantics
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

## 4. Rule Model

Each rule supports:

- `condition` (string): Evaluatable expression against runtime context
- `action` (string): Action key for middleware/executor
- `enforcement` (enum): `block`, `warn`, or `log`
- `explanation` (string, optional): Human-readable reason
- `risk_level` (enum, optional): `low`, `medium`, `high`

### 4.1 Evaluation Order

- Rules are evaluated in listed order
- Multiple matching rules may fire
- Enforcement precedence should be treated as: `block` > `warn` > `log`

## 5. Enforcement Semantics

- `block`: Prevent action execution
- `warn`: Allow action with explicit warning/audit marker
- `log`: Allow action and persist decision trace

## 6. Metadata Requirements

`metadata` should include:

- `update_source`: URL/feed origin for policy updates
- `authority`: Issuing authority (e.g., NIST)
- `applies_to`: Domains such as `data_processing`, `decision_making`
- `compliance_date`: ISO-8601 date (`YYYY-MM-DD`)

## 7. Validation

UPP policies should be validated against a JSON Schema (Draft 2020-12 recommended) before runtime loading.

## 8. Reference Example

See [examples/us-privacy-basic-v1.0.json](../examples/us-privacy-basic-v1.0.json).

## 9. Compatibility Notes

UPP is designed to be protocol-agnostic and interoperable with MCP/UCP integration layers.
