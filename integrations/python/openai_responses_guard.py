from __future__ import annotations

from typing import Any

from integrations.python.generic_guard import guarded_agent_run


def run_openai_guarded(
    *,
    policy_path: str,
    context: dict[str, Any],
    client: Any,
    model: str,
    prompt: str,
) -> dict[str, Any]:
    def _invoke() -> Any:
        return client.responses.create(
            model=model,
            input=prompt,
        )

    return guarded_agent_run(
        policy_path=policy_path,
        context=context,
        run_callable=_invoke,
    )
