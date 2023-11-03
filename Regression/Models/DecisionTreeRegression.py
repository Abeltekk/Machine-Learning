# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 22:05:34 2019

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
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 0)

#Fitting decision tree regression to dataset
from sklearn.tree import DecisionTreeRegressor
#regressor = DecisionTreeRegressor(min_samples_split  = 10)
regressor = DecisionTreeRegressor(min_samples_leaf  = 1)

regressor.fit(X_train, y_train)


#prediction of new value
y_pred = regressor.predict(X_test)

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('MAPE:', np.sqrt(mean_absolute_percentage_error(y_test, y_pred)))

#visualisiong the Decision Tree Regression results
plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Decision Tree Regression')
plt.xlabel('km')
plt.ylabel('price')
plt.show()



#visualisiong the Decision Tree Regression for smoother curve results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Decision Tree Regression')
plt.xlabel('km')
plt.ylabel('price')
plt.show()


