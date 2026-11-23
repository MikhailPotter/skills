---
name: execute
description: Carry out a planned software task or a whole implementation plan, or resume from a checkpoint. Check the result against its acceptance criteria and report the evidence or the blocker.
---

# Execute

Read the user's selection and the corresponding Plan handoff. Work and report in the user's language. The coordinator owns scope, integration, communication with the user, and the final verification record.

## Establish the execution scope

1. For a topic, read its brief, decisions, acceptance criteria and task graph. Work on eligible tasks and verify the combined result against the topic criteria. For a single task, read its card and the applicable topic context. Use accepted prerequisite outputs and keep execution within the selected task. When addressing review findings, recover the selected card, criteria and reviewed version first. Confirm the current target before changing it. Report a missing prerequisite that falls outside the selection. A completed investigation unlocks dependent work only when it supplies the specific evidence or decision that work needs.
2. Confirm the current brief and task versions, actual artifacts, relevant project rules, and prerequisite evidence. Treat card status as a starting point for inspection. On resume, reconcile the checkpoint with current inputs, files, in-flight assignments, and actions with uncertain outcomes. Recheck affected evidence when inputs changed.
3. Read and apply [Independent review](../independent-review/SKILL.md) in preparation mode to select checks and evidence. Acceptance and behavior is mandatory for each task and for the integrated result of a whole topic. Include the other applicable axes and checks required by the plan or project. Update the selection if material risks change.

## Execute and coordinate

- Work inline for closely coupled steps. Use a worker subagent for a bounded investigation or eligible task when it can return a distinct result and delegation is available and permitted. Parallelize only with disjoint write scopes or isolated workspaces and an agreed integration owner. Reassess eligibility after accepting each prerequisite output.
- Give workers the task ID, objective, relevant input versions and references, permitted workspace and write scope, output and evidence requirements, and conditions for returning a blocker. Ask them to report observed checks and unresolved items. The coordinator checks returned versions and integrates the result.
- Run author checks and capture their actual outcomes. Apply Independent review to the pinned result and selected axes. For a consequential design choice, run the solution axis on the proposed approach early when its findings could affect implementation. Give corrections to an implementer, pin the revised result, and repeat the affected checks before acceptance.

## Handle blockers

Identify the affected task, criterion, or check and the input needed to continue. Resolve technical difficulties within the authorized goal and keep independent work moving. When executing the whole topic, pick up an eligible missing prerequisite within scope. When executing a single task, report missing results from outside that task.

Return to the user when a decision would materially change the expected behavior, acceptance criteria, or authorized scope. Explain what was discovered, the options and implications, and which work awaits the decision. Update the affected plan before acting on changed scope. For unavailable evidence, access, data, or an independent reviewer, name the precise missing input and the conditions for resuming.

Before yielding, record a checkpoint with the task or topic ID, current inputs, actual artifact locations and versions, completed work, check outcomes, pending actions, blocker, and next safe step. Make it readable in a fresh conversation with access to those inputs. Record an uncertain launch or external action as uncertain and reconcile it before retrying.

## Deliver the result

Use the [execution handoff](references/execution-handoff.md) for the result and any checkpoint. If Independent review is unavailable, continue authorized work and record the required independent checks as pending.

Return the report in the conversation. If the user requests a file or the project provides a writable location for execution artifacts, save it there and include its path. The user can request a separate Review later. Execute runs its own mandatory checks during this invocation.
