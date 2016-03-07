import talib
import numpy as np

def addFeatures(stock):
	"""
	Input pandas data frame, generate features for sock.
	"""
	df = stock
	df['TSF'] = talib.TSF(np.asarray(df.AdjClose))
	df['STDDEV'] = talib.STDDEV(np.asarray(df.AdjClose))
	real = talib.ADOSC(np.asarray(df.High), np.asarray(df.Low), np.asarray(df.AdjClose), np.asarray(df.Volume.astype('double')))
	df['ADOSC'] = real > 0
	df['ADOSC'] = df['ADOSC'].astype(int)
	df['ADX'] = talib.ADX(np.asarray(df.High), np.asarray(df.Low), np.asarray(df.AdjClose))
	macd, macdsignal, macdhist = talib.MACD(np.asarray(df.AdjClose))
	df['MACD'] = macd
	df['MOM'] = talib.MOM(np.asarray(df.AdjClose))
	df['MFI'] = talib.MFI(np.asarray(df.High), np.asarray(df.Low), np.asarray(df.AdjClose), np.asarray(df.Volume.astype('double')))
	df['RSI'] = talib.RSI(np.asarray(df.AdjClose))
	df['TRIX'] = talib.TRIX(np.asarray(df.AdjClose))
	df['ATR'] = talib.ATR(np.asarray(df.High), np.asarray(df.Low), np.asarray(df.AdjClose))
	#Add 9 lagged return
	for i in range(1,10):
		name = 'laggedReturn_' + str(i)
		df[name] = df.AdjClose.pct_change(periods=i)
	return df


