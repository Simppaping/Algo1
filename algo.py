# import modules
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import dearpygui.dearpygui as dpg

# initialize parameters
start_date = datetime(2022, 4, 1)
end_date = datetime(2022, 4, 10)


def data_import(*tickers):
    dates = []
    opens = []
    closes = []
    highs = []
    lows = []
    for ticker in tickers:
        data = yf.download(ticker)
        epoch = [date.timestamp() for date in data.index]
        dates.append(epoch)
        opens.append(data["Open"])
        closes.append(data["Close"])
        highs.append(data["High"])
        lows.append(data["Low"])
    
    return dates, opens, highs, lows, closes

ticker = "GOOGL"

dates = data_import(ticker)
opens = data_import(ticker)
highs = data_import(ticker)
lows = data_import(ticker)
closes = data_import(ticker)
print(data_import("AAPL"))
# display
dpg.create_context()

with dpg.window(label="Tutorial"):
    # create plot
    with dpg.plot(label="Candle Series", height=400, width=-1):
        dpg.add_plot_legend()
        xaxis = dpg.add_plot_axis(dpg.mvXAxis, label="Day", time=True)
        with dpg.plot_axis(dpg.mvYAxis, label="USD"):
            dpg.add_candle_series(dates, opens, closes, lows, highs, label="GOOGL", time_unit=dpg.mvTimeUnit_Day)
            dpg.fit_axis_data(dpg.top_container_stack())
        dpg.fit_axis_data(xaxis)

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

print(data_import("AAPL"))

# plt.figure(figsize = (20,10))
# plt.title('Opening Prices for {} and {} from {} to {}'.format(ticker1, ticker2, start_date, end_date))
# plt.plot()

# plt.show()
