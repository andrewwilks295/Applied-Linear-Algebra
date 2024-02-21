# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:40:52 2023

@author: wilks
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris_names = load_iris()['target_names']
iris_types = load_iris()['target']

iris_feature = load_iris()['feature_names']
iris_data = np.array(load_iris()['data'])

k = 3
kmeans= KMeans(n_clusters = k, random_state = 0)
kmeans.fit(iris_data)

print("\n\nI predict that the clustering will be fairly similar to the max and minimum numbers within the iris_data.")

#print(iris_data)
print("\nCluster Assignments:\n", iris_types)

print("Cluster Centers:\n", kmeans.cluster_centers_)


print("\nFrom what I understand, the clustering is very good when")
print("the difference between the numbers if extremely small.")
print("All three clusters have insignificant differences when it comes to the")
print("final numbers in the returned set. The differences are very few.")
print("The numbers go from about 6 down to about 0.2 in both the iris_data")
print("and in the final clustering of centers. I could have made an error by")
print("missinterpreting something, but machine wise, I don't think there are")
print("any errors. For my hypothesis, I believe this was close to being right")
print("seeing that the data is between about 6 and 0.2. I guess some of my other errors")
print("come from my J^clust being to low, but I don't see how low is bad.")

