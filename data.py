import pandas as pd
from pandas import DataFrame, Series
import pandas_datareader.data as web
from datetime import datetime
from dateutil import parser
import tushare as ts

def getStock_A(ticker, start='2005-01-01', end='2015-09-30'):
	"""
	Get daily US stock data from Yahoo Finance.
	"""
	df = web.DataReader(ticker, 'yahoo', start, end)
	col_name = df.columns[-1]
	df = df.rename(columns={col_name:'AdjClose'})
	df = df[['Open', 'High', 'Low', 'Volume', 'AdjClose']]
	return df



def getStock_C(ticker, start='2005-01-01', end='2015-09-30'):
	"""
	Get daily Chinese stock data from TuShare.
	"""
	df = ts.get_h_data(ticker, index=True, start=start, end=end)
	df = df.iloc[::-1]
	df = df[['open', 'high', 'low', 'volume', 'close']]
	df.columns = ['Open', 'High', 'Low', 'Volume', 'AdjClose']
	return df


