import streamlit as st

from utils.data import TEAMS

team = st.selectbox("Choose a team", TEAMS)

st.write("here is the graph")