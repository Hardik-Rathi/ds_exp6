# Experiment 6 — Statistical Distribution Analysis

**Course:** Data Science  
**Experiment:** 6 — Analyzing and Interpreting Statistical Distributions in Robotic Environments  
**Repository:** https://github.com/Hardik-Rathi/ds_exp6

## Overview
This project analyzes the statistical characteristics of the provided Indian Meteorological Department (IMD) subdivision rainfall dataset. It demonstrates how descriptive statistics and visualizations can be used to understand distributions, variability, skewness, kurtosis, and potential outliers.

> **Dataset note:** The supplied CSV contains rainfall measurements, not direct robotic sensor readings. It is used here as environmental measurement data to demonstrate the statistical methods in Experiment 6.

## Repository contents
- `Experiment_6_Statistical_Distributions.ipynb` — Jupyter Notebook with the analysis and visualizations.
- `Experiment_6_Statistical_Distributions.py` — Python script version of the analysis.
- `Sub_Division_IMD_2017.csv` — dataset used by the notebook/script.

## Analysis performed
- Load and inspect the dataset.
- Select numeric measurement columns for analysis.
- Calculate descriptive statistics such as mean, median, and standard deviation.
- Plot histograms and density curves.
- Calculate skewness and kurtosis.
- Identify potential outliers using the interquartile range (IQR) method.
- Compare observed data with a fitted normal distribution where appropriate.
- Interpret distribution characteristics and their relevance to data analysis.

## Requirements
- Python 3.9 or newer
- pandas
- NumPy
- Matplotlib
- SciPy
- Jupyter Notebook (for the `.ipynb` file)

Install the required libraries:

```bash
pip install pandas numpy matplotlib scipy jupyter
```

## How to run

### Option 1: Jupyter Notebook
1. Download or clone this repository.
2. Keep the CSV file in the same folder as the notebook.
3. Open a terminal in the project folder and run:

   ```bash
   jupyter notebook
   ```

4. Open `Experiment_6_Statistical_Distributions.ipynb` and run the cells from top to bottom.

### Option 2: Python script
Keep the CSV file in the same folder as the script, then run:

```bash
python Experiment_6_Statistical_Distributions.py
```

If the CSV filename in the script differs from the file in your repository, update the filename in the script to match exactly.

## Interpreting the results
Histograms and density plots show the shape of the data distribution. Mean, median and standard deviation summarize its centre and spread, while skewness and kurtosis describe asymmetry and tail behaviour. IQR-based flags identify possible outliers; these are candidates for review, not automatically errors.

## Author
Hardik Rathi

## Repository
[Open the GitHub repository](https://github.com/Hardik-Rathi/ds_exp6)
