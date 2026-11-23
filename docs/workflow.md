# Walk through a draft-saving issue

## Start with a user report

Choose **Problem** and ask “A writer refreshed the editor and lost their last paragraph. Help me pin down what we need to fix.” Give the agent access to the relevant project files and answer questions about what the writer observed.

## From Problem to Plan

One detail changes the scope of the fix: did the writer see *Saved* before refreshing? Suppose they confirm they did, and that recovery while a save is in progress is outside this request. Problem reads its understanding back to the requester. A correction reopens the affected question. Once the outcome is clear, the requester can pass this brief to Plan in the same chat or a fresh one.

> **User report:** “I saw *Saved*, refreshed the editor, and lost my last paragraph.”
>
> **Expected outcome:** Once the editor shows *Saved*, refreshing the same draft restores the latest edit.
>
> **Scope:** This covers edits the editor has acknowledged as saved.
>
> **Success check:** Add a paragraph, wait for *Saved*, refresh, and compare the restored paragraph with the edit.
>
> **Open question:** Where is the edit lost?

Paste the brief into a fresh chat, select **Plan**, and ask it to prepare the work. The acceptance check is already clear. If locating the failure would change the scope of the fix, Plan can make that investigation the first task. [Example task dependency](../skills/plan/references/topic-and-tasks.md#example-dependency)

For example, the topic might be `draft-saving`, revision `r1`. The topic succeeds when the restored text matches the acknowledged edit. One possible split is:

| Task | What the team can accept | Dependency |
|---|---|---|
| T1 · Reproduce the loss | A repeatable sequence and observations showing where the acknowledged text is lost, or a record of what the bounded investigation could establish. | Ready to start. |
| T2 · Preserve acknowledged edits | On the revised editor, the same sequence restores the exact paragraph. A regression check covers that sequence. | Needs a reproduction and evidence locating the loss. An inconclusive T1 leaves T2 blocked. |

If the cause is known and the change is local, one task can cover the fix and the regression check. To challenge the plan first, give Review the topic and brief. It can flag missing coverage, a dependency that prevents work from starting, or a criterion nobody can test. Plan can use those findings to revise the topic before implementation.

## Execute a task or the whole topic

Ask “Complete T1 and return the reproduction steps and evidence,” or select the whole topic to include implementation and the combined acceptance check. The coordinator handles closely coupled steps itself. When work can be delegated, each worker gets a task ID, its inputs, its write scope, and the evidence to return. The coordinator integrates the changes and checks the combined behavior.

Suppose investigation reveals that the editor also displays *Saved* while offline. Should that promise survive a refresh before the server receives the edit? The requester owns that product decision. The coordinator describes what each choice would mean and continues any independent work, such as reproducing the online case. If offline recovery enters scope, update the topic revision and its criteria before implementing it. If the answer has to wait, a checkpoint records the affected task, revision, evidence, and next safe step.

## Verify, correct, and recheck

For the fix itself, Execute records the author’s regression check and requests independent verification against the exact revision. A behavior reviewer gets the brief and tries the writer’s sequence. A separate implementation reviewer inspects the changed code and its failure paths. Other applicable checks cover the design choice, documented project rules, and efficiency when resource use matters. Reviewers start with the relevant evidence and form their own conclusions before seeing other verdicts.

Suppose a reviewer reproduces the loss when refreshing immediately after *Saved*. The report gives the revision, steps, expected text, and observed text. Execute takes the finding back to an implementer. A reviewer checks the corrected revision and repeats the affected checks. When all mandatory checks pass, the coordinator can hand back a verified result. If required evidence or an independent check is missing, the handoff names what remains open.

Choose standalone **Review** when you want another assessment of the plan, the delivered fix, or a revision after feedback. Provide the applicable criteria and exact target, plus the earlier report for a re-review. A new chat can follow the finding from the original requirement to the correction using those references.
