import pandas as pd
import mplfinance as mpf
import matplotlib 
#%matplotlib inline 

file = 'NSEI.csv'
data = pd.read_csv(file)
#print (data)
#print (data.info())
#print (data.columns)

data.Date = pd.to_datetime(data.Date)
#print (data.info())

data = data.set_index('Date')
#print (data)

#mpf.plot(data)
#mpf.plot(data,type='line',volume =True)

#mpf.plot(data['2021-07'],volume = True )

#mpf.plot(data['2021-03':'2021-07'],type='candle',mav=(20),volume = True )

#mpf.plot(data['2021-03':'2021-07'],type='candle',mav=(20),volume = True,tight_layout=True)

#mpf.plot(data['2021-03':'2021-07'],figratio(20,12),type='candle',title='Nifty 50 prices 2020/21',mav=(20),volume = True,tight_layout=True)

mpf.plot(data['2021-03':'2021-07'],figratio(20,12),type='candle',title='Nifty 50 prices 2020/21',mav=(20),volume = True,tight_layout=True,style='yahoo')