# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:57:42 2021

@author: Teo Bee Guan
"""

import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

snp500 = pd.read_csv("Datasets/SP500.csv")
symbols = snp500['Symbol'].sort_values().tolist()

st.set_page_config(
    page_title="Market Profile Chart (US S&P 500)",
    layout="wide")


ticker = st.sidebar.selectbox(
    'Choose a S&P 500 Stock',
     symbols)

i = st.sidebar.selectbox(
        "Interval in minutes",
        ("1m", "5m", "15m", "30m")
    )

p = st.sidebar.number_input("How many days (1-30)", min_value=1, max_value=30, step=1)

stock = yf.Ticker(ticker)
history_data = stock.history(interval = i, period = str(p) + "d")

prices = history_data['Close']
volumes = history_data['Volume']

lower = prices.min()
upper = prices.max()

prices_ax = np.linspace(lower,upper, num=20)

vol_ax = np.zeros(20)

for i in range(0, len(volumes)):
    if(prices[i] >= prices_ax[0] and prices[i] < prices_ax[1]):
        vol_ax[0] += volumes[i]   
        
    elif(prices[i] >= prices_ax[1] and prices[i] < prices_ax[2]):
        vol_ax[1] += volumes[i]  
        
    elif(prices[i] >= prices_ax[2] and prices[i] < prices_ax[3]):
        vol_ax[2] += volumes[i] 
        
    elif(prices[i] >= prices_ax[3] and prices[i] < prices_ax[4]):
        vol_ax[3] += volumes[i]  
        
    elif(prices[i] >= prices_ax[4] and prices[i] < prices_ax[5]):
        vol_ax[4] += volumes[i]  
        
    elif(prices[i] >= prices_ax[5] and prices[i] < prices_ax[6]):
        vol_ax[5] += volumes[i] 
        
    elif(prices[i] >= prices_ax[6] and prices[i] < prices_ax[7]):
        vol_ax[6] += volumes[i] 

    elif(prices[i] >= prices_ax[7] and prices[i] < prices_ax[8]):
        vol_ax[7] += volumes[i] 

    elif(prices[i] >= prices_ax[8] and prices[i] < prices_ax[9]):
        vol_ax[8] += volumes[i] 

    elif(prices[i] >= prices_ax[9] and prices[i] < prices_ax[10]):
        vol_ax[9] += volumes[i] 

    elif(prices[i] >= prices_ax[10] and prices[i] < prices_ax[11]):
        vol_ax[10] += volumes[i] 

    elif(prices[i] >= prices_ax[11] and prices[i] < prices_ax[12]):
        vol_ax[11] += volumes[i] 

    elif(prices[i] >= prices_ax[12] and prices[i] < prices_ax[13]):
        vol_ax[12] += volumes[i] 

    elif(prices[i] >= prices_ax[13] and prices[i] < prices_ax[14]):
        vol_ax[13] += volumes[i] 

    elif(prices[i] >= prices_ax[14] and prices[i] < prices_ax[15]):
        vol_ax[14] += volumes[i]   
        
    elif(prices[i] >= prices_ax[15] and prices[i] < prices_ax[16]):
        vol_ax[15] += volumes[i] 
        
    elif(prices[i] >= prices_ax[16] and prices[i] < prices_ax[17]):
        vol_ax[16] += volumes[i]         
        
    elif(prices[i] >= prices_ax[17] and prices[i] < prices_ax[18]):
        vol_ax[17] += volumes[i]         
        
    elif(prices[i] >= prices_ax[18] and prices[i] < prices_ax[19]):
        vol_ax[18] += volumes[i] 
    
    else:
        vol_ax[19] += volumes[i]
        
fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.2, 0.8],
        specs=[[{}, {}]],
        horizontal_spacing = 0.01
    
    )

fig.add_trace(
        go.Bar(
                x = vol_ax, 
                y= prices_ax,
                text = np.around(prices_ax,2),
                textposition='auto',
                orientation = 'h'
            ),
        
        row = 1, col =1
    )


dateStr = history_data.index.strftime("%d-%m-%Y %H:%M:%S")

fig.add_trace(
    go.Candlestick(x=dateStr,
                open=history_data['Open'],
                high=history_data['High'],
                low=history_data['Low'],
                close=history_data['Close'],
                yaxis= "y2"
                
            ),
    
        row = 1, col=2
    )
        

fig.update_layout(
    title_text='Market Profile Chart (US S&P 500)', # title of plot
    bargap=0.01, # gap between bars of adjacent location coordinates,
    showlegend=False,
    
    xaxis = dict(
            showticklabels = False
        ),
    yaxis = dict(
            showticklabels = False
        ),
    
    yaxis2 = dict(
            title = "Price (USD)",
            side="right"
        
        )

)

fig.update_yaxes(nticks=20)
fig.update_yaxes(side="right")
fig.update_layout(height=800)

config={
        'modeBarButtonsToAdd': ['drawline']
    }

st.plotly_chart(fig, use_container_width=True, config=config)


