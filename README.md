# NDVI Workflow Lab: Building a Data Workflow with an AI Agent

GEOG 213/313 Advanced Geospatial Analytics with Python, Clark University.

In lectures 22 to 24 you designed a workflow to calculate a time series of
mean NDVI from Landsat for two NEON sites, San Joaquin Experimental Range
(SJER) in central California and Harvard Forest (HARV) in Massachusetts. In
this lab you build that workflow with an AI coding agent (GitHub Copilot in
Agent mode).

You own the parts of the work that need your judgment: the question, the
plan, the tests, the review of every change and the check that the results
make scientific sense. The agent writes most of the implementation.

## What you will practice

- Writing an `AGENTS.md` that turns your workflow design into instructions
  an agent can follow (lectures 04 and 22)
- Using your pseudocode as a plan, and asking the agent to critique it
  before any code exists (lecture 23)
- Specifying tests before any code exists, with expected answers you work
  out yourself, and checking that the tests can catch real mistakes
  (lecture 24)
- Building in small steps, one scene, then one site, then many sites, and
  reviewing each change before committing it
- Checking results against scientific expectations, not just passing tests
- Reviewing code an agent wrote without guidance

## Setup

You need git, [pixi](https://pixi.sh), VS Code and GitHub Copilot (free with
the GitHub Student Developer Pack). Running the full workflow (Part 5) needs
internet access to Microsoft Planetary Computer. The tests do not.

```
pixi install
pixi run test
```

## Parts

| Part | Instructions | Time | AI? |
|---|---|---|---|
| 0 | `prompts/00_setup.md` | 10 min | No |
| 1 | `prompts/01_write_agents_md.md` | 25 min | No |
| 2 | `prompts/02_critique_plan.md` | 15 min | Yes, as a reviewer |
| 3 | `prompts/03_specify_tests.md` | 30 min | Plan: no. Test code: yes |
| 4 | `prompts/04_build_one_scene.md` | 25 min | Yes |
| 5 | `prompts/05_build_site_and_workflow.md` | 30 min | Yes |
| 6 | `prompts/06_sanity_check.md` | 10 min | No |
| 7 | `prompts/07_code_review.md` | 20 min | No |
| 8 | `prompts/08_reflection.md` | homework | No |

## What to submit

Push these to your copy of the repository:

- `AGENTS.md`
- your test plan (`tests/TEST_PLAN.md`) and tests in `tests/`
- your code in `ndvi_workflow/`
- `outputs/all-sites-ndvi.csv` and the plot (or the file names you chose in
  `AGENTS.md`)
- `ai_logs/log.md` (and any exported chat sessions)
- `REVIEW.md`
- `REFLECTION.md`

## Commands

| Command | What it does |
|---|---|
| `pixi run test` | Run the tests |
| `pixi run workflow` | Run the full workflow and write to `outputs/` |
| `pixi run reset` | Throw away every uncommitted change (use after a bad agent run) |

## Data

`data/sites.geojson` contains a box of about 1 km x 1 km centered on the
NEON tower at each site. Landsat data come from the `landsat-c2-l2`
collection on [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/dataset/landsat-c2-l2).
