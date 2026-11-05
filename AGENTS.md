# AGENTS.md

Guidance for coding agents working in this repository. Read this before making
any change.

<!--
Part 1 of the lab: replace every TODO below with your own words, written
without AI. Keep the sections marked "(set by the instructor)" as they are.
Be specific: the agent only knows what you write here and what is in the code.
-->

## What this project is

TODO: The question this workflow answers, who will use the outputs, and why
it matters (lecture 22).

## Data

TODO: Which dataset you will use (collection, satellites, processing level),
why it fits the question (temporal frequency, resolution), the time period,
and where the site boundaries come from (`data/sites.geojson`).

## Outputs

TODO: Exactly what the workflow produces: file names, csv columns (with
units), and what the plot shows.

## Workflow

TODO: Your pseudocode from lecture 23, from one scene to one site to many
sites, with the inputs and outputs of each block. For each block, name the
module and function that will implement it, for example
`ndvi_workflow/scene.py: scene_ndvi_stats(red_dn, nir_dn, qa)`.

## Domain rules

TODO: Scientific rules the code must follow. You will add to this section in
Part 2 of the lab.

## Project layout (set by the instructor)

```
pixi.toml        environment and tasks (the only place commands are defined)
pytest.ini       test settings
data/            input data (read-only)
ndvi_workflow/   the Python package, one module per stage of the workflow
tests/           tests and the test plan (the plan is written by the student)
outputs/         everything the workflow writes
review/          code review exercise (do not edit)
prompts/         lab instructions
ai_logs/         the student's notes and exported chat logs
```

## Environment and tooling (set by the instructor)

- This project uses pixi for everything. Never run or suggest `pip`, `conda`,
  `venv` or `virtualenv`, and never create `requirements.txt`.
- Do not add dependencies. If you think one is needed, stop and ask.
- Do not edit the `[tasks]` section of `pixi.toml`.
- Run the tests with `pixi run test`. Run the workflow with `pixi run workflow`.

## Code rules (set by the instructor)

- Never modify, move or delete anything in `data/`.
- Write outputs only to `outputs/`.
- Do not change anything in `tests/` unless the user explicitly asks. When
  asked to write tests, follow `tests/TEST_PLAN.md` exactly and use its
  expected values as written. If a test looks wrong, stop and explain why
  instead of changing it.
- Do not edit anything in `review/`.
- Keep functions small, with one job each, and give each a numpydoc
  docstring (Parameters, Returns).
- Keep scientific calculations in pure functions: arrays in, arrays or
  numbers out, with no network or file access, so they can be tested
  without internet. Network access belongs only in `ndvi_workflow/data.py`.
- Catch specific exceptions only. Never use a bare `except:`.

## Definition of done

1. `pixi run test` passes.
2. Only the files needed for the task changed (check with `git status`).
3. TODO: Add the checks that tell you the results are scientifically
   sensible (Part 6 of the lab will help).
