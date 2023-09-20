import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

tickers = ["AAPL", "MSFT", "GOOGL","BAJAJ-AUTO.ns"]

plt.figure(figsize=(15, 8))

for ticker in tickers:
    try:
        # Initialize the yfinance Ticker object
        stock = yf.Ticker(ticker)
        
        hist_data = stock.history(period="10y")
        
        if hist_data.empty:
            print(f"No historical data found for ticker '{ticker}'.")
            continue

        if not isinstance(hist_data.index, pd.DatetimeIndex):
            print(f"Data for ticker '{ticker}' does not have a DatetimeIndex.")
            continue
        
        country = stock.info.get("country", "Unknown")
        
        hist_data_resampled = hist_data['Close'].resample('Y').last()
        
        plt.plot(hist_data_resampled.index, hist_data_resampled, label=f"{ticker} ({country}) Closing Price")
        
        for i in range(1, len(hist_data_resampled)):
            y1, y2 = hist_data_resampled.iloc[i-1], hist_data_resampled.iloc[i]
            x1, x2 = hist_data_resampled.index[i-1], hist_data_resampled.index[i]
            price_diff = (y2 - y1)/y1 *100
            annotation = f"{price_diff:+.2f}"
            mid_point_x = x1 + (x2 - x1) / 2
            mid_point_y = y1 + (y2 - y1) / 2
            plt.annotate(annotation, (mid_point_x, mid_point_y), textcoords="offset points", xytext=(0,10), ha='center')
            
    except KeyError:
        print(f"Ticker symbol '{ticker}' not found.")

plt.title("Yearly Price Changes in Stock Prices")
plt.xlabel("Year")
plt.ylabel("Closing Price in $")
plt.legend()
plt.grid(True)


plt.show()
