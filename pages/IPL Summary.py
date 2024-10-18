import os
import sys

import streamlit as st

current_dir = os.getcwd()
sys.path.append(os.path.join(current_dir))


from analysis import IPL_Summary

print(IPL_Summary.deliveries)
