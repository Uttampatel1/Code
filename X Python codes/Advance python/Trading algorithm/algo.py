import pandas as pd
import numpy as np
import requests 
import math
#import XlsxWriter

#stocks = pd.read_csv('NSEI.csv')
#print (stocks)
stocks = pd.read_csv('sp_500_stocks.csv')
#print (stocks)

from secrets import IEX_CLOUD_API_TOKEN

symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
#print (api_url)

data = requests.get(api_url).json()
#print (data.status_code)
#print (data)

price = data['latestPrice']
market_cap= data['marketCap']
#print (price)
#print(market_cap/1000000000000)

my_columns = ['Ticker','Stock Price', 'Market capitalization', 'Number of shares to Buy']
'''
final_dataframe = pd.DataFrame(columns=my_columns)
#print (final_dataframe)

final_dataframe.append(
    pd.Series(
    [
        symbol,price,market_cap,'N/A'
    ],
    index = my_columns 
    ),ignore_index=True 
)
#print (final_dataframe)
'''
final_dataframe = pd.DataFrame (columns= my_columns)

for stock in stocks['Ticker'][:2]:
	api_url = f'https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}'
	data = requests.get(api_url).json()
	final_dataframe = final_dataframe.append(
    pd.Series(
    [
        stock, 
        data['latestPrice'], 
        data['marketCap'],
        'N/A'
    ],
    index = my_columns 
    ),ignore_index=True 
    )
print (final_dataframe)

def chunks(lst,n):
	for i in range (0,len(lst),n):
		yield lst[i:i+n]
		
symbol_groups = list(chunks(stocks['Ticker'],100))
symbol_string = []

for i in range (0,len(symbol_groups)):
	symbol_string.append(','.join(symbol_groups[i]))
#	print (symbol_string[i])

