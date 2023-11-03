# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:43:31 2019

"""

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import dataset
dataset = pd.read_csv(r'D:\Jacobs\Lecture\PTM\Sources\2021\Regression\Datasets\gebrauchtwagen.csv')
X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 3].values


# scatter plot the data using panda
print(dataset.describe());
dataset.plot.scatter(x='km', y='price')
plt.show()

# split the dataset into test and train (1-test) dataset
from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# fit SLR to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


#To retrieve the intercept:
print(regressor.intercept_)
#For retrieving the slopes/coefficients
print(regressor.coef_)


# predict test set
y_pred = regressor.predict(X_test)
plt.scatter(X_test, y_pred)


# Visualize the training set, test set, and result
plt.scatter(X_train,y_train,color = 'red')
plt.scatter(X_test,y_test,color = 'yellow')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('km&price(training set)')
plt.xlabel('km')
plt.ylabel('price')
plt.show()


#Model evaluation
# print the R-squared value for the model
print('R Score =' + str(regressor.score(X, y)))

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


