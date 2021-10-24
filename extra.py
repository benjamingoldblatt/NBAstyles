import json
import pandas as pd
from sklearn.cluster import KMeans
import csv
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


trackingdf = pd.read_csv("playtype.csv")
teams = trackingdf['TEAM']
trackingdf = trackingdf.drop('TEAM', axis=1)

scaler = StandardScaler()
scaler.fit(trackingdf)
StandardScaler(copy=True, with_mean=True, with_std=True)
samples_scaled = scaler.transform(trackingdf)

model = KMeans(n_clusters=6)
model.fit(samples_scaled)
labels = model.predict(samples_scaled)

mergings = linkage(samples_scaled, method='complete')

dendrogram(mergings,
           labels=teams,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()
