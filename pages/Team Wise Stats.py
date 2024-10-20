import os
import sys
import streamlit as st


current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))


team = st.selectbox("Choose a team")

st.write("here is the graph")
