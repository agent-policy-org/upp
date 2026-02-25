from __future__ import annotations

from typing import Any

from integrations.python.generic_guard import guarded_agent_run


def run_langchain_guarded(
    *,
    policy_path: str,
    context: dict[str, Any],
    chain: Any,
    chain_input: dict[str, Any],
) -> dict[str, Any]:
    def _invoke() -> Any:
        return chain.invoke(chain_input)

    return guarded_agent_run(
        policy_path=policy_path,
        context=context,
        run_callable=_invoke,
    )
