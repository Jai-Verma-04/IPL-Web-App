import os
import sys
import streamlit as st


from utils.constants import TEAMS

team = st.selectbox("Choose a team", TEAMS)

st.write("here is the graph")
