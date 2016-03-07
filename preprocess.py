from datetime import datetime
def Prep(df, test_date = datetime(2014,1,1)):
	"""
	Prepare the data for forecasting.
	Input test starting date.
	"""
	df['UpDown'] = df.laggedReturn_1.shift(-1)
	df.UpDown[df.UpDown > 0] = 1
	df.UpDown[df.UpDown <= 0] = 0
	df = df.dropna()
	features = df.columns[5:-1]
	X = df[features]
	y = df.UpDown
	X_train = X[X.index < test_date]
	y_train = y[y.index < test_date]
	X_test = X[X.index >= test_date]
	y_test = y[y.index >= test_date]
	return X_train, y_train, X_test, y_test


