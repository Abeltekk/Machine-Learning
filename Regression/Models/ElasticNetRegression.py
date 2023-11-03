# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 07:49:46 2021

"""

"""
Elastic Net Regression
"""

#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

#Importing the dataset
dataset = pd.read_csv(r'D:\Jacobs\Lecture\PTM\Sources\2021\Regression\Datasets\gebrauchtwagen.csv')
X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 3].values


# split dataset into test and train (1-test) dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 0)

#Fitting Elastic Net regression to dataset
from sklearn.linear_model import ElasticNet
regressor = ElasticNet(alpha=1.0, l1_ratio=0.5)
regressor.fit(X_train, y_train)


from sklearn.linear_model import ElasticNetCV
from sklearn.model_selection import RepeatedKFold
from numpy import arange
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
# define model
ratios = arange(0, 1, 0.01)
alphas = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.0, 1.0, 10.0, 100.0]
model = ElasticNetCV(l1_ratio=ratios, alphas=alphas, cv=cv, n_jobs=-1)
# fit model
regressor.fit(X_train, y_train)

#prediction of new value
y_pred = regressor.predict(X_test)

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('MAPE:', np.sqrt(mean_absolute_percentage_error(y_test, y_pred)))

#visualisiong the Decision tree Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Decision tree Regression')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()



#visualisiong the decision tree Regression for smoother curve results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Random Forest Regression')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()