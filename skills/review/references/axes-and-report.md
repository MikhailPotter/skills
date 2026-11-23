# Review axes and report

## Plan axes

| Axis | Check | Evidence |
|---|---|---|
| **Brief coverage** | Compare topic and tasks with the agreed goal, scope and constraints. Look for omissions, incorrect interpretations, and work added beyond the agreed boundaries. | Brief or decision reference and affected task, or the missing coverage. |
| **Executability** | Check that task outputs, required inputs and dependencies let a fresh executor start eligible work. Look for unresolved prerequisites, cycles, and conflicting work presented as parallel. | Task references, the blocking input or dependency path, and the work it affects. |
| **Verifiability** | Check for observable acceptance criteria per task and a combined check for interacting tasks. | Criterion reference, the check an executor can run or observe, and any missing evidence. |
| **Solution quality** | Include when the plan commits to a consequential technical choice or feasibility assumption. Compare the choice with constraints and relevant alternatives. | Design reference, relevant constraints, and evidence such as a prototype or experiment when needed. |

In a re-review, reproducible evidence on the new target can establish that a specific finding is fixed. Label the evidence source. Record any outstanding independent assignment and use the shared axis verdict rules, including precedence for confirmed blockers. Mark the finding unverified when the available evidence does not establish the fix.

## Report format

Write in the user's language. Use a short summary and preserve the findings and coverage reported for each axis.

```markdown
# Review — <subject>

**Target:** <version or immutable snapshot and baseline when applicable>
**Sources:** <brief, plan, project rules and previous report as applicable>
**Scope:** <requested coverage and its boundaries>
**Conclusion:** Passed | Changes requested | Inconclusive

| Axis | Verdict | Evidence and coverage |
|---|---|---|
| <axis> | Passed, failed, pending, or not applicable | <reviewer or tool, reference and any gap> |

## Findings by axis
<Give each finding a stable ID. Cite the criterion, location or scenario, evidence and consequence. Identify blockers and optional improvements separately.>

## Re-review, when applicable
<For prior findings mark fixed, still open, or unverified. Name affected
regressions checked on the new version and any evidence carried forward.>

## Disposition
<What passed, which changes are requested, or the exact inputs still needed. For a handoff to Plan or Execute, identify the topic revision, affected tasks and finding IDs. Link the original inputs or include the relevant criteria, constraints and decisions when they exist only in chat.>
```
