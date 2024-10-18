import os
import sys
import time


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

import streamlit as st
from analysis import team_analysis
from utils import CONSTANTS

team = st.selectbox("Choose a team", CONSTANTS.TEAMS)

st.write("here is the graph")
st.pyplot(team_analysis.graph(team))