# Execution handoff

Write in the user's language. Keep the report usable in a new conversation with access to its referenced inputs and artifacts. Use the status matching the evidence.

```markdown
# Execution — <topic or task>

**Input:** <topic or task ID and brief or plan version>
**Status:** Verified | Partial | Blocked
**Result:** <artifact location and exact version or snapshot, plus baseline when applicable>

## Outcome and evidence
<What changed or was established. Map observations to task criteria and,
for a whole topic, to the combined acceptance criteria.>

| Axis or criterion | Status | Evidence and source |
|---|---|---|
| <axis or criterion> | Passed, failed, pending, or not applicable | <reviewer or tool, exact version, evidence or gap> |

## Checkpoint, when work remains
<Completed work, current artifact locations and versions, pending checks,
blocking input or decision, and the next safe step. Record any operation
with an uncertain outcome and what must be checked before repeating it.>
```

Use **Verified** only when all mandatory checks for the selected scope pass. Use **Partial** for work with useful results that still needs work or verification. Use **Blocked** when the selected work cannot continue until the named condition changes. Show the available result and checkpoint in either incomplete case. Keep passing author or tool evidence separate from pending independent review.
