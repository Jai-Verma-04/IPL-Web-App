from functools import lru_cache
import os
import sys
import pandas as pd
import streamlit as st


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

from utils import read_data

deliveries = read_data.deliveries_data()
matches = read_data.matches_data()


def number_of_matches_played(team):
    return matches[(matches.team1 == team) | (matches.team2 == team)]['id'].nunique()


def match_won(team):
    return matches.winner.value_counts().loc[team]

def win_percentage(team):
    return round(match_won(team)/number_of_matches_played(team) * 100, 2)


def most_wins(team):
    # Calculate the crosstab once and reuse it
    crosstab_result = pd.crosstab(matches.team1, matches.team2)

    # Create a DataFrame with the team having the most wins and the number of wins
    most_wins_against_teams = pd.DataFrame({
        'Against the team ': crosstab_result.idxmax(axis=1),
        'Number of Wins': crosstab_result.max(axis=1),
    })

    return most_wins_against_teams.loc[team]

def matches_per_season(team):
    return matches[(matches.team1 == team) | (matches.team2 == team)]['season'].value_counts().sort_index().reset_index()
    

def most_matches_won_at_venue(team):
    return matches[(matches.winner == team)]['venue'].value_counts().idxmax(), matches[(matches.winner == team)]['venue'].value_counts().max()


def num_of_trophies(team):
    return matches[matches.match_type == 'Final']['winner'].value_counts().loc[team]

def match_and_toss(team):
    lu = matches[(matches.toss_winner == team) & (matches.winner == team)].count().values[0]
    ll = matches[(matches.toss_winner == team) & (matches.winner != team)].count().values[0]
    ru = matches[(matches.toss_winner != team) & (matches.winner == team)].count().values[0]
    rl = number_of_matches_played(team) - match_won(team)-ll
    
    return pd.DataFrame([[lu, ru, lu+ru], [ll, rl, ll+rl], [lu+ll, ru+rl, lu+ll+ru+rl]], columns=(['Tosses Won', 'Tosses Lost', 'Total']), index=['Matches Won', 'Matches Lost', 'Total'])


def highest_team_score(team):
    filtered_matches = matches[matches.team1 == team]

    # Find the index of the maximum target_runs
    max_index = filtered_matches['target_runs'].idxmax()

    # Extract the corresponding team2 and target_runs
    team2 = filtered_matches.loc[max_index, 'team2']
    target_runs = filtered_matches.loc[max_index, 'target_runs']

    return team2, target_runs

def total6s(team):
    return deliveries[(deliveries.batting_team == team)  & (deliveries.batsman_runs == 6)].shape[0]

def total4s(team):
    return deliveries[(deliveries.batting_team == team)  & (deliveries.batsman_runs == 4)].shape[0]

def top3scorers(team):
    batting_data = deliveries[deliveries.batting_team == team]
    top_scorers = batting_data.groupby('batter')['batsman_runs'].sum().reset_index().sort_values(by='batsman_runs', ascending=False).head(3)
    
    return top_scorers

def top3wicket_takers(team):
    bowling_data = deliveries[(deliveries['bowling_team'] == team) & (deliveries['is_wicket'] == 1)]
    top_wicket_takers = bowling_data.groupby('bowler')['player_dismissed'].count().reset_index().sort_values(by='player_dismissed', ascending=False).head(3)

    return top_wicket_takers


def avg_powerplay_score(team):
    team_powerplay_data = deliveries[(deliveries['batting_team'] == team) & (deliveries['over'] <= 5)]
    avg_powerplay_score = round(team_powerplay_data.groupby('match_id')['total_runs'].sum().reset_index().mean().values[1])

    return avg_powerplay_score