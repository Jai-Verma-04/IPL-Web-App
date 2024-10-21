# -------------------------------------------------------------------------------------------------------
# File Name: player_analysis.py
# Author: Jai Verma
# Description: Analyse and extract some key stats from the data for a selected player.
#              These functions will be used by the Player Analysis page to display these stats for the
#              player selected by the user.
# -------------------------------------------------------------------------------------------------------


# Importing the required libraries
from re import S
import pandas as pd

# importing read_data from utils to read the data from the parquet files.
from utils.read_data import matches, deliveries    


batsman_scores = deliveries.groupby(['match_id', 'inning', 'over', 'batter'])['batsman_runs'].sum().reset_index()


#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#

# There is no categorization of a player as a batter or bower explicitly, neither is there any table that has those details.
# This would mean that the players page would look the same for both bowlers and batters.
# The bowling and batting both stats have to be displayed for each of them.

def total_matches_played(player_name: str) -> int:
    # An obvious shortcoming of this function is if the player has not contributed in any fielding, bowling, batting, or on non-striker
    # then the code will not be able to find the players name anywhere
    # A fix for this could have been the playing XI players list but it is not available in this dataset.

    '''
    The function takes player name as input and returns the total number of matches played by them.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of matches played by the selected player.
    '''
    return deliveries[
        (deliveries.batter == player_name) | (deliveries.bowler == player_name) | 
        (deliveries.fielder == player_name) | (deliveries.non_striker == player_name)
        ]['match_id'].nunique()


def runs_scored(player_name: str) -> int:
    '''
    The function takes player name as input and returns the total runs scored by them.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of runs scored by the selected player.
    '''
    return deliveries.loc[deliveries.batter == player_name, 'batsman_runs'].sum()


def wickets_taken(player_name: str) -> int:
    '''
    The function takes player name as input and returns the total number of wickets taken by them.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of wickets taken by the selected player.
    '''
    return deliveries.loc[deliveries.bowler == player_name,'is_wicket'].sum()


def highest_individual_score(player_name: str) -> int:
    '''
    The function takes player name as input and returns their highest individual score.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Highest Individal Score of the batsman in an innings.
    '''
    return batsman_scores.loc[batsman_scores.batter == player_name, 'batsman_runs'].max()


def total_50s(player_name: str) -> int:
    '''
    The function takes player name as input and returns the total number of 50s scored by them.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of 50s scored by the selected player.
    '''
    return batsman_scores.loc[
         (batsman_scores.batter == player_name) & 
         (batsman_scores.batsman_runs >= 50) & 
         (batsman_scores.batsman_runs < 100), 
         'batsman_runs'].count()


def total_100s(player_name: str) -> int:
    '''
    The function takes player name as input and returns the total number of 100s scored by them.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of 100s scored by the selected player.
    '''
    return batsman_scores.loc[
         (batsman_scores.batter == player_name) & 
         (batsman_scores.batsman_runs >= 100),
         'batsman_runs'].count()


def potm_awards(player_name: str) -> int:
    '''
    The function takes player name as input and returns the total number of POTM awarded to them.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of POTM awards of the selected player.
    '''
    return matches.loc[matches.player_of_match == player_name]['player_of_match'].count()


def total_4s_hit(player_name: str) -> int:
    '''
    The function takes player name as input and returns the total number of 4s hit by the player.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of 4s hit by the selected player.
    '''
    return deliveries[(deliveries.batter == player_name) & (deliveries.batsman_runs == 4)].shape[0]


def total_6s_hit(player_name: str) -> int:
    '''
    The function takes player name as input and returns the total number 6s hit by the player.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of 6s hit by the selected player.
    '''
    return deliveries[(deliveries.batter == player_name) & (deliveries.batsman_runs == 6)].shape[0]


def batting_average(player_name: str) -> float:   
    # Formula: total runs scored / total dismissals

    '''
    The function takes player name as input and returns their batting average.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Batting Average of the selected player.
    '''
    number_of_dismissals = deliveries[(deliveries.player_dismissed == player_name)].shape[0]
    try:
        return round(runs_scored(player_name)/number_of_dismissals, 2)
    except ZeroDivisionError:
        return runs_scored(player_name)


