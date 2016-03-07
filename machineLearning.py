from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors
from sklearn.svm import LinearSVC
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

def Classify(X_train, y_train, X_test, y_test, method):
	"""
	Performs classification on daily returns.
	"""   
	if method == 'RF':   
		return RF(X_train, y_train, X_test, y_test)
        
	elif method == 'KNN':
		return KNN(X_train, y_train, X_test, y_test)
    
	elif method == 'SVM':   
		return SVMClass(X_train, y_train, X_test, y_test)

	elif method == 'LDA':
		return LinearDA(X_train, y_train, X_test, y_test)

	elif method == 'QDA': 
		return QuadDA(X_train, y_train, X_test, y_test)

def RF(X_train, y_train, X_test, y_test):
	clf = RandomForestClassifier(n_estimators=1000, n_jobs=-1)
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	return accuracy

def KNN(X_train, y_train, X_test, y_test):
	clf = neighbors.KNeighborsClassifier()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	return accuracy

def SVMClass(X_train, y_train, X_test, y_test):
	clf = LinearSVC()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	return accuracy

def QuadDA(X_train, y_train, X_test, y_test): 
	clf = QDA()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	return accuracy

def LinearDA(X_train, y_train, X_test, y_test):
	clf = LDA()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	return accuracy





