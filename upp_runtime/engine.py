from __future__ import annotations

import ast
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class PolicyDecision:
    blocked: bool
    enforcement: str
    actions: list[str]
    warnings: list[str]
    logs: list[str]
    matched_rules: list[dict[str, Any]]


def load_policy(path: str | Path) -> dict[str, Any]:
    policy_path = Path(path)
    with policy_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_policy(policy: dict[str, Any], context: dict[str, Any]) -> PolicyDecision:
    rules = policy.get("rules", [])

    blocked = False
    actions: list[str] = []
    warnings: list[str] = []
    logs: list[str] = []
    matched_rules: list[dict[str, Any]] = []

    for rule in rules:
        condition = str(rule.get("condition", "")).strip()
        if not condition:
            continue

        if _evaluate_condition(condition, context):
            matched_rules.append(rule)
            action = str(rule.get("action", "")).strip()
            if action:
                actions.append(action)

            enforcement = str(rule.get("enforcement", "log")).lower().strip()
            message = str(rule.get("explanation", "")).strip() or action

            if enforcement == "block":
                blocked = True
                warnings.append(message)
            elif enforcement == "warn":
                warnings.append(message)
            else:
                logs.append(message)

    final_enforcement = "allow"
    if blocked:
        final_enforcement = "block"
    elif warnings:
        final_enforcement = "warn"
    elif logs:
        final_enforcement = "log"

    return PolicyDecision(
        blocked=blocked,
        enforcement=final_enforcement,
        actions=actions,
        warnings=warnings,
        logs=logs,
        matched_rules=matched_rules,
    )


def _evaluate_condition(condition: str, context: dict[str, Any]) -> bool:
    expression = ast.parse(condition, mode="eval")
    result = _safe_eval(expression.body, context)
    return bool(result)


def _safe_eval(node: ast.AST, context: dict[str, Any]) -> Any:
    if isinstance(node, ast.BoolOp):
        values = [_safe_eval(value, context) for value in node.values]
        if isinstance(node.op, ast.And):
            return all(values)
        if isinstance(node.op, ast.Or):
            return any(values)
        raise ValueError("Unsupported boolean operator")

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return not bool(_safe_eval(node.operand, context))

    if isinstance(node, ast.Compare):
        left_value = _safe_eval(node.left, context)
        for operator_node, comparator_node in zip(node.ops, node.comparators):
            right_value = _safe_eval(comparator_node, context)
            if isinstance(operator_node, ast.Eq):
                valid = left_value == right_value
            elif isinstance(operator_node, ast.NotEq):
                valid = left_value != right_value
            elif isinstance(operator_node, ast.Gt):
                valid = left_value > right_value
            elif isinstance(operator_node, ast.GtE):
                valid = left_value >= right_value
            elif isinstance(operator_node, ast.Lt):
                valid = left_value < right_value
            elif isinstance(operator_node, ast.LtE):
                valid = left_value <= right_value
            elif isinstance(operator_node, ast.In):
                valid = left_value in right_value
            elif isinstance(operator_node, ast.NotIn):
                valid = left_value not in right_value
            else:
                raise ValueError("Unsupported comparison operator")

            if not valid:
                return False
            left_value = right_value
        return True

    if isinstance(node, ast.Name):
        lowered = node.id.lower()
        if lowered == "true":
            return True
        if lowered == "false":
            return False
        if lowered == "null":
            return None
        return context.get(node.id)

    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.List):
        return [_safe_eval(item, context) for item in node.elts]

    if isinstance(node, ast.Tuple):
        return tuple(_safe_eval(item, context) for item in node.elts)

    raise ValueError(f"Unsupported expression type: {type(node).__name__}")
