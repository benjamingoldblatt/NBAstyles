import csv
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def plot_team(team):
    points = len(keystats)
    angles = np.linspace(0, 2 * np.pi, points, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    ax.set_rgrids([]) # This removes grid lines

    ax.set_thetagrids(np.degrees(angles), keystats)
    team_stats= teamstats[team]
    team_stats = team_stats+team_stats[:1]
    color1 = colors[colors["NBA Team Name"] == team]["Color 1"]
    color1 = color1.to_string().split(" ")[-1]
    
    color2 = colors[colors["NBA Team Name"] == team]["Color 2"]
    color2 = color2.to_string().split(" ")[-1]
    
    ax.plot(angles, team_stats, linewidth=0.75, color = color2)
    ax.fill(angles, team_stats, alpha=0.25, color = color1)
    ax.set_title(team + " Offensive Profile (2020-21)", y=1.08)
    
    plt.savefig('playtype_graphs/{}.png'.format(team), bbox_inches='tight')



playtype = pd.read_csv('playtype.csv')  
colors = pd.read_csv('teamcolors.csv', delimiter = "\t", header = 1)  
colors = colors.replace("Los Angeles Clippers", "LA Clippers")

pnr_sum = playtype["PICKNROLL(ball-handler) FREQ"] + playtype["PICKNROLL(role-man) FREQ"]
playtype["PNR FREQUENCY"] = pnr_sum

teams = playtype.get("TEAM").tolist()

teamstats = dict.fromkeys(teams)

for team in teams:
    teamstats[team] = []

keystats = ["ISOLATION FREQ", "PNR FREQUENCY", "POSTUP FREQ", "TRANSITION FREQ", "SPOT UP FREQ"]

scaler = MinMaxScaler()
playtype[keystats] = scaler.fit_transform(playtype[keystats])

for index, row in playtype.iterrows():
    for stat in keystats:
        teamstats[row["TEAM"]].append(row[stat])


for team in teams:
    print(team)
    plot_team(team)
    