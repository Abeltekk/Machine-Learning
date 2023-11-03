# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:53:10 2019

"""

# import libraries
import pandas as pd
import numpy as np


# import dataset  change year to age
dataset = pd.read_csv(r"D:\Jacobs\Lecture\PTM\Sources\2021\Regression\Datasets\gebrauchtwagen.csv")
print(dataset.describe());
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values


#split dataset into test and train dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state= 0)


# === Step 2: Fit MLE to training set using all variables ===
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict test set result
y_pred = regressor.predict(X_test)

#For retrieving the intercept and slopes/coefficients
print(regressor.intercept_)
print(regressor.coef_)

#Check the quality
print('Score =' + str(regressor.score(X, y)))
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# === Step 3: Backward Elimination to optimize the model ===
import statsmodels.api as sm

# add the dummy variable ( X-zero) and set the values to ones
X_train = sm.add_constant(X_train)
X_opt = X_train[:,[0,1,2,3]]

# the sm.OLS function requires constants
model=sm.OLS(y_train,X_opt).fit()
print(model.summary())

# === Step 4: remove the variable ===
X_opt = X_train[:,[0,1,2]]
model=sm.OLS(y_train,X_opt).fit()
print(model.summary())


# === Step 5: Rebuilding the model after removing the variable ===
X_train = X_opt[:,[1,2]]
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict test set result
y_pred = regressor.predict(X_test[:,[1,2]])

#For retrieving the slopes/coefficients
print(regressor.intercept_)
print(regressor.coef_)


#Check the quality
print('Score =' + str(regressor.score(X_train, y_train)))
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

