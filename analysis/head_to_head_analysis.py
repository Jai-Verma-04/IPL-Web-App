# -------------------------------------------------------------------------------------------------------
# File Name: head_to_head_analysis.py
# Author: Jai Verma
# Description: Calculates the Head to Head team stats in IPL.
#              These functions will be used by the Head to Head Stats page to display these stats for the 
#              selected teams by the user.
#              
# -------------------------------------------------------------------------------------------------------


import pandas as pd

# importing read_data from utils to read the data from the parquet files
from utils.read_data import matches, deliveries


#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#


def matches_played(team_1: str, team_2: str) -> int:
    return matches[(matches[['team1', 'team2']].isin([team_1, team_2])).all(axis=1)].shape[0]   


def total_wins(team_1, team_2):
    return matches[(matches[['team1', 'team2']].isin([team_1, team_2])).all(axis=1)]['winner'].value_counts().reset_index()


def win_percentage(team_1, team_2):
    table = matches[(matches[['team1', 'team2']].isin([team_1, team_2])).all(axis=1)]['winner'].value_counts(normalize=True).reset_index()
    table.columns = ['team', 'Win Percentage']
    table['Win Percentage'] = table['Win Percentage'].map(lambda x: f"{round(x*100, 2)}%")

    return table


def most_runs(team_1, team_2):
    vs = deliveries[(deliveries[['batting_team', 'bowling_team']].isin([team_1, team_2])).all(axis=1)]
    most_runs_player = vs[['batter', 'batsman_runs']].groupby('batter').agg('sum').idxmax().values[0]
    total_runs = vs[['batter', 'batsman_runs']].groupby('batter').agg('sum').max().values[0]

    return most_runs_player, total_runs


def most_wickets(team_1, team_2):
    vs = deliveries[(deliveries[['batting_team', 'bowling_team']].isin([team_1, team_2])).all(axis=1)]
    most_wickets_player = vs[['is_wicket', 'bowler']].groupby('bowler').agg('count').idxmax().values[0]
    total_wickets = vs[['is_wicket', 'bowler']].groupby('bowler').agg('count').max().values[0]

    return most_wickets_player, total_wickets


def highest_score(team_1, team_2):
    table = matches[(matches[['team1', 'team2']].isin([team_1, team_2])).all(axis=1)]

    return table[table.target_overs == 20]['target_runs'].max()


def lowest_score(team_1, team_2):
    table = matches[(matches[['team1', 'team2']].isin([team_1, team_2])).all(axis=1)]

    return table[table.target_overs ==20]['target_runs'].min()


def highest_margin(team_1, team_2):
    vs2 = matches[(matches[['team1', 'team2']].isin([team_1, team_2])).all(axis=1)]
    vs2.season = vs2.season.map(lambda x: f"{int(x)}")

    return vs2[(vs2.target_overs == 20) & (vs2.result_margin == vs2.result_margin.max())].iloc[:, [2,3,4,5,6,7,10,11,12,14,15]]


# Last 5 matches result
def recent_form(team_1, team_2):
    vs2 = matches[(matches[['team1', 'team2']].isin([team_1, team_2])).all(axis=1)]

    return vs2.tail(5)['winner'].value_counts().reset_index()


def playoffs_performance(team_1, team_2):
    vs2 = matches[(matches[['team1', 'team2']].isin([team_1, team_2])).all(axis=1)]
    return vs2[vs2.match_type != 'League']['winner'].value_counts()
