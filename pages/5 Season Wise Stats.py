import streamlit as st

from analysis.season_analysis import *
from utils.data import SEASONS

seasons = st.selectbox('SEASON: ', SEASONS)

st.write(highest_run_scorer(seasons))
st.write(highest_wicket_taker(seasons))
st.write(most_wins_in_league_matches(seasons))

st.write(winner(seasons))
st.write(runner_up(seasons))