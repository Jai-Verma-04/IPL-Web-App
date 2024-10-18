# -------------------------------------------------------------------------------------------------------
# File Name: team_analysis.py
# Author: Jai Verma
# Description: Analyse and extract some key stats from the data for every team.
#              These functions will be used by the Team Analysis page to display these stats for the team 
#              selected by the user.
# -------------------------------------------------------------------------------------------------------


# Importing the required libraries
import os
import sys
import pandas as pd


# Setting the current working directory as system path
current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))


# importing read_data from utils to read the data from the parquet files.
from utils import read_data     


# reading data files using read_data module
deliveries = read_data.deliveries_data()
matches = read_data.matches_data()


#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#


def number_of_matches_played(team: str) -> int:
    '''
    The function takes team as input and returns the total number of matches played by the team.

    #### Parameter: 
    Team (Selected Team)

    #### Returns: 
    Total Number of matches played by the selected team.
    '''
    return matches[(matches.team1 == team) | (matches.team2 == team)]['id'].nunique() 


def number_of_matches_won(team: str) -> int:
    '''
    The function takes team as input and returns the total number of matches won by the team.

    #### Parameter: 
    Team (selected team)

    #### Returns:
    Total number of matches won by the team.
    '''
    return matches.winner.value_counts().loc[team]


def win_percentage(team: str) -> float:
    '''
    The function takes team as input and returns the winning percentage of the team (of all ipl seasons).

    #### Parameter:
    Team (selected team)

    #### Returns:
    Percentage of matches won in IPL.
    
    #### Formula:
    Total number of matches won / Total number of matches played * 100

    #### Uses the number_of_matches_won and number_of_matches_played functions.
    '''
    return round(number_of_matches_won(team)/number_of_matches_played(team) * 100, 2)


def most_wins_against(team: str) -> pd.Series:
    '''
    Returns the opponent team against which the given team has the most wins and the number of wins.

    #### Parameters:
    Team (selected team)
    
    #### Returns:
            Against the team:[Team name]
            Number of wins:[Wins]   
    '''

    crosstab_result = pd.crosstab(matches.team1, matches.team2)    # Create a crosstab of each team

    most_wins_against_teams = pd.DataFrame({                        # Create a pandas series object
        'Against the team ': crosstab_result.idxmax(axis=1),        # Name of the team against which most wins occurs
        'Number of Wins': crosstab_result.max(axis=1),              # Total Number of wins against that team
    }).loc[team]                                                    # locate the name of the team given in the function input

    return most_wins_against_teams


def matches_per_season(team: str) -> pd.DataFrame:
    '''
    Returns the total number of matches played in each season for the given team.

    #### Parameter:
    Team (selected team)

    #### Returns:
    pd.DataFrame: number of matches played in each season.

    Returns a table with columns 'season', 'count'.
    '''
    
    return matches[(matches.team1 == team) | (matches.team2 == team)]['season'].value_counts().sort_index().reset_index()
    

def most_matches_won_at_venue(team: str) -> tuple:
    '''
    Returns the venue (stadium) at which the team has won the most matches and number of matches won at that venue.

    #### Parameter:
    Team (selected team)

    #### Returns:
    Tuple with first element as the venue (stadium name) and the second element is the number of matches won at that venue.
    '''
    return matches[(matches.winner == team)]['venue'].value_counts().idxmax(), matches[(matches.winner == team)]['venue'].value_counts().max()


def number_of_trophies(team: str) -> int:
    '''
    Returns the total number of ipl trophies won by the selected team.

    #### Parameter:
    Team (selected team)

    #### Returns:
    Number of IPL Trophies won by the selected team.
    '''
    return matches[matches.match_type == 'Final']['winner'].value_counts().loc[team]


