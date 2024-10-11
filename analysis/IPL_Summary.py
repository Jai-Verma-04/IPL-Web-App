import os
import sys

current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

from utils import read_data

deliveries = read_data.deliveries_data()
matches = read_data.matches_data()

total_runs = deliveries.total_runs.sum()

total_balls = deliveries.shape[0]

total_wickets = deliveries.is_wicket.value_counts()[1]

total_seasons = len(matches.season.unique())

most_wickets_player = deliveries[(deliveries.is_wicket == 1)]['bowler'].value_counts().idxmax()
most_wickets = deliveries[(deliveries.is_wicket == 1)]['bowler'].value_counts().max()

bat_runs = deliveries.groupby('batter')['batsman_runs'].sum()
most_runs_player = bat_runs.idxmax()
most_runs = bat_runs.max()

most_catches_by = deliveries[deliveries.dismissal_kind == 'caught']['fielder'].value_counts().idxmax()
most_catches = deliveries[deliveries.dismissal_kind == 'caught']['fielder'].value_counts().max()

total_boundaries = deliveries[(deliveries.batsman_runs == 4) | (deliveries.batsman_runs == 6)]['batter'].count()

most6s_player = deliveries[deliveries.batsman_runs == 6]['batter'].value_counts().idxmax()
most6s = deliveries[deliveries.batsman_runs == 6]['batter'].value_counts().max()

most4s_player = deliveries[deliveries.batsman_runs == 4]['batter'].value_counts().idxmax()
most4s = deliveries[deliveries.batsman_runs == 4]['batter'].value_counts().max()

most_potm = matches['player_of_match'].value_counts().idxmax()
most_potm_times = matches['player_of_match'].value_counts().max()

highest_team_score_team = matches[matches.target_runs == max(matches.target_runs)]['team1'].values[0]
highest_team_score = max(matches.target_runs)


batsman_scores = deliveries.groupby(['match_id', 'inning', 'batter'])['batsman_runs'].sum().reset_index()
highest_individual_score = batsman_scores.batsman_runs.max()
highest_individual_score_batsman = batsman_scores[batsman_scores['batsman_runs'] == highest_individual_score]['batter'].values[0]

total50s = batsman_scores[(batsman_scores.batsman_runs >= 50) & (batsman_scores.batsman_runs <=99)]
most50s = total50s['batter'].value_counts().idxmax()
most50s_count = total50s['batter'].value_counts().max()

total100s = batsman_scores[(batsman_scores.batsman_runs >= 100)]
most100s = total100s['batter'].value_counts().idxmax()
most100s_count = total100s['batter'].value_counts().max()