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


def display_matches(team_1: str, team_2: str, season: int) -> pd.DataFrame:
    '''
    The function takes team names and season as input and returns a dataframe with \
        details of the matches played between the two teams in the selected season.

    #### Parameter: 
    Team_1 (Selected Team)
    Team_2 (Selected Team)
    Season (Selected Season)

    #### Returns: 
    pd.DataFrame: Matches played between the two selected teams in the selected season.
    '''

    # List all the matches that have team1 == team_1, team2 == team_2 and season == season parameters passed through the function.
    matches_list = matches[
                        (
                            matches[['team1', 'team2', 'season']].isin([team_1, team_2, season])
                        ).all(axis=1)
                    ]
    
    del matches_list['Unnamed: 0']              # Delete the Unnamed: 0 column from the dataframe
    
    return matches_list[['id','match_type', 'winner', 'date', 'season', 'city', 'venue', 'team1', 'team2']]


class MatchInfo:
    '''
    Contains functions (properties) to return match summary using match_id of the selected match.
    '''

    def __init__(self, match_id) -> object:
        '''
        Initialize match_id parameter and a dataframe filtered on the match_id.
        '''
        self.match_id = match_id              # initialize the match_id variable
        self.match_df = matches[matches.id == self.match_id]        # Filter matches based on the match id

    
    @property
    def match_name(self) -> str:
        '''
        Returns match name for the selected match id.
        '''
        match_name = f"{self.match_df['team1'].values[0]} vs {self.match_df['team2'].values[0]}"
        return match_name


    @property
    def match_date(self) -> str:
        '''
        Returns the date on which the selected match was played
        '''
        match_date = self.match_df['date'].values[0]
        return match_date
    

    @property
    def toss(self) -> tuple:
        '''
        Returns a tuple containing the toss winner and the toss decision from the selected match_id as a tuple.

        Returns:
        tuple: (Toss Winner, Toss Decision)
        '''
        toss_winner = self.match_df['toss_winner'].values[0]
        toss_decision = self.match_df['toss_decision'].values[0]

        return toss_winner, toss_decision
    

    @property
    def venue(self) -> tuple:
        '''
        Returns the stadium (venue) and city in which the selected match was played.

        Returns:
        tuple : (Stadium, City)
        '''
        stadium = self.match_df['venue'].values[0]
        city = self.match_df['city'].values[0]

        return stadium, city
    

    @property
    def umpires(self) -> tuple:
        '''
        Returns the names of the two on-field umpires of the selected game.

        Returns:
        tuple: (Name of umpire 1, Name of umpire 2)
        '''

        umpire1 = self.match_df['umpire1'].values[0]
        umpire2 = self.match_df['umpire2'].values[0]

        return umpire1, umpire2
    

    @property
    def result(self) -> str:
        '''
        Returns the result of the selected match.

        Possible values - 
        1. Win (By wicket)
        2. Win (By runs)
        3. Tie
        4. No result
        '''
        
        team = self.match_df['winner'].values[0]
        result_margin = self.match_df['result_margin'].values[0]
        results = self.match_df['result'].values[0]

        # If the team won by runs or wickets, display the victory margin also, 
        # otherwise display tie/no result for the matches with no result.

        if results in ('runs', 'wickets'):
            return f"{team} won by {int(result_margin)} {results}"
        else:
            return results
        

    @property
    def potm(self) -> str:
        '''
        Returns the player of the match of the selected match.
        '''
        return self.match_df['player_of_match'].values[0]    


class ScoreCard:
    '''
    Contains functions (properties) that will be used to generate the batting / bowling card for both the innings of the selected match.
    '''

    def __init__(self, match_id, inning):
        '''
        Initialize a variable for match_id.
        Initialize a dataframe filtered on the match id and the innings.
        '''
        self.match_id = match_id
        
        self.inning_df = deliveries[(deliveries.match_id == match_id) & (deliveries.inning==inning)]   # Filter matches based on match_id and inning number
        del self.inning_df['Unnamed: 0']        # Delete the Unnamed: 0 column from the dataframe

