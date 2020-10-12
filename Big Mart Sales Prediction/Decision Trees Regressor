import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import csv

data = pd.read_csv("Train.csv")

le = preprocessing.LabelEncoder()


for d in data:
    if(d!= 'Item_Outlet_Sales' and d!='Item_Identifier' and d!='Outlet_Identifier' ):
        data[d] = le.fit_transform(list(data[d]))


predict = "Item_Outlet_Sales"
X = np.array(data.drop([predict,'Item_Identifier','Outlet_Identifier', 'Item_Weight', 'Item_Fat_Content', 'Outlet_Establishment_Year'], 1))
Y = np.array(data[predict])


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size = 0.1)
K = 9
model = DecisionTreeRegressor(max_depth = 15,min_samples_leaf=200)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)

print (acc)




