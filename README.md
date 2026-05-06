# CS3 GrangerCausality
A DS 4002 Case Study by Jonah Lee

## Overview
Can average hourly wages in the United States predict where home prices are headed? That is the question at the center of this case study. Using monthly time series data from the Federal Reserve Bank of St. Louis (FRED) — spanning nearly two decades of economic history including the 2008 financial crisis and the COVID-19 pandemic — you will apply Granger causality to determine whether wage data improves our ability to forecast the U.S. National Home Price Index (USNHPI).

This case study is targeted at second-year UVA students with some Python experience. You do not need prior experience with time series analysis or econometrics. Everything you need to get started is in this repository.

## Hook and Rubric
The hook document and rubric for this case study are located in the root of this repository:

* `CS3_Hook_Document.pdf` - Read this first. It frames the problem and your mission.
* `CS3_Rubric.pdf` - Read this second. It describes exactly what you need to produce and how you will be graded.

Both documents should be referenced continuously throughout your work.

## Software and Platform

* Language: Python 3.12
* Platform: Google Colab (recommended) or any machine with a standard Python environment
* Packages required:
  * `pandas`
  * `numpy`
  * `matplotlib`
  * `statsmodels`
  * `scipy`

Install all packages with:

```
pip install pandas numpy matplotlib statsmodels scipy
```

## Repository Map

```
CS3_GrangerCausality/
├── CS3_Hook_Document.pdf         # Hook document — read first
├── CS3_Rubric.pdf                # Rubric — your guide to success
├── README.md                     # This file
├── LICENSE.md                    # License terms
├── REFERENCES.md                 # All references in IEEE format
│
├── DATA/
│   ├── raw_wages.csv             # Raw average hourly earnings data from FRED
│   ├── raw_hpi.csv               # Raw U.S. National Home Price Index data from FRED
│   └── merged_cleaned.csv        # Cleaned and merged dataset ready for analysis
│
├── SCRIPTS/
│   ├── 01_data_merge_clean.py    # Download instructions, merging, and cleaning
│   ├── 02_eda.py                 # Exploratory data analysis and visualizations
│   ├── 03_stationarity_tests.py  # ADF and KPSS stationarity tests
│   ├── 04_var_order_selection.py # VAR model lag order selection (AIC, BIC, HQIC, FPE)
│   └── 05_granger_causality.py   # Granger causality test and results
│
├── OUTPUT/
│   ├── time_series_plot.png      # Wages and USNHPI over time with key periods marked
│   ├── correlation_matrix.png    # Correlation matrix of key variables
│   ├── monthly_wage_diff.png     # Average hourly wage difference by month
│   ├── monthly_hpi_diff.png      # Average USNHPI difference by month
│   ├── wage_vs_hpi_linear.png    # Linear relationship between wage and USNHPI
│   └── granger_causation_matrix.png  # Final Granger causation matrix with p-values
│
└── Materials/                    # Supplemental readings to get you started
    ├── intro_to_granger_causality.pdf     # Blog post: Aptech Systems explainer
    └── granger_causality_handbook_ch4.pdf # Technical: AIM Time Series Handbook, Ch. 4
```

## Data
Both datasets are freely available from the Federal Reserve Bank of St. Louis (FRED) and are small enough to include directly in this repository.

* **Average Hourly Earnings of All Employees, Total Private** — Series ID: `CES0500000003`
  Download from: https://fred.stlouisfed.org/series/CES0500000003
* **S&P/Case-Shiller U.S. National Home Price Index** — Series ID: `CSUSHPINSA`
  Download from: https://fred.stlouisfed.org/series/CSUSHPINSA

Download both CSVs and place them in the `DATA/` folder. Script `01_data_merge_clean.py` will handle the rest.

Dataset summary:

* 238 monthly observations from March 2006 through December 2025
* 6 columns after merging and cleaning, including lag and log-differenced variables
* Key variables: `avg_hourly_wage`, `USNHPI`, `avg_hourly_wage_lag`, `avg_hourly_wage_log_diff`, `USNHPI_log_diff`
* Notable periods covered: 2008 financial crisis, COVID-19 pandemic, post-pandemic housing surge

## How to Reproduce Results

1. Download both FRED datasets using the links above and place the CSVs in the `DATA/` folder.
2. Install the required packages listed above.
3. Run the scripts in `SCRIPTS/` in order, starting with `01_data_merge_clean.py`. Each script builds on the output of the one before it.
4. Review your output figures against the plots in the `OUTPUT/` folder to verify your results match.
5. The final Granger causation matrix produced by `05_granger_causality.py` is the central result of the analysis.

Note: All scripts were developed and tested in Python 3.12. Runtime is minimal — none of the scripts should take more than a minute to run on a standard laptop.

## Reference Materials
Two reference articles are provided in the `Materials/` folder to help you understand Granger causality before diving into the code. Start with the Aptech blog post if you are new to the method, then work through the handbook chapter for a more technical treatment.

All full citations are in `REFERENCES.md`.
