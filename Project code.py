# Research question:
# Is the mass of a supermassive black hole related to the bolometric luminosity of its active galactic nucleus?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Read the black hole dataset

data = pd.read_csv(
    "black_hole_data.txt",
    sep="|",       # The columns in the dataset are separated by |
    skiprows=2     # Skip the first two lines because they contain dataset information
)

# Remove columns that are completely empty

data = data.dropna(axis=1, how="all")

# Remove extra spaces from the column names

data.columns = data.columns.str.strip()

# Convert the black hole mass and luminosity columns to numbers

# If a value is blank or cannot be converted to a number,

# errors="coerce" changes it into NaN (a missing value)

data["log_bh_mass"] = pd.to_numeric(
    data["log_bh_mass"],
    errors="coerce"
)

data["log_lbol"] = pd.to_numeric(
    data["log_lbol"],
    errors="coerce"
)

# Remove rows where black hole mass or luminosity is missing

# We need both measurements to investigate the relationship between them

clean_data = data.dropna(
    subset=["log_bh_mass", "log_lbol"]
)

# Print the number of objects before and after removing missing values

print("Number of objects in original dataset:", len(data))
print("Number of objects used in analysis:", len(clean_data))

# Store the black hole masses and luminosities

black_hole_mass = clean_data["log_bh_mass"]
luminosity = clean_data["log_lbol"]

# --------------------------------------------------
# Figure 1: Distribution of black hole masses
# --------------------------------------------------

plt.hist(
    black_hole_mass,
    bins=15,
    edgecolor="black"
)

# Label the x-axis

plt.xlabel(r"$\log_{10}(M_{\rm BH}/M_\odot)$")

# Label the y-axis

plt.ylabel(
    "Number of AGN"
)
# Add a title

plt.title(
    "Distribution of Black Hole Masses"
)

# Save the graph as a PNG file

plt.savefig(
    "black_hole_mass_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the graph

plt.show()

# --------------------------------------------------
# Figure 2: Black hole mass vs AGN luminosity
# --------------------------------------------------

# Create a scatter plot

# Each point represents one AGN

plt.scatter(
    black_hole_mass,
    luminosity
)

# Label the x-axis

plt.xlabel(r"$\log_{10}(M_{\rm BH}/M_\odot)$")


# Label the y-axis

plt.ylabel(r"$\log_{10}(L_{\rm bol}/L_\odot)$")

# Add a title to the graph

plt.title(
    "Black Hole Mass vs AGN Luminosity"
)

# Save the graph as a PNG file

plt.savefig(
    "black_hole_mass_vs_luminosity.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the graph

plt.show()

# --------------------------------------------------------
# Calculate the Pearson correlation coefficient
# --------------------------------------------------------

# This measures the strength of the linear relationship

# between black hole mass and AGN luminosity

correlation, _ = stats.pearsonr(
    black_hole_mass,
    luminosity
)

# ---------------------------------------------------------
# Calculate the statistical uncertainty using bootstrapping
# ---------------------------------------------------------

# Set a random seed so the results can be reproduced

np.random.seed(42)

# Choose the number of bootstrap samples

number_of_bootstraps = 10000

# Create an empty list to store the Pearson correlation
# coefficient from each bootstrap sample

bootstrap_correlations = []

# Create 10,000 bootstrap samples

for i in range(number_of_bootstraps):

    # Randomly select 150 AGNs from the original sample
    # with replacement
    #
    # replace=True means the same AGN can be selected
    # more than once in one bootstrap sample

    bootstrap_sample = clean_data.sample(
        n=len(clean_data),
        replace=True
    )

    # Calculate the Pearson correlation coefficient
    # for this bootstrap sample

    bootstrap_correlation, _ = stats.pearsonr(
        bootstrap_sample["log_bh_mass"],
        bootstrap_sample["log_lbol"]
    )

    # Store the correlation coefficient

    bootstrap_correlations.append(
        bootstrap_correlation
    )

# Calculate the standard deviation of the Pearson
# correlation coefficients from the bootstrap samples

correlation_uncertainty = np.std(
    bootstrap_correlations,
    ddof=1
)

# --------------------------------------------------------
# Calculate the significance of the correlation
# --------------------------------------------------------

# Calculate how many statistical uncertainties the
# Pearson correlation coefficient is away from zero

significance = abs(correlation) / correlation_uncertainty

# --------------------------------------------------------
# Print the results
# --------------------------------------------------------

print("Pearson correlation coefficient =", correlation)
print("Statistical uncertainty =", correlation_uncertainty)
print("Significance =", significance, "sigma")