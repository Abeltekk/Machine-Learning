import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
# there are different decision tree algorithms, this one is classifying one and there is a regression one as well

data = pd.read_csv("Placement.csv")

# the attributes I wanna use
data = data[["status", "mba_p","etest_p", "ssc_p",  "hsc_p", "degree_p", "specialisation" , "workex"]]
le = preprocessing.LabelEncoder() # to clean the data for use

# using label econder to clean the data in this case from strings to integers so we can use them
data.workex = le.fit_transform(list(data["workex"]))
data.specialisation = le.fit_transform(list(data["specialisation"]))
data.status = le.fit_transform(list(data["status"]))

# divide the values into the data you have and the one you want to predict
predict = "status"
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# divide data into training and testing data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

# making a model, fitting it with the train data and then check the accuracy 
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)







