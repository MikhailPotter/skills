# Topic and task handoff

Use the user's language for headings and content. A topic groups the work needed to reach one shared outcome. Put the brief's common constraints in the topic and add task-specific constraints in the relevant cards. Keep links to the brief and evidence accessible to the next executor. When the brief exists only in conversation, include the agreed details needed to execute the plan in a fresh chat.

## Topic template

```markdown
# <Topic title>

**Topic ID and revision:** <stable project-unique topic ID and current revision>
**Planning status:** Ready | Partially ready | Awaiting input
**Problem brief:** <Path or reference and revision when available>

## Outcome and scope
<Agreed goal and affected users or process. Include relevant boundaries and behavior to preserve.>

## Decisions and open questions
<Carry forward material decisions and assumptions. For each open item, say whether
it blocks planning, blocks a specific task, or can be investigated during work.>

## Topic acceptance
- **TC-1** — <Observable outcome and evidence needed to demonstrate it.>
<Include an end-to-end check when tasks interact.>

## Tasks
| ID and outcome | State | Required input | Topic criteria |
|---|---|---|---|
| T1 · <Outcome> | Ready or blocked | <Specific input and source, or none> | TC-1 |

## Starting point
<Which task can start. Include sequencing advice or write conflicts where useful.>
```

Use **Ready** when the task set is defined. Individual tasks may still wait for known prerequisites. Use **Partially ready** when some work is defined but a material decision or missing input prevents planning the rest. Use **Awaiting input** when the open issue prevents a usable plan. A topic can contain a single task.

## Task template

```markdown
### T1 · <Outcome-oriented task title>

**State:** Ready | Blocked
**Topic:** <Topic reference if the card is stored separately>
**Result:** <Behavior, evidence, or artifact the task must produce>
**Scope and inputs:** <Relevant constraints, entry points, and source references>
**Blocking prerequisites:** <Task or external input, required result, and what it enables>

**Acceptance**
- **T1.1** — <Given the relevant conditions, state what must be observed and how to check it.>

**Contributes to:** <Topic criteria IDs, or the task and criteria this prerequisite unlocks>
```

For an investigation, include the question, the effort bound, and which decision its findings enable. Accept the evidence and its limits even if the investigation ends without a conclusive cause. A dependent task stays blocked until the specific evidence or decision it requires is available.

### Example dependency

A writer sees *Saved* but loses the latest paragraph after refreshing the draft. If the cause is known and the fix is local, keep the change and its regression check in one task. If the cause determines which component needs to change, make T1 a bounded investigation. T2 can start once T1 supplies a repeatable case and evidence showing where the edited text is lost. If T1 reaches its effort limit without that evidence, record its findings and keep T2 blocked.

For topic acceptance, edit a paragraph, wait for *Saved*, refresh the same draft, and compare the restored paragraph with the edit.
