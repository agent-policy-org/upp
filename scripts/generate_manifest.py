from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def _canonical_bytes(payload: dict) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _sha256_digest(payload: dict) -> str:
    digest = hashlib.sha256(_canonical_bytes(payload)).hexdigest()
    return f"sha256:{digest}"


def _build_policy_entry(*, payload: dict, file_name: str, policy_url_base: str) -> dict:
    return {
        "policy_id": payload["policy_id"],
        "jurisdiction": payload["jurisdiction"],
        "version": payload["version"],
        "digest": _sha256_digest(payload),
        "url": f"{policy_url_base.rstrip('/')}/{file_name}",
    }


def generate_manifest(*, repo_root: Path, repository_url: str, latest: str, policy_url_base: str) -> dict:
    examples_dir = repo_root / "examples"
    policy_files = sorted(examples_dir.glob("*.json"))

    policies: list[dict] = []
    for policy_path in policy_files:
        with policy_path.open("r", encoding="utf-8") as file:
            payload = json.load(file)
        policies.append(
            _build_policy_entry(
                payload=payload,
                file_name=policy_path.name,
                policy_url_base=policy_url_base,
            )
        )

    policies.sort(key=lambda item: (item["jurisdiction"], item["policy_id"], item["version"]))

    return {
        "repository": repository_url,
        "latest": latest,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "policies": policies,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate UPP policy manifest from examples/")
    parser.add_argument(
        "--repository-url",
        default="https://github.com/agent-policy-org/upp",
        help="Canonical repository URL",
    )
    parser.add_argument(
        "--latest",
        default="1.0",
        help="Latest protocol/schema version",
    )
    parser.add_argument(
        "--policy-url-base",
        default="https://raw.githubusercontent.com/agent-policy-org/upp/main/examples",
        help="Base URL where policy JSON files are hosted",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    manifest = generate_manifest(
        repo_root=repo_root,
        repository_url=args.repository_url,
        latest=args.latest,
        policy_url_base=args.policy_url_base,
    )

    output_path = repo_root / ".well-known" / "upp" / "manifest.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(manifest, file, indent=2)
        file.write("\n")

    print(f"Manifest written: {output_path}")
    print(f"Policies indexed: {len(manifest['policies'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
