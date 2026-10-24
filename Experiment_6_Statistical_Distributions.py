# Experiment No. 6: Analyzing and Interpreting Statistical Distributions
# Dataset: Sub-Division IMD rainfall data (monthly and seasonal rainfall)
# Note: This dataset is rainfall data, not direct robotic sensor readings.
# Rainfall is treated as environmental measurement data for the statistical analysis.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# If running locally, keep the CSV in the same folder as this notebook.
file_path = "Sub_Division_IMD_2017(1).csv"
df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
display(df.head())

# Choose a subdivision to analyze. Change this value if desired.
subdivision = "Madhya Maharashtra"
subset = df[df["SUBDIVISION"] == subdivision].copy()

if subset.empty:
    subdivision = df["SUBDIVISION"].dropna().iloc[0]
    subset = df[df["SUBDIVISION"] == subdivision].copy()
    print("Requested subdivision not found; using:", subdivision)
else:
    print("Analyzing subdivision:", subdivision)

# Select annual and monthly rainfall attributes.
variables = ["ANNUAL", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
available_variables = [col for col in variables if col in subset.columns]
data = subset[available_variables].apply(pd.to_numeric, errors="coerce")

# Basic statistical summary.
summary = pd.DataFrame({
    "Mean": data.mean(),
    "Median": data.median(),
    "Standard Deviation": data.std(),
    "Variance": data.var(),
    "Skewness": data.skew(),
    "Kurtosis (excess)": data.kurtosis(),
    "Minimum": data.min(),
    "Maximum": data.max(),
    "Missing Values": data.isna().sum()
})
display(summary.round(3))

# Histogram for annual rainfall.
annual = data["ANNUAL"].dropna()
plt.figure(figsize=(8, 5))
plt.hist(annual, bins=15, density=True, alpha=0.7, edgecolor="black", label="Observed annual rainfall")
x = np.linspace(annual.min(), annual.max(), 300)
mu, sigma = stats.norm.fit(annual)
plt.plot(x, stats.norm.pdf(x, mu, sigma), linewidth=2, label="Fitted normal distribution")
plt.title(f"Annual Rainfall Distribution — {subdivision}")
plt.xlabel("Annual rainfall (mm)")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()

# Density plots for selected variables.
plt.figure(figsize=(9, 5))
for col in ["ANNUAL", "JJAS", "MAM", "OND"]:
    if col in subset.columns:
        values = pd.to_numeric(subset[col], errors="coerce").dropna()
        if len(values) > 1 and values.nunique() > 1:
            values.plot(kind="kde", label=col)
plt.title(f"Rainfall Density Curves — {subdivision}")
plt.xlabel("Rainfall (mm)")
plt.ylabel("Density")
plt.legend()
plt.tight_layout()
plt.show()

# Boxplot and IQR-based potential outlier detection for annual rainfall.
q1, q3 = annual.quantile([0.25, 0.75])
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = annual[(annual < lower_bound) | (annual > upper_bound)]

plt.figure(figsize=(8, 3.5))
plt.boxplot(annual, vert=False)
plt.title(f"Annual Rainfall Boxplot — {subdivision}")
plt.xlabel("Annual rainfall (mm)")
plt.tight_layout()
plt.show()

print(f"Potential outliers using the 1.5×IQR rule: {len(outliers)}")
display(pd.DataFrame({"Year": subset.loc[outliers.index, "YEAR"], "Annual rainfall (mm)": outliers}).reset_index(drop=True))

# Compare annual rainfall with a fitted normal distribution using the Kolmogorov–Smirnov test.
# The test is a rough diagnostic because the normal parameters are estimated from the same sample.
if len(annual) >= 8 and annual.std(ddof=1) > 0:
    ks_stat, ks_pvalue = stats.kstest(annual, "norm", args=(mu, sigma))
    print(f"Fitted normal distribution: mean={mu:.2f} mm, std={sigma:.2f} mm")
    print(f"KS statistic={ks_stat:.4f}, p-value={ks_pvalue:.4f}")
else:
    print("Not enough non-constant annual rainfall observations for the normality diagnostic.")

# Interpretation helper.
skew = annual.skew()
if skew > 0.5:
    skew_text = "positively skewed (a longer right tail)"
elif skew < -0.5:
    skew_text = "negatively skewed (a longer left tail)"
else:
    skew_text = "approximately symmetric by the skewness measure"

print("\\nInterpretation:")
print(f"Annual rainfall for {subdivision} is {skew_text}.")
print(f"Mean = {annual.mean():.2f} mm; median = {annual.median():.2f} mm; standard deviation = {annual.std():.2f} mm.")
print("Large standard deviation indicates substantial year-to-year variation.")
print("Potential outliers are unusual values under the IQR rule; they are not automatically errors.")
print("In a robotics context, the same workflow can be applied to real sensor measurements such as range, temperature, or IMU readings.")
