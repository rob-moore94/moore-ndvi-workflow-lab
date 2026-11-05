# Part 0: Set up (10 min)

1. Make your own copy of this repository: on the lab's GitHub page, click
   "Use this template", then "Create a new repository". Make it private and
   add the instructors as collaborators. Clone your copy.
2. In the terminal, from the repository folder, run:

   ```
   pixi install
   pixi run test
   ```

   You should see `6 passed`. These tests come with the starter code and
   check `ndvi_workflow/indices.py`, which you know from lecture 24.
3. Run `git status` and make sure the working tree is clean.
4. Open the folder in VS Code. Open Copilot Chat and make sure it is in
   Agent mode (see lecture 04).
5. Read `README.md`, `AGENTS.md`, `tests/test_indices.py` and
   `tests/conftest.py`.

## Rules for the whole lab

- Commit before every agent session. If a session goes badly, run
  `pixi run reset` to throw away every uncommitted change.
- Start a new chat session for each part. Long sessions use more credits
  and make the agent less focused.
- When the agent asks to run a command, only allow `pixi run test` with
  "Allow Exact Command Line in this Workspace". Read any other command
  before you allow it.
- Keep notes in `ai_logs/log.md` as you go: what you asked, what the agent
  did, what you had to fix, and the credits used. Write the notes yourself.
