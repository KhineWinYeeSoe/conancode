# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:06:03 2021

@author: lifestyle
"""

import streamlit as st
import pandas as pd


st.write("""
# Stock Market Web Application
**Visually** show data on a stock!Only Apple and Netflix stocks are available for now!
""")

st.sidebar.header('User Input')
def get_input():
    start_date=st.sidebar.text_input("Start Date",'2018-01-02')
    end_date=st.sidebar.text_input("End Date",'2018-08-04')
    stock_symbol=st.sidebar.text_input("Stock Symbol","AAPL")
    return start_date,end_date,stock_symbol

def get_company_name(symbol):
    if symbol=="AAPL":
        return'Apple'
    #elif symbol=="TSLA":
        #return "Tesla"
    elif symbol=="NFLX":
        return 'Netflix'
    else:
        'None'
        
def get_data(symbol,start,end):
    if symbol.upper()=='AAPL':
        df=pd.read_csv("https://raw.githubusercontent.com/iambharathvaj/Stock-Price-Prediction/master/AAPL.csv")
    elif symbol.upper()=='NFLX':
        df=pd.read_csv("https://raw.githubusercontent.com/Shivamtarone1999/Netflix-Stock-Price-Prediction/master/NFLX.csv")    
    #elif symbol.upper()=='TSLA':
        #df=pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv")
    else:
        df=pd.DataFrame(columns=['Date','Close','Open','Volume','Adj Close','High','Low'])
    
    start=pd.to_datetime(start)
    end=pd.to_datetime(end) 
    start_row=0
    end_row=0
    for i in range(0,len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row=i
            break
    for j in range(0,len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row=len(df) -1 -j
            break
    df=df.set_index(pd.DatetimeIndex(df['Date'].values))
    return df.iloc[start_row:end_row +1,:]

start,end,symbol=get_input()
df=get_data(symbol,start,end)
company_name=get_company_name(symbol.upper())

st.header(company_name+"Close Price\n")
st.line_chart(df['Close'])       
    
st.header(company_name+"Volume\n")
st.line_chart(df['Volume'])       
    
st.header('Data Statistics')
st.write(df.describe())

