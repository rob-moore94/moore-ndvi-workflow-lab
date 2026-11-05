# Part 5: Build one site, then many sites (30 min)

Use two separate chat sessions, and commit after each one.

## Session A: one site

Optional but recommended: first add one or two rows for your one-site
function to `tests/TEST_PLAN.md`, for example that two scenes on the same
date are reduced to one, or that scenes with too few clear pixels are
dropped. Then ask the agent, in its own session, to write only those tests
in `tests/test_site.py` (as in Part 3), and review them before you continue.

Then paste:

```
Read AGENTS.md. Implement the data access functions in ndvi_workflow/data.py
(read the site boundaries, search Planetary Computer for Landsat 8 and 9
Collection 2 Level-2 scenes, and load the red, near-infrared and QA_PIXEL
bands for one site with stackstac) and the one-site function in
ndvi_workflow/site.py. Reuse the functions in ndvi_workflow/scene.py.
Do not modify anything in tests/ or data/. Run `pixi run test` when you are done.
```

Review the diff as in Part 4. In particular, check how the site boundary is
reprojected before cropping, and how the scale factor is handled. Then commit.

## Session B: many sites

Paste:

```
Read AGENTS.md. Implement the many-sites workflow in ndvi_workflow/workflow.py
and a command line entry point in ndvi_workflow/__main__.py, so that
`pixi run workflow` writes the outputs described in AGENTS.md to outputs/.
Do not modify anything in tests/ or data/.
```

Review the diff. Is the csv written once, after the loop over sites? Then
run the workflow yourself (it needs internet and may take a few minutes):

```
pixi run workflow
```

Commit your code and the files in `outputs/`.
