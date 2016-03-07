import statsmodels.tsa.stattools as ts
from datetime import datetime

# Output the results of the Augmented Dickey-Fuller test for CSI300 with a lag order value of 1
ts.adfuller(HS300['AdjClose'], 1)

from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn

def hurst(ts):
	"""
	Returns the Hurst Exponent of the stock data
	"""
	lags = range(2, 100)
	tau = [sqrt(std(subtract(ts[lag:], ts[:-lag]))) for lag in lags]
	poly = polyfit(log(lags), log(tau), 1)
	return poly[0]*2.0

print("Hurst(CSI300):  %s" % hurst(HS300['AdjClose']))
