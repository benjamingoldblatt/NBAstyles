import json
from numpy import right_shift
import pandas as pd
from sklearn.cluster import KMeans
import csv
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


trackingdf = pd.read_csv("playtype.csv")
teams = trackingdf['TEAM'].to_numpy()
trackingdf = trackingdf.drop('TEAM', axis=1)
print(teams)


scaler = StandardScaler()
scaler.fit(trackingdf)
StandardScaler(copy=True, with_mean=True, with_std=True)
samples_scaled = scaler.transform(trackingdf)

mergings = linkage(trackingdf, method='complete')


dendrogram(mergings,
           labels=teams,
           leaf_font_size=6,
           orientation='right'
)
plt.show()