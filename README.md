
# Supermassive Black Hole Mass and AGN Luminosity Analysis

This project investigates the relationship between the mass of supermassive black holes and the bolometric luminosity of their active galactic nuclei (AGNs), using a publicly available astronomical dataset.

## 🔬 Research Question
**Is the mass of a supermassive black hole related to the luminosity of its active galactic nucleus?**

## Dataset

**Name:** XMM-COSMOS Catalog of X-Ray Selected Type 1 AGN
- **Original source:** [NASA HEASARC](https://heasarc.gsfc.nasa.gov/db-perl/W3Browse/w3table.pl?tablehead=name%3Dxmmcosmagn&Action=More+Options)
- **Original dataset:** 545 AGNs
- **File used:** `black_hole_data.txt`
- **Final dataset:** 150 AGNs after removing missing values from either or both variables

## Code Workflow
- Loads and cleans the dataset.
- Plots a histogram of black-hole masses.
- Creates a scatter plot of black-hole mass versus AGN bolometric luminosity.
- Calculates the Pearson correlation coefficient.
- Estimates the statistical uncertainty using bootstrapping (10,000 samples with replacement).
- Calculates the ratio between the correlation coefficient and its statistical uncertainty.

  
## Output
The script generates two figures:
- `black_hole_mass_distribution.png`
- `black_hole_mass_vs_luminosity.png`

It also prints the following results:

- **Original number of AGNs:** 545
- **Number of AGNs used:** 150
- **Pearson correlation coefficient:** 0.390
- **Bootstrap statistical uncertainty:** 0.0781
- **Significance:** 5.00

## How to run the code 


### Requirements
- Python 3
- NumPy
- pandas
- Matplotlib
- SciPy

### Installation
Install the required libraries using:

```bash
python3 -m pip install numpy pandas matplotlib scipy
```