def match_and_toss(team: str) -> pd.DataFrame:
    '''
    Returns a 2x2 contingency table showing the relationship between match and toss outcomes.

    #### Parameter:
    Team (selected team)

    #### Returns:
    pd.DataFrame: A contingency table with match outcomes (won/lost) and toss outcomes (won/lost), along with totals.

    #### Table Format

    |               | Tosses Won&nbsp; | Tosses Lost &nbsp;| Total
    |---------------|------------|-------------|-------|
    | Matches Won   
    | Matches Lost  
    | Total         
    '''

    lu = matches[(matches.toss_winner == team) & (matches.winner == team)].count().values[0]     
    ll = matches[(matches.toss_winner == team) & (matches.winner != team)].count().values[0]
    ru = matches[(matches.toss_winner != team) & (matches.winner == team)].count().values[0]
    rl = number_of_matches_played(team) - number_of_matches_won(team)-ll
    
    return pd.DataFrame([[lu, ru, lu+ru], [ll, rl, ll+rl], [lu+ll, ru+rl, lu+ll+ru+rl]], columns=(['Tosses Won', 'Tosses Lost', 'Total']), index=['Matches Won', 'Matches Lost', 'Total'])


def highest_team_score(team: str) -> tuple:
    '''
    Returns the maximum score that the team has scored and the team against which it was made.

    #### Parameter:
    Team (selected team)

    #### Returns:
    tuple: (against the team, highest score) 
    '''
    filtered_matches = matches[matches.team1 == team]

    max_index = filtered_matches['target_runs'].idxmax()

    team2 = filtered_matches.loc[max_index, 'team2']
    target_runs = filtered_matches.loc[max_index, 'target_runs']

    return team2, target_runs


def total_6s(team: str) -> int:
    '''
    Returns the total number of 6s hit by the team.

    #### Parameter:
    Team (selected team)

    #### Returns:
    Total Number of 6s hit by the team in all seasons combined.
    '''
    return deliveries[(deliveries.batting_team == team)  & (deliveries.batsman_runs == 6)].shape[0]


def total_4s(team: str) -> int:
    '''
    Returns the total number of 4s hit by the team.

    #### Parameter:
    Team (selected team)

    #### Returns:
    Total Number of 4s hit by the team in all seasons combined.
    '''
    return deliveries[(deliveries.batting_team == team)  & (deliveries.batsman_runs == 4)].shape[0]


def top3_run_scorers(team: str) -> pd.DataFrame:
    '''
    Returns the Top 3 Run scorers of the team.

    #### Parameter:
    Team (selected team)

    #### Returns:
    pd.DataFrame: Top 3 Scorers from the team along with the runs that they have scored.
    '''
    batting_data = deliveries[deliveries.batting_team == team]
    top_scorers = batting_data.groupby('batter')['batsman_runs'].sum().reset_index().sort_values(by='batsman_runs', ascending=False).head(3)
    
    return top_scorers


def top3_wicket_takers(team: str) -> pd.DataFrame:
    '''
    Returns the Top 3 Wicket takers of the team.

    #### Parameter:
    Team (selected team)

    #### Returns:
    pd.DataFrame: Top 3 wicket takers from the team along with the wickets that they have taken.
    '''
    bowling_data = deliveries[(deliveries['bowling_team'] == team) & (deliveries['is_wicket'] == 1)]
    top_wicket_takers = bowling_data.groupby('bowler')['player_dismissed'].count().reset_index().sort_values(by='player_dismissed', ascending=False).head(3)

    return top_wicket_takers


def avg_powerplay_score(team: str) -> int:
    '''
    Returns the average powerplay score of the team.

    #### Parameter:
    Team (selected team)

    #### Returns:
    Returns the average powerplay (overs 0 - 5) score of the selected team.
    '''
    team_powerplay_data = deliveries[(deliveries['batting_team'] == team) & (deliveries['over'] <= 5)]
    avg_powerplay_score = round(team_powerplay_data.groupby('match_id')['total_runs'].sum().reset_index().mean().values[1])

    return avg_powerplay_score