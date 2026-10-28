import sys
from contextlib import redirect_stdout

import numpy as np
import pandas as pd

from matrix_operations_utility import print_precision, print_return_analysis


CSV_FILE = "sample data\indices-july2016.csv"
OUTPUT_FILE = "question11_output.txt"
INDEX_COLUMNS = ["BAC", "BNS", "C", "GS", "JPM", "MS", "TD", "USB", "WFC"]

def calculate_returns(prices):
    return {
        "log": np.log(prices).diff().dropna(),
        "percent": prices.pct_change().dropna(),
    }


def main():
    data = pd.read_csv(CSV_FILE, parse_dates=["Date"], index_col="Date")
    data = data.sort_index()
    prices = data.loc[:, INDEX_COLUMNS]

    daily_returns = calculate_returns(prices)
    weekly_prices = prices.resample("W").last()
    monthly_prices = prices.resample("ME").last()
    weekly_returns = calculate_returns(weekly_prices)
    monthly_returns = calculate_returns(monthly_prices)

    log_returns = daily_returns["log"]
    pct_returns = daily_returns["percent"]

    return_columns = pd.concat(
        [
            log_returns.add_suffix("_LOG_DELTA"),
            pct_returns.add_suffix("_PCT_DELTA"),
        ],
        axis=1,
    )
    print("\n-------------------------------DAILY LOG RETURNS / DAILY PERCENT RETURNS DATAFRAME------------------------------------------\n")
    print_precision(data.join(return_columns))

    print_return_analysis("TIME SERIES MATRIX FOR DAILY LOG RETURNS", log_returns)
    print_return_analysis("TIME SERIES MATRIX FOR DAILY RETURNS PERCENT", pct_returns)
    print_return_analysis("TIME SERIES MATRIX FOR WEEKLY LOG RETURNS", weekly_returns["log"])
    print_return_analysis("TIME SERIES MATRIX FOR WEEKLY RETURNS PERCENT", weekly_returns["percent"])
    print_return_analysis("TIME SERIES MATRIX FOR MONTHLY LOG RETURNS", monthly_returns["log"])
    print_return_analysis("TIME SERIES MATRIX FOR MONTHLY RETURNS PERCENT", monthly_returns["percent"])


if __name__ == "__main__":
    main()