def runs_conceded(player_name: str) -> int:
    # helping function only for the next few functions.
    # to return the total runs conceded by the bowler.
    return deliveries[(deliveries.bowler == player_name)]['total_runs'].sum()


def bowling_average(player_name: str) -> float:   
    # Formula: total runs conceded / total wickets taken
    '''
    ### Average runs conceded to take a wicket.
    The function takes player name as input and returns their bowling average.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Bowling Average of the selected player.
    '''
    number_of_wickets = wickets_taken(player_name)
    try:
        return round(runs_conceded(player_name) / number_of_wickets, 2)
    except ZeroDivisionError:
        return runs_conceded(player_name)

def strike_rate(player_name: str) -> float:   
    # Formula: (total runs scored / total balls faced) * 100
    '''
    ### Average number of runs a batter scores per 100 balls faced.
    The function takes player name as input and returns their strike rate.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Strike Rate of the selected player.
    '''
    return round((runs_scored(player_name)/deliveries[deliveries.batter == player_name].shape[0])*100, 2)


def runs_scored_in_powerplay(player_name: str) -> int:
    '''
    ### This demonstrates their hitting ability in the starting overs.
    The function takes player name as input and returns the total runs scored by them in the powerplay.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of runs scored by the selected player during the powerplay.
    '''

    return batsman_scores[(batsman_scores.batter == player_name) & (batsman_scores.over <6)]['batsman_runs'].sum()


def runs_scored_in_death_overs(player_name: str) -> int:
    '''
    ### This demonstrates their match finishing abilities.
    The function takes player name as input and returns the total runs scored by them in the death overs.

    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Total Number of runs scored by the selected player in the death overs.
    '''
    return batsman_scores[(batsman_scores.batter == player_name) & (batsman_scores.over >=16)]['batsman_runs'].sum()


def favorite_teams_to_score(player_name: str) -> pd.DataFrame:
    '''
    The function takes player name as input and returns the top 3 teams against which they have scored the most.
    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Top 3 teams against which the batter has the most runs.
    '''
    batsman_scores_2 = deliveries.groupby(['batter', 'bowling_team'])['batsman_runs'].sum().reset_index()
    favorites = batsman_scores_2[batsman_scores_2.batter == player_name].sort_values(by = 'batsman_runs', ascending=False).head(3)

    return favorites


def favorite_team_for_bowlers(player_name: str) -> pd.DataFrame:
    '''
    The function takes player name as input and returns the top 3 teams against which they have taken the most wickets.
    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Top 3 teams against which the bowler has the most wickets.
    '''
    bowling_teams = deliveries[deliveries.is_wicket == 1].groupby(['bowler', 'batting_team'])['is_wicket'].count().reset_index()
    favorites = bowling_teams.loc[bowling_teams.bowler == player_name].sort_values(by = 'is_wicket', ascending=False).head(3)

    return favorites


def most_successful_venue(player_name: str) -> tuple:
    '''
    The function takes player name as input and returns the venue in which they are the most successful.
    #### Parameter: 
    player_name (Name of the Player)

    #### Returns: 
    Venue in which the player has scored the most or has taken the most wickets.
    '''

    deliveries_with_venue = pd.merge(deliveries, matches[['id', 'venue']], 
                                 left_on='match_id', right_on='id', 
                                 how='left')
    
    # for runs
    runs_by_venue = deliveries_with_venue.groupby(['batter','venue'])['batsman_runs'].sum().reset_index()
    best_venue_for_runs = runs_by_venue.loc[runs_by_venue.batter == player_name].sort_values(by='batsman_runs', ascending=False).head(1)['venue']

    if len(best_venue_for_runs)>0:
        best_venue_for_runs = best_venue_for_runs.values[0].split(',')[0]
    else:
        best_venue_for_runs = None

    # for wickets
    wickets_by_venue = deliveries_with_venue.groupby(['bowler','venue'])['is_wicket'].count().reset_index()
    best_venue_for_wickets = wickets_by_venue.loc[wickets_by_venue.bowler == player_name].sort_values(by='is_wicket', ascending=False).head(1)['venue']
    
    if len(best_venue_for_wickets)>0:
        best_venue_for_wickets = best_venue_for_wickets.values[0].split(',')[0]
    else:
        best_venue_for_wickets = None

    return best_venue_for_runs, best_venue_for_wickets