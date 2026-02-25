from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

from upp_runtime import evaluate_policy, load_policy


def guarded_agent_run(
    *,
    policy_path: str | Path,
    context: dict[str, Any],
    run_callable: Callable[[], Any],
) -> dict[str, Any]:
    policy = load_policy(policy_path)
    decision = evaluate_policy(policy, context)

    if decision.blocked:
        return {
            "status": "blocked",
            "decision": decision,
            "result": None,
        }

    result = run_callable()
    return {
        "status": "allowed",
        "decision": decision,
        "result": result,
    }
