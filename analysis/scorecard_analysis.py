# -------------------------------------------------------------------------------------------------------
# File Name: generate_scorecard.py
# Author: Jai Verma
# Description: Generate Scorecard for a particular match from the IPL.
#              These functions will be used by the Generate Scorecard page to display the scorecard for the 
#              teams / match selected by the user.
# -------------------------------------------------------------------------------------------------------


# Importing the required libraries
import pandas as pd

# importing read_data from utils to read the data from the parquet files.
from utils.read_data import matches, deliveries    


#-------------------------------------------------------------------------------------#
#                             |  FUNCTIONS    |                                       #
#-------------------------------------------------------------------------------------#


def display_matches(team_1, team_2, season):

    matches_list = matches[
                    (
                        matches[['team1', 'team2', 'season']].isin([team_1, team_2, season])
                    ).all(axis=1)]
    del matches_list['Unnamed: 0']
    
    return matches_list[['id','match_type', 'winner', 'date', 'season', 'city', 'venue', 'team1', 'team2']]

class MatchInfo:
    
    def __init__(self, match_id):
        self.match_id = match_id
        self.match_df = matches[matches.id == self.match_id]

    
    @property
    def match_name(self):
        match_name = f"{self.match_df['team1'].values[0]} vs {self.match_df['team2'].values[0]}"
        return match_name

    @property
    def match_date(self):
        match_date = self.match_df['date'].values[0]
        return match_date
    
    @property
    def toss(self):
        toss_winner = self.match_df['toss_winner'].values[0]
        toss_decision = self.match_df['toss_decision'].values[0]

        return toss_winner, toss_decision
    
    @property
    def venue(self):
        stadium = self.match_df['venue'].values[0]
        city = self.match_df['city'].values[0]

        return stadium, city
    
    @property
    def umpires(self):
        umpire1 = self.match_df['umpire1'].values[0]
        umpire2 = self.match_df['umpire2'].values[0]

        return umpire1, umpire2
    
    @property
    def result(self):
        team = self.match_df['winner'].values[0]
        result_margin = self.match_df['result_margin'].values[0]
        results = self.match_df['result'].values[0]

        if results in ('runs', 'wickets'):
            return f"{team} won by {int(result_margin)} {results}"
        else:
            return results
        
    @property
    def potm(self):
        return self.match_df['player_of_match'].values[0]    


class ScoreCard:

    def __init__(self, match_id, inning):
        self.match_id = match_id
        
        self.inning_df = deliveries[(deliveries.match_id == match_id) & (deliveries.inning==inning)]
        del self.inning_df['Unnamed: 0']

