import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
import sklearn

data = pd.read_csv("student-mat.csv", sep=";")
gender = {'M': 1,'F': 2} 
data["sex"] = [gender[item] for item in data["sex"]] 

data = data[["sex", "G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "sex"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
acc = classifier.score(x_test, y_test)


print (acc)

predictions = classifier.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
