import pandas as pd
import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

import csv

data = pd.read_csv("Train.csv")
test = pd.read_csv("Test.csv")

le = preprocessing.LabelEncoder()


    
for d in data:
    if(d!='Item_Identifier' and d!='Outlet_Identifier' ):
        data[d] = le.fit_transform(list(data[d]))
for d in test:
    if(d!='Item_Identifier' and d!='Outlet_Identifier' ):
        test[d] = le.fit_transform(list(test[d]))

        
predict = "Item_Outlet_Sales"

X = np.array(data.drop([predict, 'Item_Identifier','Outlet_Identifier', 'Item_Fat_Content', 'Outlet_Establishment_Year'], 1))
Y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size = 0.1)

model = LinearRegression()
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print (acc)


Item_id = test['Item_Identifier']
Outlet_id = test['Outlet_Identifier']
test = np.array(test.drop(['Item_Identifier','Outlet_Identifier', 'Item_Fat_Content', 'Outlet_Establishment_Year'], 1))
predictions = model.predict(test)


fields = ['Item_Identifier', 'Outlet_Identifier', 'Item_Outlet_Sales']  
    
# data rows of csv file  
rows = [ ] 
min_val = 765
for i in range(len(test)):

    if predictions[i]<min_val: 
        predictions[i] = min_val
    rows += [[Item_id[i],Outlet_id[i], predictions[i]]]
    
# name of csv file  
filename = "solution.csv"
    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 
