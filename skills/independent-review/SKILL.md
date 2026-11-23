---
name: independent-review
description: Shared verification procedure for execution and review workflows. Assign each area requiring judgment to a fresh reviewer and collect verdicts and evidence for the exact version under review.
---

# Independent review

Internal procedure for Execute and Review. Read [result axes](references/result-axes.md) when selecting checks for a result. For a plan, use the axes supplied by the caller. When asked only to prepare checks, return the applicable axes and expected evidence and stop before dispatch.

## Prepare the inputs

1. Pin the reviewed material and related criteria or brief. For a comparison, pin the exact base and result, verify that they resolve, and confirm the change set matches the requested scope. Use the effective merge base when reviewing a branch against its target. Include selected uncommitted work in an inspectable snapshot. Investigate an unexpected empty diff before dispatch.
2. Resolve the relevant intent, decisions, applicable project rules and evidence. Record which rules tooling covers and which require judgment. Give each axis its relevant inputs. When inputs are missing or contradictory, identify the affected criteria and continue every check with sufficient evidence, including others on the same axis.

## Run the assignments

Assign each selected judgment axis to a separate agent in a fresh context using permitted host tools. Select reviewers who did not author or modify the target. Give them their axis, scope, exact target and baseline where relevant, sources, criteria and required output below. Allow inspection and reproducible checks within existing permissions. Keep the target read-only and use isolation for checks that would change it.

Exclude implementation history, expected conclusions and other reviewers' reports from the initial context. For re-review, pass prior findings as scenarios to investigate afresh. Run independent assignments in parallel when they can inspect the same pinned material safely. Record automated and author evidence separately. An unavailable independent assignment stays pending.

## Return evidence by axis

Include the reviewer or tool, pinned references, checked criteria, expected and observed outcomes, evidence and gaps. Report confirmed defects, documented rule violations, uncertainties and optional improvements separately. Support defects with the location or scenario, trigger and consequence. Cite the documented rule and affected change for violations. Apply project rules before general design or readability heuristics.

Keep verdicts separate. **Passed** requires the selected checks and required independent judgment to pass. **Failed** means evidence establishes a blocking defect or violation. **Pending** means a required input, check or reviewer is missing and no blocking defect has been established on that axis. A confirmed blocker takes precedence. List outstanding checks alongside the failure. **Not applicable** means the axis does not apply to the stated scope. A tool that could not run leaves a gap unless its failure itself establishes a defect. Passing tool or author evidence can coexist with a pending independent review.

Retain reports against their original versions and repeat affected checks after a change. If a reviewer authors a correction, assign another reviewer to that scope. Return evidence and blockers to the caller, which owns the final disposition.
