import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

variables = pandas.read_csv('Placement.csv')
variables.gender = le.fit_transform(list(variables["gender"]))
print (variables.gender)
X = variables[['gender']]
Y = variables[['mba_p']]


kmeans=KMeans(n_clusters=4)
kmeansoutput=kmeans.fit(Y)
y_km=kmeansoutput.labels_

pl.scatter(Y, y_km)
pl.xlabel('gender')
pl.ylabel('degree')
pl.title('2 Cluster K-Means')
pl.show()


