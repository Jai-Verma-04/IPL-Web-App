import streamlit as st
import os
from utils.data import TEAMS

team = st.selectbox("Choose a team", TEAMS)

logo_path = os.path.join('static/team_logos', f"{team}.png")


st.image(logo_path)