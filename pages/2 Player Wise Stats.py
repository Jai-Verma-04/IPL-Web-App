import streamlit as st
from analysis import player_analysis
from utils.data import PLAYERS

st.set_page_config(page_title="Player Wise Stats", page_icon="🤵")


player_name = st.selectbox("Choose a player (start typing the last name)", options = PLAYERS, index=120)


st.write(f"Batting Average: {player_analysis.batting_average(player_name=player_name)}")
st.write(f"Strike Rate: {player_analysis.strike_rate(player_name=player_name)}")
st.write(f"powerplay runs: {player_analysis.runs_scored_in_powerplay(player_name=player_name)}")
st.write(f"death over runs: {player_analysis.runs_scored_in_death_overs(player_name=player_name)}")
st.write(f"Most Successful Batting Venue: {player_analysis.most_successful_venue(player_name=player_name)[0]}")
st.write(f"Most Successful Bowling Venue: {player_analysis.most_successful_venue(player_name=player_name)[1]}")
st.write(player_analysis.wickets_taken(player_name))

st.image(f"./static/players/{player_name}.png")