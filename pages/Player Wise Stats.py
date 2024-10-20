import streamlit as st

st.set_page_config(page_title="Player Wise Stats", page_icon="🤵", initial_sidebar_state="collapsed")

import os
import sys


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

from analysis import player_analysis
from utils import constants

player_name = st.selectbox("Choose a player (start typing the last name)", options = constants.PLAYERS, index=None)


st.write(f"Batting Average: {player_analysis.batting_average(player_name=player_name)}")
st.write(f"Strike Rate: {player_analysis.strike_rate(player_name=player_name)}")
st.write(f"powerplay runs: {player_analysis.runs_scored_in_powerplay(player_name=player_name)}")
st.write(f"death over runs: {player_analysis.runs_scored_in_death_overs(player_name=player_name)}")
st.write(f"Most Successful Batting Venue: {player_analysis.most_successful_venue(player_name=player_name)[0]}")
st.write(f"Most Successful Bowling Venue: {player_analysis.most_successful_venue(player_name=player_name)[1]}")

# print(constants.PLAYERS)