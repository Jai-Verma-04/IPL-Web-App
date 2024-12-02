import streamlit as st

from utils.data import SEASONS, TEAMS

from analysis.scorecard_analysis import *

team_1 = st.selectbox('Choose a team: ', TEAMS, key = 'team_1')
team_2 = st.selectbox('Choose a team: ', [team for team in TEAMS if team!=team_1], key = 'team_2')
season = st.selectbox('Choose a season', SEASONS, key='season')

matches_list = display_matches(team_1, team_2, season)

if len(matches_list)==0:
    st.write("No matches available for the selected combination")
    st.stop()
else:
    st.table(matches_list)

match_id = st.selectbox("Choose Match ID: ", matches_list['id'], key='match_id')


a=MatchInfo(match_id)

st.write(a.match_name)
st.write(a.match_date)
st.write(f"{a.toss[0]} won the toss and opt to {a.toss[1]}")
st.write(f"{a.umpires[0]} and {a.umpires[1]}")
st.write(f"{a.venue[0].split(',')[0].strip()}, {a.venue[1]}")
st.write(a.result)
st.write(a.potm)

inning_1, inning_2 = st.tabs(["First Innings", "Second Innings"])


with inning_1:
    inning = 1
    
    batting, bowling = st.tabs(['batting', 'bowling'])
    
    with batting:
        score=ScoreCard(match_id, inning=inning)
    
        st.write(score.batting_data)
        st.write(score.key_batter)
        st.write(score.batting_summary)
        st.image(f"static/players/{score.key_batter}.png")

    with bowling:
        st.write(score.bowler_data)
        st.write(score.key_bowler)
        st.write(score.fall_of_wickets)
        st.image(f"static/players/{score.key_bowler}.png")


with inning_2:
    inning = 2
    
    batting, bowling = st.tabs(['batting', 'bowling'])
    
    with batting:
        score=ScoreCard(match_id, inning=inning)
    
        st.write(score.batting_data)
        st.write(score.key_batter)
        st.write(score.batting_summary)
        st.image(f"static/players/{score.key_batter}.png")

    with bowling:
        st.write(score.bowler_data)
        st.write(score.key_bowler)
        st.write(score.fall_of_wickets)
        st.image(f"static/players/{score.key_bowler}.png")
    
