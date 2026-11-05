# Part 6: Check the science (10 min, no AI)

Passing tests show that the code does what you specified. They do not show
that the result is right. Open the csv file and the plot in `outputs/` and
check:

1. There is one csv file and one plot, and both include both sites.
2. All mean NDVI values are between -1 and 1, and values for vegetation are
   roughly between 0.2 and 0.9.
3. The number of scenes makes sense. Landsat 8 and 9 together observe a
   location about every 8 days. How many scenes were found for each site, and
   how many were kept after cloud filtering? Why might HARV keep fewer?
4. The seasonal pattern matches what you know from lecture 22: SJER should
   green up with the winter rains, peak in early spring and brown down by
   late spring, while HARV should peak in summer. The two curves should look
   nearly opposite.

If any check fails, find out why before you change any code. Write down
what you found in `REFLECTION.md`, then add these checks to the Definition
of done in `AGENTS.md`.

<details>
<summary>Hints if your curves look wrong</summary>

- Are all values close to 0, or is the curve almost flat? Check whether the
  scale factor and offset are applied twice. `stackstac.stack` applies them
  automatically unless you pass `rescale=False`.
- Are there sudden drops in NDVI? Check the cloud mask and the minimum
  fraction of clear pixels.
- Are there values above 1? Check pixels with negative reflectance.
- Did you get no scenes at all? Check the CRS of the site boundary when
  cropping.

</details>
