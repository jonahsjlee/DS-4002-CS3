# Granger Causality Analysis of Average Hourly Wages and the U.S. Housing Price Index
- DS 4002 Group 5, Project 2
- Group Leader: Jonathan Sutkus
- Group Members: Jonathan Sutkus, Siwen Liao, Jonah Lee
- Mar 19, 2026

## Repository Contents
The goal of this project is to perform a Granger Causality analysis to determine whether average hourly wage in the United States can be a reliable predictor of the U.S. National Home Price Index (USNHPI). The DS-4002_Group5_Project2 repository contains the DATA folder (includes our two original and our final dataset of interest as well as more information about the data located in the data appendix), the SCRIPTS folder (includes code for preprocessing/cleaning the dataset, testing the stationarity of the data, and running the Granger Causaility to show predictive power), the OUTPUTS folder (contains screenshots or PDFs of our results from the lag plots, stationarity tests, and Granger Causality), and the LICENSE.md and README.md files.

## Section 1: Software and Platform

### Software/Platform
This project was developed and run using: 
- Google Colab/Jupyter Notebook on a Mac

### Packages
The following Python packages are required:

- pandas
- numpy
- matplotlib.pyplot
- lag_plot (from pandas.plotting)
- kpss, adfuller, grangercausalitytests (from statsmodels.tsa.stattools_
- VAR (from statsmodels.tsa.vector_ar.var_model)

## Section 2: Documentation Map
```text
DS-4002_Group5_Project1/
│
├── DATA/
│ ├── Avg_Hourly_Wage_data.csv
│ ├── P2_Data.csv
│ ├── P2_Data_Appendix.csv
│ ├── P2_Data_With_LogDiff.csv
│ ├── USNHPI_data.csv
│
├── OUTPUT/
│ ├── choosing_p_forVARmodel_values.png
│ ├── granger_causation_matrix_p=14.png
│ ├── granger_causation_matrix_p=2.png
│ ├── lagplots_avghourlywage_USNHPI.png
│ ├── lagplots_stationaritytests_differences.pdf
│ ├── lagplots_stationaritytests_logdifferences.pdf
│
├── SCRIPTS/
│ ├── 01_preprocess.py
│ ├── 02_checkstationarity.py
│ ├── 03_grangercausality.py
│
├── LICENSE
└── README.md
```

### Folder Descriptions
- **DATA**: Contains two original datasets and our final datatset alongside the data appendix that includes more information about our variables and observations.
  - Original datasets of 238 months (or observations) ranging from March of 2006 to December of 2025.
  - Cleaned dataset after preprocessing.
  - Our Data Appendix describes our unit of observation as well as all of the key variables we will be utilizing in our analysis alongside some exploratory visuals associated with some of our variables of interest. 
- **SCRIPTS**: Contains python scripts for data preprocessing/cleaning, lag plots and stationarity tests, and the Granger Causality analysis.
- **OUTPUT**: Contains png files of the lag plots for avg_hourly_wage and USNHPI, results from the multivariate information criterion on selecting the order p for the VAR model, and the granger causation matrices for VAR models with order p=2 and p=14. Contains PDFs of the lag plots and stationarity tests for avg_hourly_wage_differences, USNHPI_differences, avg_hourly_wage_log_differences, and USNHPI_log_differences. 
- **LICENSE**: MIT license was selected based on recommendation from the DS 4002 Ml3 Rubric.
- **README.md**: Instructions, documentation, and respository overview. 

## Section 3: Instructions for Reproduction

- **Step 1**: Clone the repository. Cloning creates a complete local copy of the repository, including all files and branches. Make sure that you can see the DATA, OUTPUT, and SCRIPTS folders. Confirm that the Avg_Hourly_Wage_data.csv and USNHPI_data.csv exist in the DATA folder. 
- **Step 2**: In Google Colab, or the desired platform of choice, run the 01_preprocess.py script. The 01_preprocess.py script merges the Avg_Hourly_Wage_data.csv and USNHPI_data.csv dataset together so we can analyze both variables at once with respect to time. The 01_preprocess.py script produces a new dataset, P2_Data.csv. Upload and save P2_Data.csv to the DATA folder. 
- **Step 3**: After preprocessing the data, run the 02_checkstationarity.py script.
  - This script will:
    - Read the P2_Data.csv dataset
    - Verify all dates are in the correct format
    - Verify time intervals are constant
    - Check for and remove missing values
    - Create lag plots to check if the data is stationary
    - Use the KPSS and ADF tests to verify stationarity
    - Create two new columns in the dataset: avg_hourly_wage_log_diff and USNHPI_log_diff
    - Save the new dataset to the repository as P2_Data_With_LogDiff

  - The output should include:
    - The time intervals and NA values for P2_Data.csv
    - The lag plots for avg_hourly_wage and USNHPI
    - The lag plots for avg_hourly_wage_diff and USNHPI_diff
    - The results from the KPSS and ADF tests for avg_hourly_wage_diff and USNHPI_diff
    - The lag plots for avg_hourly_wage_log_diff and USNHPI_log_diff
    - The results from the KPSS and ADF tests for avg_hourly_wage_log_diff and USNHPI_log_diff
   
  - Some notes for Step 3:
    - You will see that the original variables, avg_hourly_wage and USNHPI, show a strong trend. This signals non-stationarity. This is why we then test the differences, avg_hourly_wage_diff and USNHPI_diff. From the kpss and adf tests, we can see that the results still show non-stationarity. As a result, we take a logarithmic transformation of avg_hourly_wage and USNHPI and compute the differences to get avg_hourly_wage_log_diff and USNHPI_log_diff. Functions are created for lag plots and the KPSS and ADF tests to make this process easier.
   
- **Step 4**: Finally, we can perform the Granger Causality test. To do this, run the 03_grangercausality.py script.
  - This script will:
    - read the P2_Data_With_LogDiff.csv dataset
    - split the dataset in a training set (80%) and a test set (20%)
    - select the VAR order p by computing different multivariate information criterion values (AIC, BIC, FPE, HQIC)
    - fit the VAR model with the chosen order
    - test variables for Granger Causality using the SSR-based chi-squared test
    - output a Granger Causation matrix with p-values from the test
   
  - The output should include:
    - Plots for the VAR order p by different multivariate information criterion
    - The order p results from each multivariate information criterion
    - The Granger Causation matrix for p=2
    - The Granger Causation matrix for p=14

- **Step 5**: Verify your outputs match those in the OUTPUT folder.

## References

- [1] Eric, “Introduction to Granger Causality,” Aptech Systems Blog, Oct. 4, 2021. [Online]. Available: https://www.aptech.com/blog/introduction-to-granger-causality/. [Accessed: Mar. 11, 2026].
- [2] Grewal, A., Hepburn, K. J., Lear, S. A., Adshade, M., & Card, K. G. (2024). The impact of housing prices on residents’ health: A systematic review. BMC Public Health. Retrieved from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10983630/
- [3] Louie, S., Mondragon, J., & Wieland, J. F. (2025). Supply constraints do not explain house price and quantity growth across U.S. cities (Federal Reserve Bank of San Francisco Working Paper No. 2025-06). Federal Reserve Bank of San Francisco. https://www.frbsf.org/wp-content/uploads/wp2025-06.pdf
- [4] PhD Students in Data Science Batch 2023, Asian Institute of Management, “Chapter 4: Granger Causality Test,” Time Series Analysis Handbook, 2020. - [Online]. Available: https://phdinds-aim.github.io/time_series_handbook/04_GrangerCausality/04_GrangerCausality.html. [Accessed: Mar. 9, 2026].
- [5] ScienceDirect. (n.d.). Granger-causality. In ScienceDirect Topics. Elsevier. Retrieved February 25, 2026, from https://www.sciencedirect.com/topics/social-sciences/granger-causality
- [6] U.S. Bureau of Labor Statistics. (n.d.). Average hourly earnings of all employees, total private (CES0500000003). Retrieved March 11, 2026, from FRED, Federal Reserve Bank of St. Louis: https://fred.stlouisfed.org/series/CES0500000003
- [7] U.S. Federal Housing Finance Agency. (n.d.). S&P/Case-Shiller U.S. National Home Price Index (CSUSHPINSA). Retrieved March 11, 2026, from FRED, Federal Reserve Bank of St. Louis: https://fred.stlouisfed.org/series/CSUSHPINSA
