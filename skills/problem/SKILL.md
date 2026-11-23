---
name: problem
description: Investigate a bug report, feature request, or problem area. Use evidence and a short interview to write a problem brief with scope and signs of success, or report findings for further investigation.
---

# Problem

Use the text following the invocation as the starting request. Continue the same interview when the user answers or corrects it. Speak and write in the user's language unless they request another.

Produce a problem brief or investigation findings. The brief describes the outcome the user wants and how to recognize it. Leave task decomposition and implementation for separately requested work.

## Establish the starting point

Identify the area, the requested outcome of this conversation, and what the user already decided. The request may describe a defect, an area to investigate, or a proposed solution. Infer the underlying problem where supported and ask when competing interpretations would lead to substantially different work.

Inspect available, relevant sources before asking for facts you can look up. Look at existing behavior, examples, documentation and prior decisions as appropriate. Distinguish verified observations, reported observations, hypotheses, user decisions and working assumptions. Bound any broad investigation to the area the user described. Report gaps in access or coverage.

## Run the interview in rounds

1. Identify the nearest unresolved decisions that could substantially change the problem, desired outcome, scope or signs of success. For each, check whether it depends on another answer or a fact still being investigated.
2. Resolve available facts yourself. If an observation is available only to the user, ask for a concrete example or condition. Ask the user to decide tradeoffs that require their intent or authority. For delegated, reversible details, state a working assumption when it matters to the brief.
3. Ask the highest-impact question first when other questions depend on it. Group a short set of independent questions when each answer is useful on its own. Use plain wording, explain what changes with the answer, and recommend an option when evidence supports one. Use an open question when the need is still unclear.
4. Wait for answers before proceeding on dependent questions or decisions. Continue investigation that can proceed independently. After each reply, update the working understanding, resolve newly answerable facts, and reconsider the next round. Reuse settled answers and explicitly surface material contradictions or corrections.

Carry technical unknowns forward when they can be investigated within a clear goal.

## Read back and stop

Read back the understood problem, who it affects, the desired outcome, scope and a concrete success example. If the user corrects the readback, update the affected parts and reopen only questions made relevant by the correction.

Choose the applicable exit:

- **Ready for planning.** The problem, affected users or process, desired result, material boundaries and observable signs of success are clear enough to plan work. List remaining investigation questions, including any unconfirmed technical cause. A clear, authorized brief can end with the readback. Record explicit confirmation only when the user actually gives it.
- **Awaiting a decision.** A material question about the goal, scope or success blocks a usable brief. Return the current brief with the exact question, the consequence of leaving it open, and what would allow planning to start. Continue the same interview when the user replies.
- **Findings delivered.** The user asked for investigation within an area. Report confirmed findings with evidence, distinguish unconfirmed observations, and state coverage and limits. If the investigation found no confirmed issues, report what was checked and what remained outside the investigation.

## Deliver the handoff

Use the [problem brief template](references/problem-brief.md) for a planning handoff or a brief awaiting a decision. Make the handoff readable in a fresh conversation. Include source references and enough context to interpret them. For an investigation-only request, use the findings format in the same reference.

Return the Markdown in the conversation. When the user requests a file or the project already provides a location for this artifact, save it there if writable and return its path. Copying the brief into a new conversation is a valid handoff. End with the outcome requested by the user. A later explicit `Plan` invocation can consume the brief.
