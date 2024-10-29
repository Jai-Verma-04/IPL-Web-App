from re import Match
import streamlit as st


from utils.data import SEASONS, TEAMS

from analysis.scorecard_analysis import *


team_1 = st.selectbox('Choose a team: ', TEAMS, key = 'team_1')
team_2 = st.selectbox('Choose a team: ', TEAMS, key = 'team_2')
season = st.selectbox('Choose a season', SEASONS)

matches_list = display_matches(team_1, team_2, season)
st.write(matches_list)

match_id = st.selectbox("Choose Match ID: ", matches_list['id'])


a=MatchInfo(match_id)

st.write(a.match_name)
st.write(a.match_date)
st.write(f"{a.toss[0]} won the toss and opt to {a.toss[1]}")
st.write(f"{a.umpires[0]} and {a.umpires[1]}")
st.write(f"{a.venue[0]}, {a.venue[1]}")

expand = st.expander("My label", icon=":material/info:")

with expand:
    st.radio("Select one:", [1, 2])


inning_1, inning_2 = st.tabs(["First Innings", "Second Innings"])

b=ScoreCard(match_id)

with inning_1:
    inning = 1
    st.write(b.bowling_card(inning))

with inning_2:
    inning = 2
    st.write(b.batting_card(inning))

