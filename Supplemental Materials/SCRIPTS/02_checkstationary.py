
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot
from statsmodels.tsa.stattools import kpss, adfuller

# importing dataset
df = pd.read_csv('/content/DS-4002_Group5_Project2/DATA/P2_Data.csv')

# verifying all dates are in the correct format
df['date'] = pd.to_datetime(df['date'])

# verifying constant time intervals
df['date_diff'] = df['date'].diff()
print('time intervals: \n', df['date_diff'].value_counts(), '\n')

# checking for missing values
print('NA values: \n', df.isna().sum(), '\n')

# removing rows with missing values
df = df.dropna()

# creating lag plot function to check if the data is stationary
def lag_plots(data_df, column1, column2):
    # setting layout of plots side-by-side
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    # first lag plot with first variable
    lag_plot(data_df[column1], ax=ax1)
    ax1.set_title(data_df[column1]);

    # second lag plot with second variable
    lag_plot(data_df[column2], ax=ax2)
    ax2.set_title(data_df[column2]);

    # labelling axes
    ax1.set_ylabel('$y_{t+1}$');
    ax1.set_xlabel('$y_t$');
    ax2.set_ylabel('$y_{t+1}$');
    ax2.set_xlabel('$y_t$');

    # setting title and printing plots
    plt.suptitle(f'Lag Plots for {column1} and {column2}')
    plt.tight_layout()
    plt.show()

# showing lag plots for avg_hourly_wage and USNHPI
lag_plots(df, 'avg_hourly_wage', 'USNHPI')

# avg_hourly_wage and USNHPI lag plots showed a trend in the data (characteristic of non-stationary data)

# showing lag plots for avg_hourly_wage_diff and USNHPI_diff
lag_plots(df, 'avg_hourly_wage_diff', 'USNHPI_diff')

# using the KPSS and ADF tests to verify stationarity
def kpss_test(data_df):
  # storing test statistics and p-values
  test_stat, p = [], []
  # storing critical values
  cv_1, cv_25, cv_5, cv_10 = [], [], [], []
  
  # iterating through each column
  for c in data_df.columns:
    # perform kpss test
    kpss_res = kpss(data_df[c]) 
    # append test statistic
    test_stat.append(kpss_res[0])
    # append p-value
    p.append(kpss_res[1])
    # append critical values
    cv_1.append(kpss_res[3]['1%'])
    cv_25.append(kpss_res[3]['2.5%'])
    cv_5.append(kpss_res[3]['5%'])
    cv_10.append(kpss_res[3]['10%'])
  
  # create dataframe to display results
  kpss_results_df = pd.DataFrame({'Test Statistic': test_stat,
                              'P-value': p, 
                              'Critical Value 1%': cv_1,
                              'Critical Value 2.5%': cv_25,
                              'Critical Value 5%': cv_5,
                              'Critical Value 10%': cv_10},
                             index=data_df.columns).T 
  return kpss_results_df

def adf_test(data_df):
  # storing test statistics and p-values
  test_stat, p = [], []
  # storing critical values
  cv_1, cv_5, cv_10 = [], [], []

  # iterating through each column
  for c in data_df.columns:
    # perform adf test
    adf_res = adfuller(data_df[c])
    # append test statistic
    test_stat.append(adf_res[0])
    # append p-value
    p.append(adf_res[1])
    # append critical values
    cv_1.append(adf_res[4]['1%'])
    cv_5.append(adf_res[4]['5%'])
    cv_10.append(adf_res[4]['10%'])
  
  # create dataframe to display results
  adf_results_df = pd.DataFrame({'Test Statistic': test_stat,
                              'P-value': p, 
                              'Critical Value 1%': cv_1,
                              'Critical Value 5%': cv_5,
                              'Critical Value 10%': cv_10},
                             index=data_df.columns).T 
  return adf_results_df

print('kpss test results: \n', kpss_test(df[['avg_hourly_wage_diff', 'USNHPI_diff']]), '\n')
print('adf test results: \n', adf_test(df[['avg_hourly_wage_diff', 'USNHPI_diff']]), '\n')

# taking the logarithmic differences of the original variables
df['avg_hourly_wage_log_diff'] = np.log(df['avg_hourly_wage']).diff()
df['USNHPI_log_diff'] = np.log(df['USNHPI']).diff()
# removing missing values
df = df.dropna()

# showing lag plots for avg_hourly_wage_log_diff and USNHPI_log_diff
lag_plots(df, 'avg_hourly_wage_log_diff', 'USNHPI_log_diff')

# using the KPSS and ADF tests to verify stationarity
print('kpss test results: \n', kpss_test(df[['avg_hourly_wage_log_diff', 'USNHPI_log_diff']]), '\n')
print('adf test results: \n', adf_test(df[['avg_hourly_wage_log_diff', 'USNHPI_log_diff']]), '\n')

# saving updated dataset
df.to_csv('/content/DS-4002_Group5_Project2/DATA/P2_Data_With_LogDiff.csv')
