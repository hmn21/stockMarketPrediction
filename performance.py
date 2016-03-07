import pandas as pd

from abc import ABCMeta, abstractmethod

class Portfolio(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def generate_positions(self):
		"""
		Provide the logic to determine how the portfolio 
		positions are allocated on the basis of forecasting
		signals and available cash.
		"""
		raise NotImplementedError("Should implement generate_positions()!")

	@abstractmethod
	def backtest_portfolio(self):
		"""
		Provide the logic to generate the trading orders
		and subsequent equity curve (i.e. growth of total equity),
		as a sum of holdings and cash, and the bar-period returns
		associated with this curve based on the 'positions' DataFrame.

		Produces a portfolio object that can be examined by 
		other classes/functions.
		"""
		raise NotImplementedError("Should implement backtest_portfolio()!")

class MarketIntradayPortfolio(Portfolio):
	"""
	Buys or sells 500 shares of an asset at the opening price of
	every bar, depending upon the direction of the forecast, closing 
	out the trade at the close of the bar.
	"""

	def __init__(self, symbol, bars, signals, initial_capital=100000.0, shares=500):
		self.symbol = symbol        
		self.bars = bars
		self.signals = signals
		self.initial_capital = float(initial_capital)
		self.shares = int(shares)
		self.positions = self.generate_positions()

	def generate_positions(self):
		"""
		Generate the positions DataFrame, based on the signals
		provided by the 'signals' DataFrame.
		"""
		positions = pd.DataFrame(index=self.signals.index).fillna(0.0)

		positions[self.symbol] = self.shares*self.signals['signal']
		return positions

	def backtest_portfolio(self):
		"""
		Backtest the portfolio and return a DataFrame containing
		the equity curve and the percentage returns.
		"""

		portfolio = pd.DataFrame(index=self.positions.index)
		pos_diff = self.positions.diff()

		portfolio['price_diff'] = self.bars['AdjClose']-self.bars['Open']
		portfolio['price_diff'][0:5] = 0.0
		portfolio['profit'] = self.positions[self.symbol] * portfolio['price_diff']

		portfolio['total'] = self.initial_capital + portfolio['profit'].cumsum()
		portfolio['returns'] = portfolio['total'].pct_change()
		return portfolio


