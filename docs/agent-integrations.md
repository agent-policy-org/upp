# Agent Integrations (Python)

This guide shows how to enforce UPP policies before agent execution.

## Files

- Runtime engine: `upp_runtime/engine.py`
- Generic wrapper: `integrations/python/generic_guard.py`
- OpenAI wrapper: `integrations/python/openai_responses_guard.py`
- LangChain wrapper: `integrations/python/langchain_guard.py`

## 1) Generic Integration

```python
from integrations.python.generic_guard import guarded_agent_run

context = {
    "data_type": "pii",
    "consent": False,
    "bias_score": 0.12,
}

result = guarded_agent_run(
    policy_path="examples/us-privacy-basic-v1.0.json",
    context=context,
    run_callable=lambda: "agent output",
)

print(result["status"])
print(result["decision"].enforcement)
```

## 2) OpenAI Responses Integration

```python
from openai import OpenAI
from integrations.python.openai_responses_guard import run_openai_guarded

client = OpenAI()

context = {
    "data_type": "pii",
    "consent": True,
    "bias_score": 0.05,
}

result = run_openai_guarded(
    policy_path="examples/us-privacy-basic-v1.0.json",
    context=context,
    client=client,
    model="gpt-4.1-mini",
    prompt="Summarize this customer request",
)
```

## 3) LangChain Integration

```python
from integrations.python.langchain_guard import run_langchain_guarded

context = {
    "data_type": "non_pii",
    "consent": True,
    "bias_score": 0.18,
}

result = run_langchain_guarded(
    policy_path="examples/us-privacy-basic-v1.0.json",
    context=context,
    chain=chain,
    chain_input={"input": "Explain product options"},
)
```

## Enforcement Behavior

- `block`: call is prevented and status is `blocked`
- `warn`: call is allowed with warnings in decision metadata
- `log`: call is allowed and decision logs are included
- `allow`: no matching rules triggered
