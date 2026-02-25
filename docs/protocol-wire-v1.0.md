# UPP Wire Protocol Draft v1.0

This document defines a practical HTTP distribution profile for UPP policy artifacts.

Reference artifact in this repository: `.well-known/upp/manifest.json`.

## 1. Endpoints

### 1.1 Manifest

`GET /.well-known/upp/manifest.json`

Response includes:

- `repository`: canonical repository URL
- `latest`: latest protocol/schema version
- `generated_at`: timestamp
- `policies`: array of policy entries

Each policy entry includes:

- `policy_id`
- `jurisdiction`
- `version`
- `digest` (SHA-256)
- `url`

### 1.2 Policy Artifact

`GET /v1/policies/{jurisdiction}/{policy_id}/{version}.json`

Returns a policy document compliant with `docs/schema-v1.0.json`.

### 1.3 Update Feed

`GET /v1/feeds/{jurisdiction}.ndjson`

Each NDJSON row should include:

- `event_type` (`created`, `updated`, `deprecated`, `revoked`)
- `policy_ref`
- `timestamp`
- `url`
- `digest`

## 2. Caching and Rollback

- Serve `ETag` and `Cache-Control` headers on manifest/policy endpoints
- Clients should store last-known-good artifacts and associated digest
- On verification failure, clients must rollback to last-known-good policy

## 3. Authenticity

- Policy artifacts should include signature metadata (`metadata.signature`)
- Recommended trust strategies:
  - Sigstore/cosign style attestations
  - Detached JWS signatures
- Clients should pin trusted key IDs and support key rotation

## 4. Compatibility Windows

- `metadata.compatible_with` declares minimum compatible UPP runtime version
- `metadata.deprecation_date` declares planned retirement date
- Clients should reject incompatible policy updates by default

## 5. Error Handling

- `404`: policy/version not found
- `409`: requested version incompatible with current runtime profile
- `422`: malformed policy content
- `503`: temporary distribution outage (retry with exponential backoff)