# -------------------------------------------------------------------------------------------------------------------------------       
#                                                BATTING SCORECARD                                                              #
# -------------------------------------------------------------------------------------------------------------------------------       
    @property 
    def batters(self) -> list:
        '''
        Returns the list of batters that played in the innings for the selected match.

        Note: Batsman includes players who were present on the ground as a striker / non-striker even if they have not played any balls.
        '''
        batters = pd.concat([self.inning_df['batter'], self.inning_df['non_striker']]).unique()
        return batters
    
    
    @property
    def batting_data(self) -> pd.DataFrame:
        '''
        Generate a dataframe of batting for the selected innings.

        Returns a dataframe which has the following columns:
        1. Batter
        2. Dismissal type and fielder
        3. Bowler
        4. Batsman Score
        5. Balls faced
        6. Total 4s hit
        7. Total 6s hit
        8. Batter Strike Rate

        '''
        # Initialize a dataframe with the requisite column names.
        scorecard_df = pd.DataFrame(columns=['batter', 'dismissal', 'bowler', 'score', 'balls', 'batter_4s', 'batter_6s', 'strike_rate'])

        for batter in self.batters:             # for each batter in the list of unique batters (from the self.batters property)
            # Batsman Score: Sum of the runs hit by the batsman.
            score = self.inning_df[self.inning_df['batter'] == batter]['batsman_runs'].sum()

            # balls faced by the batter: count of dataframe rows where batter was on the strikers end.
            balls = self.inning_df[(self.inning_df['batter'] == batter) & (self.inning_df['extras_type'] != 'wides')].shape[0]

            # 4s hit by the batter: count the rows where batsman_runs == 4
            batter_4s = self.inning_df[(self.inning_df['batter'] == batter) & (self.inning_df['batsman_runs'] == 4)].shape[0]

            # 6s hit by the batter: count the rows where batsman_runs == 6
            batter_6s = self.inning_df[(self.inning_df['batter'] == batter) & (self.inning_df['batsman_runs'] == 6)].shape[0]

            # Batter Strike Rate: The number of runs scored per 100 balls faced. [Higher is better]
            if balls != 0:
                strike_rate = score/balls * 100
            # if the batter has not faced any balls, the strike rate will be zero
            else:       
                strike_rate = 0

            # A dataframe for finding dismissal of the batter
            dismissal_data = self.inning_df[
                                (self.inning_df['player_dismissed'] == batter) & (self.inning_df['is_wicket'] == 1)
                            ]
            
            # If batsman was dismissed
            if not dismissal_data.empty:
                # How was the batter dismissed?
                dismissal = dismissal_data['dismissal_kind'].iloc[0]
                
                # Change how the dismissals show in the dataframe.
                dismissal_mapping = {
                    'caught': 'c',
                    'bowled': '',
                    'stumped': 'st',
                    'caught and bowled': 'c&b',
                }
                
                # Which fielder dismissed the batter?
                fielder = dismissal_data['fielder'].iloc[0]
                
                # map the dismissal to the dismissal mapping.
                dismissal = dismissal_mapping.get(dismissal, dismissal)
                
                # find the bowler who was bowling to the current batter when he was dismissed.
                bowler_name = dismissal_data['bowler'].iloc[0]
                
                # If no fielder is there replace None with empty string
                if fielder == None:
                    fielder = ''
                
                # If batter is dismissed by lbw, show the dismissal as empty and add prefix 'lbw' in front of the bowler's name.
                if dismissal == 'lbw':
                    bowler = f"lbw {bowler_name}"
                    dismissal = ''

                # If batter is dismissed by caught and bowled, show dismissal as empty and add prefix 'c&b' in front of the bowler's name.
                elif dismissal == 'c&b':
                    bowler = f"c&b {bowler_name}"
                    dismissal = ''
                
                # IF batter is dismissed by run out, display the fielder name as (fielder)
                elif dismissal == 'run out':
                    bowler = f"b {bowler_name}"
                    fielder = f"({fielder})"
                # otherwise show bowler as: 'b (bowler name)' indicating the bowler name when the wicket was taken.
                else:
                    bowler = f"b {bowler_name}"

            # Batsman was not dismissed (not out)
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
            
            # Remove NA Values before concatenation
            scorecard_df = scorecard_df.dropna(axis=1, how='all')
            temp_df = temp_df.dropna(axis=1, how='all')
            
            # Concatenate the temporary DataFrame with the main DataFrame
            scorecard_df = pd.concat([scorecard_df, temp_df], ignore_index=True)

        return scorecard_df


    @property
    def key_batter(self) -> str:
        '''
        Returns the name of a key batter from the selected innings.

        Key batter - Batter who has scored the most runs in that innings.
        '''
        
        # find name of the batter from the 'batter column' who has the highest score. 
        key_batter = self.batting_data.loc[self.batting_data['score'].idxmax(), 'batter']

        return key_batter


    @property
    def batting_summary(self) -> tuple:
        '''
        Returns a summary of the batting innings.

        Summary include:
        1. Overs played
        2. Total Runs
        3. Total Wickets
        4. Run rate
        5. Extras
        '''
        # total runs: sum of the total runs made in the inning.
        total_runs = self.inning_df['total_runs'].sum()

        # Total wickets: count of the wickets taken in the inning.
        wickets = self.inning_df[self.inning_df['is_wicket'] == 1]['is_wicket'].count()

        # To calculate the number of overs
        max_over = self.inning_df['over'].max()

        # to check if an over is bowler partially
        correction_Factor = self.inning_df[(self.inning_df['over'] == max_over) & (self.inning_df['extras_type'] != 'wides')].shape[0]/6

        # if an over is bowled partially, its CF would be less than 1 and that would be added to the no_of_overs
        if correction_Factor < 1:
            no_of_overs = max_over + correction_Factor
        else:
            no_of_overs = max_over+1

        # We calculated the no_of_overs in the above way so as to calculate the run rate correctly.
        run_rate = round(total_runs / no_of_overs, 2)

        # map extras_type to display accordingly.
        extras_mapping = {
            'legbyes' : 'LB',
            'wides' : 'W',
            'byes' : 'B',
            'noballs' : 'NB',
            'penalty' : 'penalty'
        }

        self.inning_df.loc[:, 'extras_type'] = self.inning_df['extras_type'].map(extras_mapping)
        
        # TODO: Runs conceded on the byes and legbyes are not added properly
        #Find the total runs conceded by extras and number of extras given by the bowling team.
        extras = self.inning_df['extras_type'].value_counts().to_dict()
        extras_total_runs = sum(extras.values())

        return f"{int(no_of_overs)}.{int((no_of_overs * 6) % 6)}", total_runs, wickets, run_rate, extras_total_runs, extras
    
