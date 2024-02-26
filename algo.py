# import modules
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
  
# initialize parameters
start_date = datetime(2022, 4, 1)
end_date = datetime(2022, 4, 10)

def data_import(*tickers):
    result = []
    for ticker in tickers:
        data = yf.download(ticker)
        result.append(data["Open"])

    return result 

# display

print(data_import("AAPL", "TSLA", "BTC"))

# plt.figure(figsize = (20,10))
# plt.title('Opening Prices for {} and {} from {} to {}'.format(ticker1, ticker2, start_date, end_date))
# plt.plot()

# plt.show()
