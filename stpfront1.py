# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:35:34 2021

@author: lifestyle
"""

import pickle
import streamlit as st
import yfinance as yf
import pandas as pd 
import datetime
import sklearn

st.markdown('''
#   APPLE Stock Price Prediction App

Shown are the stock price data for Apple Inc.

''')
st.write('---')
st.sidebar.subheader('Query parameters')
start_date=st.sidebar.date_input("Start date",datetime.date((2009), 9, 14))
end_date=st.sidebar.date_input("End date",datetime.date((2019), 9, 21))

st.title('Apple Stock Price Chart')
df=pd.read_csv('https://raw.githubusercontent.com/iambharathvaj/Stock-Price-Prediction/master/AAPL.csv')
st.write(df)

tickers=['AAPL']
yf.download(tickers,start='2009-09-14',end='2019-09-21')

ticker_list=pd.read_csv('https://raw.githubusercontent.com/iambharathvaj/Stock-Price-Prediction/master/AAPL.csv')
tickerSymbol=st.sidebar.selectbox('Stock ticker',ticker_list)
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d',start=start_date,end=end_date)

st.header('**Ticker data**')
st.write('Chart Sample')
st.write(tickerDf)

tickerSymbol ='AAPL'

tickerData=yf.Ticker(tickerSymbol)

tickerDf=tickerData.history(period='1d',start='2009-9-14',end='2019-9-21')

st.write("""
         ##Closing Price
         """)
st.line_chart(tickerDf.Close)
st.write("""
         ##Volume
         """)
st.line_chart(tickerDf.Volume)


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
