# Problem handoff formats

Write headings and content in the user's language. Keep each section only as long as the next reader needs. Use stable source references when available. State whether an example comes from a check, a user report, or a proposed success scenario.

## Problem brief

```markdown
# Problem brief — <short problem title>

**Status:** Ready for planning | Awaiting a decision

## Problem and impact
<Who or what is affected, in which situation, and what goes wrong or falls short.>

## Observations and sources
<Observed behavior and evidence. Label reports from the user and unverified hypotheses separately. Include a reproduction example when available.>

## Desired outcome
<What the affected person or process should be able to do or observe.>

## Scope and constraints
<What is included, what is outside the request, and any behavior or constraints to preserve.>

## Signs of success
<Observable checks or representative scenarios for the overall outcome. Include a boundary case if it distinguishes material interpretations.>

## Decisions and assumptions
<Material decisions with their source. Mark working assumptions separately and explain their impact where relevant.>

## Open questions
<Separate a decision needed before planning from research that can be planned. For a blocker, state the question, who can resolve it, and what the answer unlocks.>
```

The brief gives Plan the desired overall outcome and its boundaries. Plan can derive task-level acceptance criteria from it. Include a technical cause or approach only when supported and relevant, and identify whether it is a confirmed fact, a decision or a hypothesis.

## Investigation findings

```markdown
# Findings — <area investigated>

## Scope and coverage
<What was examined and under which conditions.>

## Confirmed findings
<For each finding, describe the symptom, affected scenario, evidence and observed impact. State explicitly if the investigation confirmed none.>

## Open observations and limits
<What could not be confirmed, what was outside coverage, and which evidence would help.>
```
