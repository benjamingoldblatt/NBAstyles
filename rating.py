from numpy import right_shift
import pandas as pd
import csv
import matplotlib.pyplot as plt

df = pd.read_csv('rating.csv')
salarycap = df['ACTIVE CAP'].to_numpy()
winperc = df['WIN PERCENTAGE'].to_numpy()
teams = df['TEAM']

plt.scatter(salarycap[15:], winperc[15:])
plt.xlabel("salary cap")
plt.ylabel("win percentage")
for i, label in enumerate(teams[15:]):
    str = ""
    arr = label.split(' ')
    if len(arr) > 2:
        arr = arr[1:]
    for j in range(1, len(arr)):
        str = str + arr[j]
    plt.annotate(str, (salarycap[15 + i], winperc[15 + i]+.003))
plt.show()