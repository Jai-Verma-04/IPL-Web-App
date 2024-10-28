# -------------------------------------------------------------------------------------------------------
# File Name: season_analysis.py
# Author: Jai Verma
# Description: Calculates the season wise summary of IPL.
#              These functions will be used by the Season Analysis to display these stats for the season 
#              selected by the user.
# -------------------------------------------------------------------------------------------------------


import pandas as pd

# importing read_data from utils to read the data from the parquet files
from utils.read_data import matches, deliveries


deliveries_with_season = pd.merge(deliveries, matches[['id', 'season']], left_on='match_id', right_on='id', how='left')

#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#


def total_matches_played(season: int) -> int:
    return matches.season.value_counts().sort_index(ascending=False).loc[season]


def total_runs_scored(season: int) -> int:
    matches['team2_runs'] = matches.target_runs - matches.result_margin
    matches['total_runs'] = matches.target_runs + matches.team2_runs
    
    return matches[['season', 'total_runs']].groupby('season').agg('sum').loc[season].values[0]


# Also the orange cap winner
def highest_run_scorer(season: int) -> tuple:
    return deliveries_with_season[['batter','batsman_runs', 'season']].groupby(['season', 'batter']).agg('sum').loc[season].idxmax().values[0], \
    deliveries_with_season[['batter','batsman_runs', 'season']].groupby(['season', 'batter']).agg('sum').loc[season].max().values[0],


# Also the Purple cap winner
def highest_wicket_taker(season: int) -> tuple:
    return deliveries_with_season[deliveries_with_season['is_wicket'] == 1][['is_wicket', 'bowler', 'season']].groupby(['season', 'bowler']).agg('count').loc[season].idxmax().values[0], \
    deliveries_with_season[deliveries_with_season['is_wicket'] == 1][['is_wicket', 'bowler', 'season']].groupby(['season', 'bowler']).agg('count').loc[season].max().values[0]


def total_6s(season: int) -> int:
    return deliveries_with_season[(deliveries_with_season.batsman_runs == 6) & (deliveries_with_season.season == season)].shape[0]


def total_4s(season: int) -> int:
    deliveries_with_season[(deliveries_with_season.batsman_runs == 4) & (deliveries_with_season.season == season)].shape[0]


def most_wins_in_league_matches(season: int) -> tuple:
    return matches[(matches.season == season) & (matches.match_type == 'League')]['winner'].value_counts().idxmax(),\
    matches[(matches.season == season) & (matches.match_type == 'League')]['winner'].value_counts().max()


def final_match(season: int):
    match = matches[(matches.match_type == 'Final') & (matches.season == season)][['team1', 'team2', 'winner']].reset_index(drop=True)
    return match

def winner(season: int) -> str:
    match = final_match(season)

    return match.winner.iloc[0]


def runner_up(season: int) -> str:
    match = final_match(season)

    runner_up = ''

    if match.team1.iloc[0] == winner(season):
        runner_up = match.team2.iloc[0]
    else:
        runner_up = match.team1.iloc[0]

    return runner_up
