import sklearn
import sklearn.model_selection
import sklearn.cluster
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
d=pd.read_csv("C:\\Users\\Ritvik\\Documents\\datasets\\Iris.csv")
d1=d['Id']
d=d.drop(['Id'],axis=1)
y=d['Species']
d=d.drop(['Species'],axis=1)
x=d
kmeans=sklearn.cluster.KMeans(n_clusters=6)
kmeans.fit(x)
print(kmeans.cluster_centers_)
plt.plot(d['PetalLengthCm'][y=='Iris-setosa'],d['PetalWidthCm'][y=='Iris-setosa'],"k.")
plt.plot(d['PetalLengthCm'][y=='Iris-versicolor'],d['PetalWidthCm'][y=='Iris-versicolor'],"r.")
plt.plot(d['PetalLengthCm'][y=='Iris-virginica'],d['PetalWidthCm'][y=='Iris-virginica'],"g.")
plt.scatter(kmeans.cluster_centers_[:,2:3],kmeans.cluster_centers_[:,3:])

plt.show()
