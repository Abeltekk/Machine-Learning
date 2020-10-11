


import numpy as np
import pandas as pd
import sklearn
from sklearn import svm
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler 
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt 
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.cluster import KMeans


data = pd.read_csv("Placement.csv")

data = data[[ "status", "mba_p","etest_p", "specialisation","gender", "ssc_p", "ssc_b", "hsc_p", "hsc_b", "hsc_s", "degree_p", "degree_t", "workex"]]
# the data has everything but salary
le = preprocessing.LabelEncoder() # to convert labels in to numberic forms
# so the machine can work with them
data.gender = le.fit_transform(list(data["gender"])) # changing the string labelings to integers, 0 and 1 in this case
data.ssc_b = le.fit_transform(list(data["ssc_b"]))
data.hsc_b = le.fit_transform(list(data["hsc_b"]))
data.hsc_s = le.fit_transform(list(data["hsc_s"]))
data.degree_t = le.fit_transform(list(data["degree_t"]))
data.workex = le.fit_transform(list(data["workex"]))
data.specialisation = le.fit_transform(list(data["specialisation"]))
data.status = le.fit_transform(list(data["status"]))


predict = "status"
X = np.array(data.drop([predict], 1))
y = np.array(data[predict])


sc = StandardScaler()
X = sc.fit_transform(X) 

pca = PCA(n_components = 2) 
X = pca.fit_transform(X) 
kmeans = KMeans(n_clusters=7).fit(data)


plt.scatter (X[ : , 0], X[ : , 1],  c= kmeans.labels_, s=50, alpha=0.7)
plt.show()






