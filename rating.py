from numpy import right_shift
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


df = pd.read_csv('rating.csv')
salarycap = df['ACTIVE CAP'].to_numpy()
winperc = df['OFFRTG'].to_numpy()
teams = df['TEAM']
pnrs = ["Kings", "Jazz", "Hawks", "Bulls", "Cavaliers", "Mavericks", "Magic"]
isos = ["Celtics", "Knicks", "Blazers", "Clippers"]
isotrans = ["Nets", "Bucks", "Wizards"]
spotuptrans = ["Hornets", "Warriors", "Rockets", "Pacers", "Raptors"]
post = ["Nuggets", "76ers", "Lakers"]
spotup = ["Pistons", "Thunder", "Timberwolves", "Suns"]
spotuptranspnr = ["Grizzlies", "Heat", "Pelicans", "Suns", "Spurs"]



plt.scatter(salarycap, winperc)
plt.xlabel("salary cap (billions)")
plt.ylabel("OFFRTG")
plt.title("Offensive Rating vs Salary Cap")
for i, label in enumerate(teams):
    str = ""
    arr = label.split(' ')
    if len(arr) > 2:
        arr = arr[1:]
    for j in range(1, len(arr)):
        str = str + arr[j]
    if str in pnrs:
        if (str == "Bulls"):
            plt.annotate(str, (salarycap[i], winperc[i]), color='red') 
        elif (str == "Jazz"):
            plt.annotate(str, (salarycap[i], winperc[i]-.25), ha='center', color='red') 
        else:
            plt.annotate(str, (salarycap[i], winperc[i]+.15), color='red')
    elif str in isos:
        plt.annotate(str, (salarycap[i], winperc[i]+.15), color='blue')   
    elif str in isotrans:
        if (str == "Wizards"):
            plt.annotate(str, (salarycap[i], winperc[i]+.2), color='green', ha="right") 
        elif (str == "Bucks"):
            plt.annotate(str, (salarycap[i], winperc[i]+.25), color='green') 
        else:
            plt.annotate(str, (salarycap[i], winperc[i]+.15), color='green')
    elif str in spotuptrans:
        plt.annotate(str, (salarycap[i], winperc[i]), color='orange')   
    elif str in post:
        if (str == "Nuggets"):
            plt.annotate(str, (salarycap[i], winperc[i]+.15), color='turquoise', ha='right') 
        else:
            plt.annotate(str, (salarycap[i], winperc[i]+.15), color='turquoise')   
    elif str in spotup:
        plt.annotate(str, (salarycap[i], winperc[i]), color='brown')   
    elif str in spotuptranspnr:
        if (str == "Pelicans"):
            plt.annotate(str, (salarycap[i], winperc[i]-.4))
        else:
            plt.annotate(str, (salarycap[i], winperc[i]+.15))

plays = ['picknroll', 'isolation', 'isol/transit', 'spotup/transit', 'postup', 'spotup', 'transtion/spotup/pnr']
colors=['red', 'blue', 'green', 'orange', 'turquoise', 'brown', 'black']
lines = [Line2D([0], [0], color=c, linewidth=3, linestyle='--') for c in colors]

plt.legend(lines, plays)


plt.show()