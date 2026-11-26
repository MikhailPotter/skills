# Engineering Workflow Skills

These agent skills bring the division of responsibilities familiar from large engineering teams into your project. You own the product decision. An analyst helps you define what success looks like, an engineer plans and implements the change, and independent reviewers check the result against the same brief.

Start with a bug report, a feature request, or an area worth investigating. You choose when to move from discovery to planning and implementation. Each stage leaves a Markdown handoff, so another agent can pick up the work in a fresh chat.

## Install

With Node.js and npm installed, run this command from your project root to install all five skills together.

```sh
npx skills@latest add MikhailPotter/skills --skill "*"
```

Choose your agent and select **Project** if prompted for the installation scope. The command installs the four workflow skills and their shared review helper.

## Try it on your own bug

Open a chat with your coding agent in the project where you installed the skills. Select the `problem` skill and describe one bug. The examples below use `$skill` mentions. If your agent uses a skill menu or another syntax, select the named skill there and send the text that follows. Include what you did, what happened, and what you expected. For example:

```text
$problem I saved Europe/Paris as my time zone in Settings. When I refreshed the page, it showed UTC again. I expected my saved choice to stick.
```

The agent checks the relevant code and may ask a follow-up question. You get a short brief in the chat with the symptom, the expected behavior, and a way to tell whether a fix worked. For this bug, the check could be:

> Save Europe/Paris, refresh Settings, and check that the selected time zone is still Europe/Paris.

Once the brief matches your bug, send this in the same chat:

```text
$plan Use the brief above to plan the fix. Include a regression test for the refresh case.
```

You get a plan with tasks and acceptance criteria. When you're ready for code changes, send:

```text
$execute Implement the plan above and show whether the saved time zone survives a refresh.
```

Execute reports the changes and verification results, including any checks it couldn't complete. For another example, [follow a lost editor draft from bug report through independent review](docs/workflow.md).

### Check your installation

If the skill is missing from your agent’s skill list, run the following command from your project root.

```sh
npx skills@latest list
```

Look for five entries from `MikhailPotter/skills`: `execute`, `independent-review`, `plan`, `problem`, and `review`.

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
