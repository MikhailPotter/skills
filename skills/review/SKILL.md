---
name: review
description: Independently review an implementation plan or a specific revision of a deliverable against its requirements. Report findings with evidence, or recheck a revised result after feedback.
---

# Review

Review the user's selected material and report in their language. Keep the reviewed artifact and task state read-only. Run checks when permitted and use an isolated workspace if a check would change the reviewed material. The output is a review report that the user can give to Plan or Execute.

## Resolve and pin the inputs

| Request | Inputs |
|---|---|
| Review a plan | The topic, task cards, originating brief and material decisions. |
| Review a result | The exact result or inspectable snapshot, relevant requirements and rules, and a baseline where the review compares changes. |
| Re-review a revision | The new result, previous report, the versions covered by that report, and the changes since its review. |

Resolve references from the request and available workspace or conversation. Pin the plan or result, the applicable brief and, when relevant, the exact baseline. For code comparisons, confirm that the change set covers the requested scope, including work in progress when selected. Give reviewers reproducible references to the same snapshot. Resolve a materially ambiguous target with the user. If a reference or source is missing, explain which axis it blocks and proceed with unaffected axes.

## Select the axes

Use the [plan axes](references/axes-and-report.md#plan-axes) for a plan. For a result, read and apply [Independent review](../independent-review/SKILL.md) in preparation mode. Honor a narrowed request and label the resulting coverage. For a general review, include applicable axes required by the acceptance criteria or project rules. On re-review, check the selected findings and regressions the new changes could introduce. Carry prior evidence forward only when you can establish that it still applies. Label it separately.

## Dispatch independent review

Read and apply Independent review to the selected axes, exact target, sources, and any previous findings. Run permissible automatic checks and include their evidence. If Independent review is unavailable, record the missing assignments and preserve any confirmed failures. Label any inline assessment by its source.

## Return the report

Use the [report format](references/axes-and-report.md#report-format). Preserve each axis's scope, verdict and evidence gaps. Reconcile conflicting findings against their cited criteria and evidence, and record unresolved disagreements. The summary covers the stated scope. Return **changes requested** when a confirmed blocking finding exists and list any pending axes alongside it. Otherwise return **inconclusive** when required evidence or independent review is missing, or **passed** once the applicable checks pass.

Return the report in the conversation. Save it when requested or when the project provides a writable location for review reports. End with the changes requested, the missing evidence, or the scope that passed.
