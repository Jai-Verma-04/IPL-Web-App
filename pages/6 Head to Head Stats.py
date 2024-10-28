import streamlit as st

from analysis.head_to_head_analysis import *

from utils.data import TEAMS


team_1 = st.selectbox("Select Team: ", TEAMS, key='team_1')
st.markdown(
    f'''
    <div style="text-align: center;"> VS </div>
    ''',
    unsafe_allow_html=True
)
team_2 = st.selectbox("Select Team: ", TEAMS, key='team_2   ')


st.write(matches_played(team_1, team_2))
st.write(total_wins(team_1, team_2))
st.write(most_runs(team_1, team_2))
st.write(most_wickets(team_1, team_2))
st.write(highest_score(team_1, team_2))
st.write(lowest_score(team_1, team_2))
st.write(highest_margin(team_1, team_2))
st.write(recent_form(team_1, team_2))
st.write(playoffs_performance(team_1, team_2))