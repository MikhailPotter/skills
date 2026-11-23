---
name: plan
description: Turn a bug report or problem brief into an implementation plan with task dependencies and testable acceptance criteria. Identify which tasks can start and what would unblock the rest.
---

# Plan

Use the brief the user names, whether it is in this conversation, pasted from elsewhere, or stored in a file. Produce a topic and its tasks in the user's language. Stop at the planning handoff. Implementation starts with a separate user request.

## Establish the planning input

1. Read the brief and relevant project material. Carry forward the desired outcome, signs of success, constraints, and decisions. Cite the source and its version when available. Make the handoff usable in a fresh conversation by including essential details and durable references.
2. If the input is a findings report, plan the finding or set of findings the user selected. When selection is delegated, state what you selected and why. If unrelated findings compete for scope and the user has not selected or delegated the choice, ask which outcome to plan.
3. Check whether an open question prevents you from defining a result or acceptance criterion. Resolve facts from available sources first. Bring material choices about intent or scope to the user. Draft any independent work and name the blocked part. When a technical unknown can be explored within the agreed goal, carry it into the plan.

## Choose task boundaries

Start with one coherent task. A separate task needs a verifiable result and a useful boundary, such as earlier feedback, separate ownership, safer sequencing, or a result that unlocks another task.

| Choice | When to use it |
|---|---|
| **Keep one task** | The work produces one result best checked as a whole. Include routine investigation, implementation, and checks as steps as needed. |
| **Split by scenario** | The work has slices that can each demonstrate an observable outcome. Look for meaningful workflow paths, business rules, user groups, or data variants. Include the layers and checks needed to prove each slice. |
| **Extract a technical prerequisite** | A prerequisite can be verified on its own and separate ownership, sequencing, or safe rollout is useful. Name the specific work it enables. |
| **Bound an investigation** | An unresolved technical question can change feasibility, design, or the scope of later tasks. Specify the question, time or effort budget, evidence to collect, and decision it will inform. Accept a supported answer or a documented blocker when the budget ends. |

Keep work together when splitting would leave incomplete pieces that require the same acceptance check. Use expected change size and review effort as signals to reconsider a boundary. A task may span several layers or pull requests.

## Connect tasks and checks

- Identify each task by a stable ID within the topic. Give it an observable output, scope, and acceptance criteria. Describe the conditions and expected evidence for each meaningful criterion.
- Use a blocking dependency when one task needs a specific accepted result from another. Name that result. Record priority and overlapping write areas separately. Parallel work needs available inputs and a safe way to combine changes.
- If a later task has a clear result but lacks a prerequisite, mark it blocked. If its scope or criteria depend on a future decision, record the follow-up condition in the topic until the task can be defined.
- Keep topic criteria separate from task acceptance. Map the work to the brief's signs of success and include a way to check combined behavior where tasks interact.

## Deliver the topic and stop

Use the [topic and task template](references/topic-and-tasks.md). Before delivery, check that every agreed sign of success has coverage or an explicit blocker, every task has a checkable result, every dependency names a required result or external input, and the dependency graph has no cycles. State what can start and what would unblock the rest. If no usable work can be defined yet, return the blocking decision or missing input and the conditions for resuming.

Return the Markdown in the conversation. If the user requests files or the project defines a writable place for plan artifacts, save the topic and its tasks according to that convention. A single document works for a small topic. Use an existing project identifier and revision when available. For a chat-only plan, a unique topic slug and a revision such as r1 suffice. Keep topic and task IDs stable across edits and advance the revision when the plan changes. When revising from Review, read the cited brief and prior topic, address the selected findings, and identify affected criteria and dependencies. Report the handoff path when a file is saved. A later explicit `Execute` invocation can take the topic or one task.
