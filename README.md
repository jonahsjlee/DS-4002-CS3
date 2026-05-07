# CS3 GrangerCausality
A DS 4002 Case Study by Jonah Lee

## Overview
The question at the center of this case study is whether average hourly wages in the U.S. can predict where home prices are headed. Using monthly time series data from the Federal Reserve Bank of St. Louis, you will apply Granger causality to determine whether wage data improves the ability to forecast the U.S. National Home Price Index.

This case study is targeted at second-year UVA students with some Python experience. You do not need prior experience with time series analysis or econometrics. Everything you need to get started is in this repository.

## Hook and Rubric
The hook document and rubric are both in the root of this repository:

* `CS3_Hook_Document.pdf` — Read this first. It frames the problem and your mission.
* `CS3_Rubric.pdf` — Read this second. It describes what you need to produce and how you will be assessed.

I would recommend coming back to both of these as you work through the analysis, not just at the beginning.

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
├── CS3_Hook_Document.pdf         # Hook document
├── CS3_Rubric.pdf                # Rubric
├── README.md                     # This file
├── LICENSE.md                    # License terms
├── REFERENCES.md                 # All references
│
├── DATA/
│   ├── P2_Data.csv
│   ├── USNHPI_data.csv
│   ├── Avg_Hourly_Wage_data.csv
│   ├── P2_Data_With_LogDiff.csv
│   ├── P2_Data_Appendix.pdf
│
├── OUTPUT/
│   ├── time_series_plot.png
│   ├── correlation_matrix.png
│   ├── monthly_wage_diff.png
│   ├── monthly_hpi_diff.png
│   ├── wage_vs_hpi_linear.png
│   └── granger_causation_matrix.png
│
└── Materials/
    ├── intro_to_granger_causality.pdf
    └── granger_causality_handbook_ch4.pdf
```

## Data
Both datasets can be accessed at the Federal Reserve Bank of St. Louis and are small enough to be included in the repository. Please download both CSV files and place them in the DATA directory.

The REFERENCES.md file contains the complete source URLs.

## How to Reproduce Results

1. Download both FRED datasets and place the CSVs in the `DATA/` folder.
2. Install the required packages listed above.
3. Clean and/or merge the data.
4. Check your figures against the plots in `OUTPUT/` to verify.
5. The Granger causation matrix from `05_granger_causality.py` is the main result you are working toward.

## Reference Materials
Two articles are included in `Materials/` to help you get up to speed on Granger causality before writing any code. If you are new to the method, start with the Aptech blog post since it is more accessible. The handbook chapter gets more technical and is worth reading once you have the basic idea down.

All full citations are in `REFERENCES.md`.
