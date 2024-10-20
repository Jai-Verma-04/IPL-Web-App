import os
import sys
import streamlit as st


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))

import utils.constants as c

team = st.selectbox("Choose a team", c.TEAMS)

st.write("here is the graph")

print(current_dir)