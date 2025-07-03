# Root Mean Square of Daily Price Movement Differences: S&P 500 and NASDAQ

## Objective

The objective of this assignment is to retrieve the historical price data for the S&P 500 (^GSPC) and NASDAQ (^IXIC) from Yahoo Finance, join this data by date, and calculate the root mean square difference in their daily price movements.

## Approach

1.  **Data Acquisition:** Use the `yfinance` library to fetch the historical 'Close' prices for the S&P 500 and NASDAQ indexes for the year to date (`5y`) with a daily interval (`1d`).
2.  **Data Preparation:** Merge the retrieved S&P 500 and NASDAQ dataframes based on their 'Date' index, keeping only the 'Close' prices. Rename the columns for clarity.
3.  **Calculate Daily Price Movement:** Compute the daily difference in closing prices for both indexes using the `.diff()` method.
4.  **Calculate Root Mean Square Difference (RMSD):** Implement a function to calculate the RMSD between the daily price movements of the S&P 500 and NASDAQ. The RMSD will quantify the typical magnitude of the difference between the daily price changes of the two indexes.
5.  **Output:** Print the calculated RMSD result, indicating the number of trading days analyzed.

## Installation on your own environment

To run this notebook, you need to install the following Python packages:

- In your terminal line run `pip install pandas`. See [pandas documentation](https://pandas.pydata.org/docs/getting_started/index.html#getting-started).
- In your terminal line run `pip install yfinance`. See [yfinance documentation](https://ranaroussi.github.io/yfinance/index.html).
- Or try in your terminal `pip install -r requirements.txt` to install dependencies.
