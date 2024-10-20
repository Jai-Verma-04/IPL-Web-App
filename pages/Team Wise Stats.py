import os
import sys
import streamlit as st


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

from utils import CONSTANTS

team = st.selectbox("Choose a team", CONSTANTS.TEAMS)

st.write("here is the graph")
