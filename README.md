# Engineering Workflow Skills

These agent skills bring the division of responsibilities familiar from large engineering teams into your project. You own the product decision. An analyst helps you define what success looks like, an engineer plans and implements the change, and independent reviewers check the result against the same brief.

Start with a bug report, a feature request, or an area worth investigating. You choose when to move from discovery to planning and implementation. Each stage leaves a Markdown handoff, so another agent can pick up the work in a fresh chat.

## Install

With Node.js and npm installed, run this command from your project root to install all five skills together.

```sh
npx skills@latest add MikhailPotter/skills --skill "*"
```

Choose your agent and select **Project** if prompted for the installation scope. The command installs the four workflow skills and their shared review helper.

**Try Problem.** Open a new chat in the project, select **Problem**, and give it a user report to investigate.

> **Report:** “I saw *Saved*, refreshed the editor, and lost my last paragraph.”
>
> **Acceptance check:** Add a paragraph, wait for *Saved*, then refresh the draft. The restored paragraph must match the edit.
>
> **Independent review:** Give a fresh reviewer the brief and the exact revision of the fix. Ask them to repeat the check and report what the editor restored.

## How the team works

| Skill | Responsibility | What passes to the next person or agent |
|---|---|---|
| [Problem](skills/problem/SKILL.md) | Like a product analyst, the agent investigates what it can, asks you about decisions that change the goal, then tells you how it understood the request. | A brief with scope, a concrete success check, and open questions. A discovery-only request can end with findings. |
| [Plan](skills/plan/SKILL.md) | Like a technical lead, the agent starts with one task and splits it when a piece can be accepted separately or unlocks another decision. | A versioned topic with task IDs, acceptance criteria, dependencies, and a starting point. |
| [Execute](skills/execute/SKILL.md) | A coordinator owns the selected task or topic. It can delegate bounded work, integrate the results, and arrange independent checks. | A result tied to a revision and evidence, or a checkpoint recording the blocker and what would allow work to resume. |
| [Review](skills/review/SKILL.md) | Independent reviewers assess a plan before implementation or a specific result afterward. You can also request a re-review after a correction. | A report linking findings to criteria and evidence. Changes to the plan go back to Plan. Corrections to the result go back to Execute. |

**When new evidence changes the scope, the decision comes back to you.** The coordinator explains the options and continues any work that can proceed independently. Once you decide, the affected plan and criteria are updated before work resumes.

**Execute includes verification.** Both Execute and Review use [Independent review](skills/independent-review/SKILL.md), the fifth skill in the bundle. Each question requiring independent judgment goes to a reviewer who did not author the change. They receive the brief, criteria, and exact revision in a fresh context. If a required reviewer is unavailable, that check stays pending.

[Walk through the draft-saving issue](docs/workflow.md) to see the interview, task dependencies, a scope decision, and the correction loop.

## Updates

To update the installed workflow later, run `npx skills@latest update` from the same project.
