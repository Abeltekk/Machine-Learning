import pandas as pd
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import preprocessing

variables = pd.read_csv('Placement.csv')
pd.read_csv("Placement" ,  index = False)
le = preprocessing.LabelEncoder()

variables.gender = le.fit_transform(list(variables["gender"]))

Y = variables[['mba_p']]
X = variables[['gender']]


X_norm = (X - X.mean()) / (X.max() - X.min())
Y_norm = (Y - Y.mean()) / (Y.max() - Y.min())
pl.scatter(Y_norm,X_norm)

kmeans=KMeans(n_clusters=2)
kmeansoutput=kmeans.fit(X)

pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.show()
