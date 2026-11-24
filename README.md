# Engineering Workflow Skills

These agent skills bring the division of responsibilities familiar from large engineering teams into your project. You own the product decision. An analyst helps you define what success looks like, an engineer plans and implements the change, and independent reviewers check the result against the same brief.

Start with a bug report, a feature request, or an area worth investigating. You choose when to move from discovery to planning and implementation. Each stage leaves a Markdown handoff, so another agent can pick up the work in a fresh chat.

## Install

With Node.js and npm installed, run this command from your project root to install all five skills together.

```sh
npx skills@latest add MikhailPotter/skills --skill "*"
```

Choose your agent and select **Project** if prompted for the installation scope. The command installs the four workflow skills and their shared review helper.

To check the installation, run the following from the same project:

```sh
npx skills@latest list
```

Look for five entries from `MikhailPotter/skills`: `execute`, `independent-review`, `plan`, `problem`, and `review`.

**Try Problem.** Open a new chat in the project, select **Problem**, and ask “I saw *Saved*, refreshed the editor, and lost my last paragraph. Help me define what we need to fix.”

Problem might reply, “The editor acknowledged the edit, but reopening the draft lost it. To check a fix, add a paragraph, wait for *Saved*, then refresh the same draft. The restored paragraph should match the edit. We still need to find where the text was lost.” [Follow this example through planning, implementation, and independent review.](docs/workflow.md)

## How the team works

| Skill | Responsibility | What passes to the next person or agent |
|---|---|---|
| [Problem](skills/problem/SKILL.md) | Like a product analyst, the agent investigates what it can, asks you about decisions that change the goal, then tells you how it understood the request. | A brief with scope, a concrete success check, and open questions. A discovery-only request can end with findings. |
| [Plan](skills/plan/SKILL.md) | Like a technical lead, the agent starts with one task and splits it when a piece can be accepted separately or unlocks another decision. | A versioned topic with task IDs, acceptance criteria, dependencies, and a starting point. |
| [Execute](skills/execute/SKILL.md) | A coordinator owns the selected task or topic. It can delegate bounded work, integrate the results, and arrange independent checks. | A result tied to a revision and evidence, or a checkpoint recording the blocker and what would allow work to resume. |
| [Review](skills/review/SKILL.md) | Independent reviewers assess a plan before implementation or a specific result afterward. You can also request a re-review after a correction. | A report linking findings to criteria and evidence. Changes to the plan go back to Plan. Corrections to the result go back to Execute. |

**When new evidence changes the scope, the decision comes back to you.** The coordinator explains the options and continues any work that can proceed independently. Once you decide, the affected plan and criteria are updated before work resumes.

**Execute includes verification.** Both Execute and Review use [Independent review](skills/independent-review/SKILL.md), the fifth skill in the bundle. Each question requiring independent judgment goes to a reviewer who did not author the change. They receive the brief, criteria, and exact revision in a fresh context. If a required reviewer is unavailable, that check stays pending.

## Updates

See the [release notes](RELEASE-NOTES.md) for changes and migration guidance.

To update these five project skills, run this command from the project where you installed them:

```sh
npx skills@latest update --project execute independent-review plan problem review
```

## Feedback and contributions

For installation issues, [open an issue](https://github.com/MikhailPotter/skills/issues) with your agent, the output of `npx skills@latest --version`, the command you ran, and the result you saw.

Before submitting a pull request, run `python3 scripts/check-install.py` from your checkout with Node.js, npm, Git, and Python 3 installed. The check installs the checkout into a temporary project and verifies the bundle and its documentation links.

## License

Released under the [MIT License](LICENSE).
