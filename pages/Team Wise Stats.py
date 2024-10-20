import os
import sys
import streamlit as st


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))
from utils import constants

team = st.selectbox("Choose a team", constants.TEAMS)

st.write("here is the graph")
