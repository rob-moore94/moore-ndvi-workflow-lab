# Part 2: Ask the agent to critique your plan (15 min)

Before any code is written, use the agent as a reviewer. Start a new chat
session in Agent mode and paste:

```
Read AGENTS.md. Do not write or change any code or files.
Review the Workflow section as an experienced remote sensing scientist would.
List any steps that are missing or that would give wrong NDVI values, and
explain in one or two sentences why each one matters.
```

Then:

1. Compare the agent's list with the answer to "What is missing from this
   pseudocode?" in lecture 23. In `ai_logs/log.md`, note which items the
   agent found, which it missed, and anything it suggested that you think
   is wrong or unnecessary.
2. Update the Workflow and Domain rules sections of `AGENTS.md` yourself.
   Be specific: for example, which QA_PIXEL bits mark a pixel as unusable,
   the scale factor and offset, and the minimum fraction of clear pixels
   for a scene to be kept.
3. Commit:

   ```
   git add AGENTS.md ai_logs/log.md
   git commit -m "Update plan after review"
   ```
