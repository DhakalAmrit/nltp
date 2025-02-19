import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price app

shown are the stock closing price an volume of Google!

""")

# https://medium.com/@kasperjuunge/yfinance-10-ways-to-get-stock-data-with-python-6677f49e8282
# https://www.youtube.com/watch?v=JwSS70SZdyM
# define the ticker symbol


tickerSymbol = st.text_input("Enter Stock Ticker","GOOGL") #GOOGL, AAPL, NVDA etc
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
#tickerDf = tickerData.history(period = '1d', start= '2010-5-31', end = '2020-5-31')
# Open HIgh   Low Close  Volume Dividends  Stock Splits
import datetime
start_date = st.date_input("Start Date", datetime.date(2010, 5, 31))
end_date = st.date_input("End Date", datetime.date(2020, 5, 31))
#st.line_chart(tickerDf.Close)
#st.line_chart(tickerDf.Volume)

try:
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=start_date, end=end_date)
    if tickerDf.empty:
        st.error("No data found. Please check the ticker symbol or date range.")
    else:
        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)
except Exception as e:
    st.error(f"Error fetching data: {e}")
