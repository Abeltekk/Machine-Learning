from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans




Data = pd.read_csv("epl_2019.csv")
x = "general_league_position"
y = "attack_scored"
df = Data[[x, y]]
  

  
kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_

print(centroids)

plt.scatter(df[x], df[y], c= kmeans.labels_, s=50, alpha=0.7)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()