# -------------------------------------------------------------------------------------------------------------------------------       
#                                                BATTING SCORECARD                                                              #
# -------------------------------------------------------------------------------------------------------------------------------       
    @property 
    def batters(self):
        batters = pd.concat([self.inning_df['batter'], self.inning_df['non_striker']]).unique()
        return batters
    
    
    @property
    def scorecard_data(self):
        scorecard_df = pd.DataFrame(columns=['batter', 'dismissal', 'bowler', 'score'])

        for batter in self.batters:
            score = self.inning_df[self.inning_df['batter'] == batter]['batsman_runs'].sum()
            balls = self.inning_df[self.inning_df['batter'] == batter].shape[0]
            batter_4s = self.inning_df[(self.inning_df['batter'] == batter) & (self.inning_df['batsman_runs'] == 4)].shape[0]
            batter_6s = self.inning_df[(self.inning_df['batter'] == batter) & (self.inning_df['batsman_runs'] == 6)].shape[0]
            strike_rate = score/balls * 100
            dismissal_data = self.inning_df[(self.inning_df['batter'] == batter) & (self.inning_df['is_wicket'] == 1)]
            
            if not dismissal_data.empty:
                dismissal = dismissal_data['dismissal_kind'].iloc[0]
                
                dismissal_mapping = {
                    'caught': 'c',
                    'bowled': '',
                    'stumped': 'st',
                    'caught and bowled': 'c&b',
                }
                
                fielder = dismissal_data['fielder'].iloc[0]
                
                dismissal = dismissal_mapping.get(dismissal, dismissal)
                
                if fielder == None:
                    fielder = ''
                    
                if dismissal == 'lbw':
                    bowler = f"lbw {dismissal_data['bowler'].iloc[0]}"
                    dismissal = ''
                elif dismissal == 'c&b':
                    bowler = f"c&b {dismissal_data['bowler'].iloc[0]}"
                    dismissal = ''
                else:
                    bowler = f"b {dismissal_data['bowler'].iloc[0]}"

            else:
                dismissal = 'Not out'
                fielder = ''
                bowler = ''
            
            # Create a temporary DataFrame for the current batter's data
            temp_df = pd.DataFrame({
                'batter': [batter],
                'dismissal': [dismissal+' '+fielder],
                'bowler': [bowler],
                'score': [score],
                'balls' :[balls],
                'batter_4s': [batter_4s],
                'batter_6s': [batter_6s],
                'strike_rate' :[strike_rate]
            })
            
            # Concatenate the temporary DataFrame with the main DataFrame
            scorecard_df = pd.concat([scorecard_df, temp_df], ignore_index=True)

        return scorecard_df

    @property
    def key_batter(self):
        highest_score = self.scorecard_data['score'].max()
        key_batter = self.scorecard_data.loc[self.scorecard_data['score'] == highest_score, 'batter'].values[0]
        return key_batter


    @property
    def batting_summary(self):
        total_runs = self.inning_df['total_runs'].sum()
        wickets = self.inning_df[self.inning_df['is_wicket'] == 1]['is_wicket'].count()
        max_over = self.inning_df['over'].max()
        correction_Factor = self.inning_df[self.inning_df['over'] == self.inning_df['over'].max()].shape[0]/6

        if correction_Factor < 1:
            no_of_overs = max_over + correction_Factor
        else:
            no_of_overs = max_over+1

        run_rate = round(total_runs / no_of_overs, 2)

        extras_mapping = {
            'legbyes' : 'LB',
            'wides' : 'W',
            'byes' : 'B',
            'noballs' : 'NB',
            'penalty' : 'penalty'
        }
        self.inning_df.loc[:, 'extras_type'] = self.inning_df['extras_type'].map(extras_mapping)
        
        extras = self.inning_df['extras_type'].value_counts().to_dict()
        extras_total_runs = sum(extras.values())

        return no_of_overs, total_runs, wickets, run_rate, extras_total_runs, extras
    
# ------------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------------
#                                               BOWLING SCORECARD                                                        #
# ------------------------------------------------------------------------------------------------------------------------

    @property
    def bowlers(self):
        bowlers = self.inning_df['bowler'].unique()
        return bowlers

    @property
    def bowler_data(self):
        bowler_df = pd.DataFrame(columns=['bowler', 'overs', 'dot balls', 'runs', 'wickets', 'economy'])

        for bowler in self.bowlers:
            balls = self.inning_df[(self.inning_df['bowler'] == bowler)]['over'].count()
            overs = balls//6

            dots = self.inning_df[(self.inning_df['bowler'] == bowler) & (self.inning_df['batsman_runs'] == 0)].shape[0]
            runs = self.inning_df[(self.inning_df['bowler'] == bowler)]['total_runs'].sum()
            wickets = self.inning_df[(self.inning_df['bowler'] == bowler) & (self.inning_df['is_wicket'] == 1)]['is_wicket'].count()
            economy = runs/overs
            # Create a temporary DataFrame for the current batter's data
            temp_df = pd.DataFrame({
                'bowler': [bowler],
                'overs': [overs],
                'dot balls': [dots],
                'runs': [runs],
                'wickets' :[wickets],
                'economy': [economy],
            })
            
            # Concatenate the temporary DataFrame with the main DataFrame
            bowler_df = pd.concat([bowler_df, temp_df], ignore_index=True)

        return bowler_df
    
    @property
    def key_bowler(self):
        most_wickets = self.bowler_data['wickets'].max()
        key_bowler = self.bowler_data.loc[self.bowler_data['wickets'] == most_wickets, 'bowler'].values[0]

        return key_bowler
    

    @property
    def fall_of_wickets(self):

        cumulative_runs = self.inning_df['total_runs'].cumsum().reset_index(drop=True)
        wickets_column = self.inning_df.loc[:, 'is_wicket'].reset_index(drop=True)
    
        df = pd.concat([cumulative_runs, wickets_column], axis=1)
        wickets = df[df['is_wicket'] == 1]

        fow = pd.DataFrame({
        'wicket': range(1, len(wickets) + 1),
        'runs': wickets['total_runs'].reset_index(drop=True)
        })
        
        return fow