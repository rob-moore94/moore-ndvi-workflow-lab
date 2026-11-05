# Part 4: Build one scene with the agent (25 min)

Run `git status` and make sure everything is committed. Start a new chat
session in Agent mode and paste:

```
Read AGENTS.md. Implement the one-scene functions described in the Workflow
section in ndvi_workflow/scene.py, so that the tests in tests/test_scene.py
pass. Do not modify anything in tests/ or data/. Run `pixi run test` when you
are done.
```

When the agent finishes:

1. Run `pixi run test` yourself.
2. Run `git status`. If the agent changed anything in `tests/` or `data/`,
   run `pixi run reset` and start again with a clearer prompt.
3. Read the full change with `git diff`. You should be able to explain every
   line. Check it against lecture 24:
   - Is there a bare `except` that could hide a real error?
   - Are the bands converted to float before any math?
   - Does each function always return the same type?
   - Are the scale factor, offset and QA bits the ones in your AGENTS.md?
4. Commit the working code:

   ```
   git add ndvi_workflow/scene.py
   git commit -m "Implement one-scene functions"
   ```

5. Break it on purpose, to check that your tests can catch real mistakes.
   For each change listed under "Break-it results" in `tests/TEST_PLAN.md`:
   make the change by hand in `ndvi_workflow/scene.py`, run
   `pixi run test`, write down which tests failed, and undo the change with
   `git checkout -- ndvi_workflow/scene.py`.

   If a change makes no test fail, your tests are not checking what you
   think. Add a row to the plan, ask the agent (in a new session) to write
   only that test, and repeat the check.
6. Note in `ai_logs/log.md` what the agent did well, what you had to fix,
   and the credits used (lecture 04 shows where to find them). Commit:

   ```
   git add tests/ ai_logs/log.md
   git commit -m "Break-it check for one-scene tests"
   ```
