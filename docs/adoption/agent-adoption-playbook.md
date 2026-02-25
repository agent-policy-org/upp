# Agent Adoption Playbook

## Objective

Drive practical UPP adoption by integrating policy enforcement before agent actions.

## Recommended Initial Agent Targets

1. OpenAI Responses-based agents
2. LangChain pipelines and tools
3. Custom Python orchestrators

## Integration Pattern

1. Load policy JSON
2. Build request context for current action
3. Evaluate policy decision (`block`, `warn`, `log`, `allow`)
4. Execute action only if not blocked
5. Persist decision metadata for audit

## Adoption Levels

### Level 1: Starter (1-2 teams)

- Integrate UPP guard in one production-adjacent flow
- Use at least one jurisdiction policy from `examples/`
- Track blocked vs warned decisions weekly

### Level 2: Standardized (3-5 teams)

- Shared policy pack and context schema across teams
- CI checks on policy files and schema compatibility
- Policy change review process through pull requests

### Level 3: Organizational (6+ teams)

- UPP guard integrated in all high-impact agent paths
- Centralized audit reporting and monthly compliance reviews
- Versioned rollout policy and deprecation windows

## Success Metrics

- Adoption: number of services/agents using UPP guard
- Coverage: percentage of high-risk actions evaluated
- Compliance: policy violation rate trend
- Operations: mean time to policy update rollout

## 90-Day Execution Plan

### Days 1-30

- Integrate `integrations/python/generic_guard.py` into one agent
- Use `examples/us-privacy-basic-v1.0.json`
- Log `PolicyDecision` outcomes

### Days 31-60

- Add `openai_responses_guard.py` or `langchain_guard.py`
- Introduce one additional jurisdiction policy
- Start weekly policy review

### Days 61-90

- Expand to at least three agent workflows
- Add release-gated policy updates
- Publish internal adoption dashboard
