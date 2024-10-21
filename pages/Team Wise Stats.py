import os
import sys
import streamlit as st


# current_dir = os.getcwd()
# sys.path.append(os.path.join(current_dir))

from utils.read_data import matches
from utils.data import TEAMS

team = st.selectbox("Choose a team", TEAMS)

st.write("here is the graph")