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
    ax.set_title(team + " Offensive Style (2020-21)", y=1.08)
    
    plt.savefig('style_graphs/{} Offensive Style.png'.format(team), bbox_inches='tight')



tracking = pd.read_csv('tracking.csv')  
colors = pd.read_csv('teamcolors.csv', delimiter = "\t", header = 1)  
colors = colors.replace("Los Angeles Clippers", "LA Clippers")

teams = tracking.get("TEAM").tolist()

teamstats = dict.fromkeys(teams)

for team in teams:
    teamstats[team] = []

keystats = ["AVG SPEED OFF", "AVG SEC PER TOUCH", "PASSES MADE", '0-3ft RIM FREQ', '10-16ft MIDRANGE FREQ', '3PT FREQ']

scaler = MinMaxScaler()
tracking[keystats[:3]] = scaler.fit_transform(tracking[keystats[:3]])

for index, row in tracking.iterrows():
    for stat in keystats[:3]:
        teamstats[row["TEAM"]].append(row[stat])

shottypes = pd.read_html('shotdistances.xls')[0]

shottypes.columns = [f'{i} {j}' for i, j in shottypes.columns]

shottypes = shottypes.rename(columns={"Unnamed: 1_level_0 Team": "TEAM", "% of FGA by Distance 10-16": "10-16ft MIDRANGE FREQ", 
                                      "% of FGA by Distance 0-3": "0-3ft RIM FREQ", '% of FGA by Distance 3P': "3PT FREQ"})

shottypes['TEAM'] = shottypes['TEAM'].apply(lambda x: x.rstrip("*"))

shottypes = shottypes.replace("Los Angeles Clippers", "LA Clippers")

shottypes[keystats[3:]] = scaler.fit_transform(shottypes[keystats[3:]])

for index, row in shottypes.iterrows():
    for stat in keystats[3:]:
        if row["TEAM"] in teamstats:
            teamstats[row["TEAM"]].append(row[stat])

for team in teams:
    print(team)
    plot_team(team)
    