# ------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------
#                                               BOWLING SCORECARD                                                        #
# ------------------------------------------------------------------------------------------------------------------------

    @property
    def bowlers(self) -> list:
        '''
        Returns a list of al the bowlers that bowled in the match.
        '''
        bowlers = self.inning_df['bowler'].unique()
        return bowlers

    @property
    def bowler_data(self) -> pd.DataFrame:
        '''
        Generates a dataframe for the bowling data of the selected innings.

        Returns a dataframe with the following column names:
        1. Bowler name
        2. Overs Bowled
        3. Dot balls bowled
        4. Runs conceded
        5.Wickets taken
        6.Bowling economy
        '''


        #create a dataframe for bowlers.
        bowler_df = pd.DataFrame(columns=['bowler', 'overs', 'dot balls', 'runs', 'wickets', 'economy'])

        # for each bowler in the match
        for bowler in self.bowlers:

            # Calculate the number of balls bowled by each bowler in which the bowler has not given "wides"
            balls = self.inning_df[(self.inning_df['bowler'] == bowler) & (self.inning_df['extras_type'] != 'W')]
            overs = balls.shape[0] // 6  # Integer division to get the number of complete overs
            remaining_balls = balls.shape[0] % 6  # Remainder to get the number of balls left
            
            #Displays the overs bowled as overs.balls  (Ex 4.2 overs)
            overs_bowled = f"{overs}.{remaining_balls}"
            
            # Calculating the dot balls bowled by the bowler
            dots = balls[balls['batsman_runs'] == 0].shape[0]

            # TODO: runs from Byes and legbyes are not added to the bowlers runs.
            # calculate the total runs conceded by the bowler
            runs = self.inning_df[(self.inning_df['bowler'] == bowler)]['total_runs'].sum()
            
            # Calculate the total wickets taken by the bowler
            wickets = self.inning_df[(self.inning_df['bowler'] == bowler) & (self.inning_df['is_wicket'] == 1) & (self.inning_df['dismissal_kind'] != 'run out')]['is_wicket'].count()
            
            # Calculates the bowling economy: Runs conceded / Overs bowled by the bowler.
            economy = runs/(overs+(remaining_balls/6))

            # Create a temporary DataFrame for the current batter's data
            temp_df = pd.DataFrame({
                'bowler': [bowler],
                'overs': [overs_bowled],
                'dot balls': [dots],
                'runs': [runs],
                'wickets' :[wickets],
                'economy': [economy],
            })
            
            #Removes any Null values to concatenate the dataframe without any errors.
            bowler_df = bowler_df.dropna(axis=1, how='all')
            temp_df = temp_df.dropna(axis=1, how = 'all')

            # Concatenate the temporary DataFrame with the main DataFrame
            bowler_df = pd.concat([bowler_df, temp_df], ignore_index=True)

        return bowler_df
    

    @property
    def key_bowler(self) -> str:
        '''
        Returns the name of the bowler with the highest wickets in the innings.
        '''
        key_bowler = self.bowler_data.loc[self.bowler_data['wickets'].idxmax(), 'bowler']

        return key_bowler
    

    @property
    def fall_of_wickets(self) -> pd.DataFrame:
        '''
        Dataframe: Fall of Wickets.
        Returns a dataframe with the columns as wicket number and the score at which the wicket was taken
        '''
        # Calculate cumulative runs at each ball
        cumulative_runs = self.inning_df['total_runs'].cumsum().reset_index(drop=True)
        wickets_column = self.inning_df.loc[:, 'is_wicket'].reset_index(drop=True)

        df = pd.concat([cumulative_runs, wickets_column], axis=1)
        wickets = df[df['is_wicket'] == 1]

        # Creates a dataframe with columns 'Wickets' and 'Runs'
        fow = pd.DataFrame({
        'wicket': range(1, len(wickets) + 1),
        'runs': wickets['total_runs'].reset_index(drop=True)
        })
        
        return fow