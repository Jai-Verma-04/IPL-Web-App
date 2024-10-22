# -------------------------------------------------------------------------------------------------------
# File Name: venue_analysis.py
# Author: Jai Verma
# Description: Analyse and extract some key stats from the data for each venue.
#              These functions will be used by the Venue Analysis page to display these stats for the
#              venue selected by the user.
# Caution / Note: Some venues are repeated twice or thrice
#                 For example the Chinnaswamy Stadium has been repeated as:
#                 > M Chinnaswamy Stadium, M Chinnaswamy Stadium, Bengaluru, M.Chinnaswamy Stadium
#
# This needs to be fixed.
# -------------------------------------------------------------------------------------------------------


# Importing the required libraries
import pandas as pd

# importing read_data from utils to read the data from the parquet files.
from utils.read_data import matches, deliveries     

deliveries_with_venue = pd.merge(deliveries, matches[['id', 'venue']], 
                        left_on='match_id', right_on='id', 
                        how='left')

#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#

def total_matches_played(venue: str) -> int:
    return matches.venue.value_counts().loc[venue]


def highest_team_total(venue: str) -> tuple:
    team = matches.loc[matches.venue == venue, ['team1', 'target_runs']].nlargest(1, 'target_runs')['team1'].values[0]
    score = matches.loc[matches.venue == venue, ['team1', 'target_runs']].nlargest(1, 'target_runs')['target_runs'].values[0]

    return team, int(score)


def lowest_team_total(venue: str) -> tuple:
    team = matches.loc[matches.venue == venue, ['team1', 'target_runs']].nsmallest(1, 'target_runs')['team1'].values[0]
    score = matches.loc[matches.venue == venue, ['team1', 'target_runs']].nsmallest(1, 'target_runs')['target_runs'].values[0]

    return team, int(score)


def average_first_innings_score(venue: str) -> int:
    return int(matches[(matches.venue == venue)]['target_runs'].mean())


def win_percentage(venue: str) -> int:
    table = matches[(matches.venue == venue) & ((matches.result == 'runs')|(matches.result == 'wickets'))]['result'].value_counts(normalize=True).reset_index()
    table = table.replace(['wickets', 'runs'], ['bowl first', 'bat first'])
    table.columns = ['toss decision', 'win percentage']
    table['win percentage'] = table['win percentage'].apply(lambda x: f"{x*100:.2f} %")
    
    return table


def most_successful_team(venue: str) -> str:
    wins_by_team_at_venue = matches[matches.venue == venue]['winner'].value_counts().reset_index()
    wins_by_team_at_venue.columns = ['team', 'count']
    
    matches_played_at_venue = pd.concat([matches.team1, matches.team2])[matches.venue == venue].value_counts().reset_index()
    matches_played_at_venue.columns = ['team', 'count']

    merged = pd.merge(matches_played_at_venue, wins_by_team_at_venue, on='team')
    merged.columns = ['team', 'matches_played', 'matches_won']

    merged['win_percent'] = round((merged['matches_won']/merged['matches_played'])*100, 2)

    # atleast played more than the Q1 of the matches (because if someone has played only 1 match and 1, their win % would be 100%)

    win_percentages = merged[(merged.matches_played > merged.matches_played.quantile(0.25))][['team', 'win_percent']].sort_values(by='win_percent', ascending=False)

    most_successful_team = win_percentages.iloc[0].iloc[0]
    win_percentage = win_percentages.iloc[0].iloc[1]

    return most_successful_team, win_percentage


def most_runs(venue: str) -> tuple:
    batter = deliveries_with_venue[deliveries_with_venue.venue == venue].groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).idxmax()
    runs = deliveries_with_venue[deliveries_with_venue.venue == venue].groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).max()
    
    return batter, runs


def most_wickets(venue: str) -> int:
    bowler = deliveries_with_venue[(deliveries_with_venue.venue == venue) & (deliveries_with_venue.is_wicket == 1)]['bowler'].value_counts().idxmax()
    wickets = deliveries_with_venue[(deliveries_with_venue.venue == venue) & (deliveries_with_venue.is_wicket == 1)]['bowler'].value_counts().max()
    
    return bowler, wickets


def total_boundaries(venue: str) -> tuple:
    return deliveries_with_venue[(deliveries_with_venue.venue == venue) & ((deliveries_with_venue.batsman_runs == 4) | (deliveries_with_venue.batsman_runs == 6))].shape[0]


def toss_decision(venue) -> tuple:
    return matches[matches.venue == venue]['toss_decision'].value_counts().reset_index()

