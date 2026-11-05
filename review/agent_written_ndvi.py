"""
NDVI time series for NEON sites.

This script was written by an AI coding agent in one turn, from this prompt:

    "Write a script that calculates the average NDVI for every Landsat scene
    in 2023 for each site in data/sites.geojson, then saves the results to a
    csv and plots them."

It is used for the code review exercise in Part 7 of the lab.
Read it, but do not run it and do not edit it.
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import planetary_computer
import pystac_client
import rasterio
from rasterio.mask import mask

STAC_URL = "https://planetarycomputer.microsoft.com/api/stac/v1"

catalog = pystac_client.Client.open(STAC_URL, modifier=planetary_computer.sign_inplace)
sites = gpd.read_file("data/sites.geojson")

for _, site in sites.iterrows():
    # Find all Landsat scenes for this site in 2023
    search = catalog.search(
        collections=["landsat-c2-l2"],
        intersects=site.geometry,
        datetime="2023-01-01/2023-12-31",
    )
    items = list(search.items())
    print(f"Found {len(items)} scenes for {site['name']}")

    results = []
    for item in items:
        try:
            # Read the red and near-infrared bands, cropped to the site
            with rasterio.open(item.assets["red"].href) as src:
                red, _ = mask(src, [site.geometry], crop=True)
            with rasterio.open(item.assets["nir08"].href) as src:
                nir, _ = mask(src, [site.geometry], crop=True)

            # Quality band
            qa = rasterio.open(item.assets["qa_pixel"].href)

            # Calculate NDVI
            ndvi = (nir - red) / (nir + red)

            results.append({"date": item.datetime.date(), "ndvi": np.nanmean(ndvi)})
        except:
            print("Skipping scene with missing data")

    # Save the results
    df = pd.DataFrame(results)
    df.to_csv("data/ndvi_results.csv")

    # Plot the time series
    plt.plot(df["date"], df["ndvi"])
    plt.title("NDVI time series")
    plt.savefig("data/ndvi_plot.png")

print("Done!")
