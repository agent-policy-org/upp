from __future__ import annotations

import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    schema_path = repo_root / "docs" / "schema-v1.0.json"
    examples_dir = repo_root / "examples"

    if not schema_path.exists():
        print(f"Missing schema file: {schema_path}")
        return 1

    if not examples_dir.exists():
        print(f"Missing examples directory: {examples_dir}")
        return 1

    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)

    example_files = sorted(examples_dir.glob("*.json"))
    if not example_files:
        print("No policy examples found in examples/")
        return 1

    has_errors = False
    for example_path in example_files:
        payload = load_json(example_path)
        errors = sorted(validator.iter_errors(payload), key=lambda item: item.path)
        if errors:
            has_errors = True
            print(f"[FAIL] {example_path.relative_to(repo_root)}")
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  - {location}: {error.message}")
        else:
            print(f"[OK]   {example_path.relative_to(repo_root)}")

    return 1 if has_errors else 0


if __name__ == "__main__":
    sys.exit(main())
