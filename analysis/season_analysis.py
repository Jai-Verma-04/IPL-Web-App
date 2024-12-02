# -------------------------------------------------------------------------------------------------------
# File Name: season_analysis.py
# Author: Jai Verma
# Description: Calculates the season wise summary of IPL.
#              These functions will be used by the Season Analysis to display these stats for the season 
#              selected by the user.
# -------------------------------------------------------------------------------------------------------


import random
import pandas as pd

# importing read_data from utils to read the data from the parquet files
from utils.read_data import matches, deliveries
from utils.data import IPL_FACTS_BY_SEASON

deliveries_with_season = pd.merge(
                            deliveries, matches[['id', 'season']], 
                            left_on='match_id', 
                            right_on='id', 
                            how='left'
                            )

#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#


def total_matches_played(season: int) -> int:
    '''
    The function takes season as input and returns the total number of matches played in that season.
    
    #### Parameter: 
    season

    #### Returns: 
    Total number of matches played in the selected season.
    '''
    return matches.season.value_counts().sort_index(ascending=False).loc[season]


def total_runs_scored(season: int) -> int:
    '''
    The function takes season as input and returns the total runs scored in that season.
    
    #### Parameter: 
    season

    #### Returns: 
    Total runs scored in the selected season.
    '''
    matches['team2_runs'] = matches.target_runs - matches.result_margin
    matches['total_runs'] = matches.target_runs + matches.team2_runs
    
    return matches[['season', 'total_runs']].groupby('season').agg('sum').loc[season].values[0]


# Also the orange cap winner
def highest_run_scorer(season: int) -> tuple:
    '''
    The function takes season as input and returns the highest run scorer in that season.
    
    #### Parameter: 
    season

    #### Returns: 
    tuple: (player name, runs)
    Highest run scorer in the selected season
    '''
    player = deliveries_with_season[
                    ['batter','batsman_runs', 'season']
                ].groupby(
                        ['season', 'batter']
                    ).agg('sum').loc[season].idxmax().values[0]
    
    runs = deliveries_with_season[
                    ['batter','batsman_runs', 'season']
                ].groupby(
                        ['season', 'batter']
                    ).agg('sum').loc[season].max().values[0]

    return player, runs


# Also the Purple cap winner
def highest_wicket_taker(season: int) -> tuple:
    '''
    The function takes season as input and returns the highest wicket taker in that season.
    
    #### Parameter: 
    season

    #### Returns: 
    tuple: (player name, wickets)
    Highest wickets taker in the selected season
    '''
    player = deliveries_with_season[
                    deliveries_with_season['is_wicket'] == 1
                ][
                    ['is_wicket', 'bowler', 'season']
                ].groupby(
                        ['season', 'bowler']
                    ).agg('count').loc[season].idxmax().values[0]

    wickets = deliveries_with_season[
                    deliveries_with_season['is_wicket'] == 1
                ][
                    ['is_wicket', 'bowler', 'season']
                ].groupby(
                        ['season', 'bowler']
                    ).agg('count').loc[season].max().values[0]

    return player, wickets


def total_6s(season: int) -> int:
    '''
    The function takes season as input and returns the total number of 6s hit in that season.
    
    #### Parameter: 
    season

    #### Returns: 
    Total number of 6s hit in the selected season.
    '''
    return deliveries_with_season[
                (deliveries_with_season.batsman_runs == 6) & (deliveries_with_season.season == season)
            ].shape[0]


def total_4s(season: int) -> int:
    '''
    The function takes season as input and returns the total number of 4s hit in that season.
    
    #### Parameter: 
    season

    #### Returns: 
    Total number of 4s hit in the selected season.
    '''
    return deliveries_with_season[
                (deliveries_with_season.batsman_runs == 4) & (deliveries_with_season.season == season)
            ].shape[0]


def final_match(season: int) -> pd.DataFrame:
    '''
    Helper function takes season as input and returns the final match of the season.
    
    #### Parameter: 
    season

    #### Returns: 
    Final match of the season
    '''
    match = matches[
                (matches.match_type == 'Final') & (matches.season == season)
            ][
                ['id', 'team1', 'team2', 'winner']
            ].reset_index(drop=True)
    
    return match


def winner(season: int) -> str:
    '''
    The function takes season as input and returns the team that won the selected season.
    
    #### Parameter: 
    season

    #### Returns: 
    Winner of the selected season
    '''
    match = final_match(season)

    return match.winner.iloc[0]


def runner_up(season: int) -> str:
    '''
    The function takes season as input and returns the team that was runners up selected season.
    
    #### Parameter: 
    season

    #### Returns: 
    Runners up of the selected season
    '''
    match = final_match(season)

    if match.team1.iloc[0] == winner(season):
        return match.team2.iloc[0]
    
    return match.team1.iloc[0]

def random_fact(season: int) -> str:
    '''
    Returns a random fact for the selected season
    '''
    fact = random.choice(IPL_FACTS_BY_SEASON.get(season))
    
    return fact