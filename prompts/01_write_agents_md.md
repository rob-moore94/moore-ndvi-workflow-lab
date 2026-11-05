# Part 1: Write AGENTS.md (25 min, no AI)

Fill in every TODO in `AGENTS.md` yourself, without AI. This is the part of
the work an agent cannot do for you: it does not know your question, why one
dataset fits it better than another, or what your users need.

Use lectures 22 and 23:

- What this project is: the NDVI seasonality question for SJER and HARV, and
  why the two sites are worth comparing.
- Data: Landsat Collection 2 Level-2 from Landsat 8 and 9, which you can
  find on Microsoft Planetary Computer as the `landsat-c2-l2` collection
  (as in lectures 13 and 17). Say why it fits the question better than the
  alternatives, and give the time period (2023).
- Outputs: one csv file and one plot that include both sites. Give the file
  names and the csv columns.
- Workflow: your pseudocode from lecture 23, with the inputs and outputs of
  each block. Name the module and function for each block. A suggested
  layout:
  - `ndvi_workflow/scene.py`: calculations for one scene (pure functions)
  - `ndvi_workflow/data.py`: reading the sites, searching for scenes and
    loading the bands (the only module that uses the network)
  - `ndvi_workflow/site.py`: all scenes for one site
  - `ndvi_workflow/workflow.py`: all sites, writing the outputs
  - `ndvi_workflow/__main__.py`: so that `pixi run workflow` runs everything

Leave the Domain rules section short for now; you will add to it in Part 2.

When you are done, commit:

```
git add AGENTS.md
git commit -m "Write AGENTS.md"
```
