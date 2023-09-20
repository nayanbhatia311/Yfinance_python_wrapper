
# Stock Price Analysis

This script fetches the historical stock prices of given ticker symbols and visualizes the yearly price changes over the past decade.

## Features:

- Fetches stock data using the `yfinance` library.
- Plots the yearly closing price of the stocks.
- Annotates the plot with percentage change in price compared to the previous year.
- Displays the country of the stock alongside its ticker symbol.

## Dependencies:

- `yfinance`
- `matplotlib`
- `pandas`

To install the dependencies, run:
```
pip install yfinance matplotlib pandas
```

## Usage:

1. Clone the repository.
2. Modify the `tickers` list in the script to include the ticker symbols of the stocks you're interested in.
3. Run the script.
4. The plot will display the yearly closing prices of the stocks, along with annotations indicating the percentage change from the previous year.

## Sample Output:

The script fetches data for the following ticker symbols by default: `AAPL`, `MSFT`, `GOOGL`, and `BAJAJ-AUTO.ns`. The output plot will show the yearly closing prices for these stocks over the last decade.

## Error Handling:

The script handles common issues, such as:
- Ticker symbols that are not found.
- Ticker symbols that do not have historical data.
- Ticker symbols whose data does not have a `DatetimeIndex`.

In such cases, appropriate messages are printed to the console.
