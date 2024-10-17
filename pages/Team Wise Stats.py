import os
import sys
import time


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

import streamlit as st
from analysis import team_analysis


team = st.selectbox("Choose a team", ['Chennai Super Kings', 'Kolkata Knight Riders'])

st.write(team_analysis.avg_powerplay_score(team))