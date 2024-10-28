import streamlit as st

from analysis.venue_analysis import average_first_innings_score, most_wickets, toss_decision, win_percentage
from utils import data

venues = data.STADIUMS

selected = st.selectbox("Choose a venue ", options=venues)

st.image(f"static\\stadiums\\{selected}.png")
