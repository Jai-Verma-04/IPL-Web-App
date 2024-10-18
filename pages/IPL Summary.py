import os
import sys

import streamlit as st

current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))


from analysis import IPL_Summary

st.write(IPL_Summary.get_most_catches())