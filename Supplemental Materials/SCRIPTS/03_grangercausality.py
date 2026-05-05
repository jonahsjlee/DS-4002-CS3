
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.vector_ar.var_model import VAR
from statsmodels.tsa.stattools import grangercausalitytests

# load dataset
df = pd.read_csv('/content/DS-4002_Group5_Project2/DATA/P2_Data_With_LogDiff.csv')

def splitter(data_df):
  # calculates 80% of the data
  end = round(len(data_df)*.8)
  # takes 80% of the data for training
  train_df = data_df.iloc[:end]
  # 20% of the data for testing
  test_df = data_df.iloc[end:]
  return train_df, test_df

train_df, test_df = splitter(df[['avg_hourly_wage_log_diff', 'USNHPI_log_diff']])

# we want to select the optimal VAR order p by computing different multivariate information criterion
def optimal_order(train_df):
  # initializing lists to store values of each of the information criterion values
  aic, bic, fpe, hqic = [], [], [], []

  # define the model
  model = VAR(train_df)

  # set different values
  p = np.arange(1, 30)

  # loop through different values
  for i in p:
    # produces and appends results to the lists we set up earlier
    result = model.fit(i)
    aic.append(result.aic)
    bic.append(result.bic)
    fpe.append(result.fpe)
    hqic.append(result.hqic)

  # create a table of results
  results_df = pd.DataFrame({'AIC': aic,
                                 'BIC': bic,
                                 'FPE': fpe,
                                 'HQIC': hqic},
                                index=p)

  # set up plots and create title
  fig, ax = plt.subplots(1, 4, figsize = (15,3), sharex=True)
  results_df.plot(subplots=True, ax=ax, marker='o')
  plt.suptitle('VAR Order p by Different Multivariate Information Criterion')
  plt.tight_layout()
  plt.show()

  # show the best order values based on each information criterion
  print(results_df.idxmin(axis=0), '\n')

# call function
optimal_order(train_df)

# fit VAR model with chosen order (p=2)
p=2
model = VAR(train_df)
var_model = model.fit(p)

# testing variables for Granger Causality
def granger_causation_matrix(data, var, p):
  # creating empty matrix to store values
  dataf = pd.DataFrame(np.zeros((len(var), len(var))), columns=var, index=var)

  # iterating through each element in the matrix
  for c in dataf.columns:
    for r in dataf.index:
      # run test
      test_res = grangercausalitytests(data[[r, c]], p, verbose=False)

      # extract p-values
      p_values = [test_res[i+1][0]['ssr_chi2test'][1] for i in range(p)]

      # take the minimum p-value because any significant result indicates Granger-causality
      min_p_value = np.min(p_values)
      dataf.loc[r,c] = min_p_value

  # labelling columns and rows of the matrix
  dataf.columns = [v + '_x' for v in var]
  dataf.index = [v + '_y' for v in var]

  return dataf

print('Granger Causation Matrix for p=2: \n', granger_causation_matrix(train_df, train_df.columns, p), '\n')

# testing p=14
p=14
model = VAR(train_df)
var_model = model.fit(p)

print('Granger Causation Matrix for p=14: \n', granger_causation_matrix(train_df, train_df.columns, p), '\n')
