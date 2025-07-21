# This script calculates the root mean square difference (RMSD) between the daily price movements of the S&P 500 and Nasdaq indexes over a specified period.
# It uses the Yahoo Finance API to fetch historical data and pandas for data manipulation.

# Import libraries
import yfinance as yf # Yahoo Finance API
import pandas as pd   # Data Wrangling

# Import ticker info
sp500 = yf.Ticker('^GSPC')
nasdaq = yf.Ticker('^IXIC')


# Set parameters & collect data
period = '5y' # Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
interval = '1d'
sp500_data  = sp500.history(period=period, interval=interval, auto_adjust=True, rounding=True)
nasdaq_data = nasdaq.history(period=period, interval=interval, auto_adjust=True, rounding=True)

# Include only closing prices and merge data
us_indexes = pd.merge(left=sp500_data[['Close']] , right=nasdaq_data[['Close']], on='Date', how='inner')
us_indexes.columns = ['sp500_adjclose', 'nasdaq_adjclose']

# Calculate the price movement
us_indexes['sp500_delta'] = us_indexes['sp500_adjclose'].diff()
us_indexes['nasdaq_delta'] = us_indexes['nasdaq_adjclose'].diff()

# print(us_indexes) # print dataframe

# Define RMS difference function
def root_mean_square_difference(column1, column2) -> float:
  """
  Calculates the root mean square difference between two columns.

  Args:
    column1: The first array or pandas Series.
    column2: The second array or pandas Series.

  Returns:
    The root mean square difference as a float.
  """

  n = len(column1[1:]) # excludes NaN day
  squared_diff = (column1[1:] - column2[1:]) ** 2
  mean_squared_diff = 1 / n * sum(squared_diff)
  rmse = mean_squared_diff ** 0.5
  return round(rmse, 2)

rmse_result = root_mean_square_difference(us_indexes['sp500_delta'], us_indexes['nasdaq_delta'])

print(f"Root Mean Square Difference between S&P 500 and NASDAQ daily price movements over {len(us_indexes)} tranding days: {rmse_result}")