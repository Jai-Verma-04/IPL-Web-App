import os
import sys
import streamlit as st


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

from ..utils.constants import TEAMS

team = st.selectbox("Choose a team", TEAMS)

st.write("here is the graph")

print(current_dir)