# Test plan

Write this yourself, without AI (Part 3). Work out every expected value by
hand and show the calculation. The agent will turn each row into a pytest
test.

## One-scene tests

| # | Function | Behavior to check | Input | Expected output (worked out by hand) | Why it matters |
|---|---|---|---|---|---|
| example | `normalized_diff` | `uint16` input does not wrap around | nir = 3000, red = 5000, both `uint16` | (3000 - 5000) / (3000 + 5000) = -0.25 | Landsat bands are stored as `uint16`; without converting to float, 3000 - 5000 wraps to 63536 and NDVI becomes 7.94 |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

## Break-it results (Part 4)

After the agent has implemented the functions and all tests pass, make each
change below by hand, run `pixi run test`, write down which tests failed, and
undo the change. If no test fails, your plan is missing a test.

| Change made to the code | Tests that failed |
|---|---|
| Remove the cloud mask (use all pixels) | |
| Remove the scale factor and offset | |
| Swap red and near-infrared in the NDVI calculation | |
