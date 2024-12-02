import streamlit as st
from utils.navigation import custom_sidebar_navigation

custom_sidebar_navigation("Home")
st.write("Welcome to IPL Web App Project")

st.info("""The Home Page is currently under construction. 
        Checkout Season Wise Stats and Generate Scorecard page from the sidebar
        """)