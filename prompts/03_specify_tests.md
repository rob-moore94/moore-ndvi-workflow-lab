# Part 3: Specify the tests, then have the agent write them (30 min)

In the agentic loop, the agent runs the tests and keeps working until they
pass, so the tests define what "correct" means. An agent can write pytest
code for you. Deciding what to test, and what the right answers are, is
your job.

## Step 1: Write a test plan (15 min, no AI)

Fill in the table in `tests/TEST_PLAN.md` for the one-scene functions you
named in `AGENTS.md`. For each test, write the function, the behavior it
checks, a small input (a few pixels is enough), the expected output and why
the test matters. The example row shows the level of detail.

Work out every expected value by hand or with a calculator, and show the
calculation. Do not get expected values from your code or from the agent: a
test whose expected value comes from the same formula as the code can never
fail. Use reflectance values for the inputs, and the `QA_*` values in
`tests/conftest.py` for clear, cloudy and other pixels.

At a minimum, plan tests that check that:

- cloudy and cloud-shadow pixels do not change the mean NDVI of a scene
- the scale factor and offset are applied (NDVI calculated from the raw
  digital numbers is different from NDVI calculated from reflectance)
- a fully cloudy scene gives nan as its mean NDVI
- mean NDVI always stays between -1 and 1
- your functions work for one scene (dims y, x) and for a stack of scenes
  (dims time, y, x)

Commit:

```
git add tests/TEST_PLAN.md
git commit -m "Add test plan"
```

## Step 2: Have the agent write the test code (10 min)

Start a new chat session in Agent mode and paste:

```
Read AGENTS.md and tests/TEST_PLAN.md. Write each row of the test plan as a
pytest test in tests/test_scene.py, using the helpers in tests/conftest.py
and the style of tests/test_indices.py. Use the expected values exactly as
they are written in the plan; do not calculate them with code. Do not
implement the functions being tested, and do not change any other file.
```

## Step 3: Review the tests (5 min)

Read `tests/test_scene.py` line by line and check that:

- there is one test for each row of the plan
- each assertion uses the expected value from your plan, typed as a number,
  not calculated with the same formula as the code (for example,
  `expected = (nir - red) / (nir + red)` is a red flag)
- each test checks values, not only that the code runs or that the output
  has the right shape
- tolerances are tight (for example `abs=1e-3`, not `abs=0.5`)

Run `pixi run test`. The new tests should fail because the functions do not
exist yet. That is expected. Make sure they fail for that reason (an
`ImportError` or `AttributeError`), not because of a mistake in a test.

In Part 4 you will check that the tests can catch real mistakes.

Commit:

```
git add tests/test_scene.py ai_logs/log.md
git commit -m "Add tests for one scene"
```
