import streamlit as st

from utils.data import TEAMS

team = st.selectbox("Choose a team", TEAMS)

st.image(f'\\static\\team_logos\\{team}.png')