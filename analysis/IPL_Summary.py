# -------------------------------------------------------------------------------------------------------
# File Name: IPL._Summary.py
# Author: Jai Verma
# Description: Calculates the complete summary of IPL..
#              These functions will be used by the IPL. Summary page to display these stats for the team 
#              selected by the user.
# -------------------------------------------------------------------------------------------------------


# importing read_data from utils to read the data from the parquet files
from utils.read_data import matches, deliveries

# batsman scores for each match and inning
batsman_scores = deliveries.groupby(['match_id', 'inning', 'batter'])['batsman_runs'].sum().reset_index()


#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#


def get_total_runs() -> int:
    '''
    #### Returns:
    Total runs scored.
    '''
    return deliveries.total_runs.sum()
    

def get_total_balls() -> int:
    '''
    #### Returns:
    Total balls bowled.
    '''
    return deliveries.shape[0]


def get_total_wickets() -> int:
    '''
    #### Returns:
    Total wickets taken.
    '''
    return deliveries.is_wicket.value_counts()[1]


def get_total_seasons() -> int:
    '''
    #### Returns:
    Total number of seasons.
    '''
    return len(matches.season.unique())


def get_total_boundaries() -> int:
    '''
    #### Returns:
    Total boundaries hit.
    '''
    return deliveries[(deliveries.batsman_runs == 4) | (deliveries.batsman_runs == 6)]['batter'].count()


def get_most_wickets() -> tuple:
    '''
    #### Returns:
    tuple: (Player with the most wickets, Number of Wickets)
    '''
    most_wickets_player = deliveries[(deliveries.is_wicket == 1)]['bowler'].value_counts().idxmax()
    most_wickets = deliveries[(deliveries.is_wicket == 1)]['bowler'].value_counts().max()
    return most_wickets_player, most_wickets


def get_most_runs() -> tuple:
    '''
    #### Returns:
    tuple: (Player with most runs, Runs)
    '''
    bat_runs = deliveries.groupby('batter')['batsman_runs'].sum()
    most_runs_player = bat_runs.idxmax()
    most_runs = bat_runs.max()
    return most_runs_player, most_runs


def get_most_catches() -> tuple:
    '''
    #### Returns:
    tuple: (Player with most catches, number of catches)
    '''
    most_catches_by = deliveries[deliveries['dismissal_kind'] == 'caught']['fielder'].value_counts().idxmax()
    most_catches = deliveries[deliveries['dismissal_kind'] == 'caught']['fielder'].value_counts().max()
    return most_catches_by, most_catches


def get_most_6s() -> tuple:
    '''
    #### Returns:
    tuple: (Player with most 6s, Number of 6s hit)
    '''
    most6s_player = deliveries[deliveries.batsman_runs == 6]['batter'].value_counts().idxmax()
    most6s = deliveries[deliveries.batsman_runs == 6]['batter'].value_counts().max()
    return most6s_player, most6s


def get_most_4s() -> tuple:
    '''
    #### Returns:
    tuple: (Player with most 4s, Number of 4s hit)
    '''
    most4s_player = deliveries[deliveries.batsman_runs == 4]['batter'].value_counts().idxmax()
    most4s = deliveries[deliveries.batsman_runs == 4]['batter'].value_counts().max()
    return most4s_player, most4s


def get_most_potm() -> tuple:
    '''
    #### Returns:
    tuple: (Player with most POTM [player of the match] awards, Number of Awards)
    '''
    most_potm = matches['player_of_match'].value_counts().idxmax()
    most_potm_times = matches['player_of_match'].value_counts().max()
    return most_potm, most_potm_times


def get_highest_team_score() -> tuple:
    '''
    #### Returns:
    tuple: (team name, highest score)
    '''
    highest_team_score_team = matches[matches.target_runs == max(matches.target_runs)]['team1'].values[0]
    highest_team_score = max(matches.target_runs)
    return highest_team_score_team, highest_team_score


def get_highest_individual_score() -> tuple:
    '''
    #### Returns:
    tuple: (Player Name, Highest individual score)
    '''
    highest_individual_score = batsman_scores.batsman_runs.max()
    highest_individual_score_batsman = batsman_scores[batsman_scores['batsman_runs'] == highest_individual_score]['batter'].values[0]
    return highest_individual_score_batsman, highest_individual_score


def get_most_50s() -> tuple:
    '''
    #### Returns:
    tuple: (Player Name, Number of 50+ scores)
    '''
    total50s = batsman_scores[(batsman_scores.batsman_runs >= 50) & (batsman_scores.batsman_runs <=99)]
    most50s = total50s['batter'].value_counts().idxmax()
    most50s_count = total50s['batter'].value_counts().max()
    return most50s, most50s_count


def get_most_100s() -> tuple:
    '''
    #### Returns:
    tuple: (Player Name, Number of 100+ scores)
    '''
    total100s = batsman_scores[(batsman_scores.batsman_runs >= 100)]
    most100s = total100s['batter'].value_counts().idxmax()
    most100s_count = total100s['batter'].value_counts().max()
    return most100s, most100s_count