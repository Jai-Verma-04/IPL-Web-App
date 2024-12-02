import streamlit as st
from analysis import player_analysis
from utils.data import PLAYERS
from utils.navigation import custom_sidebar_navigation

st.set_page_config(page_title="Player Wise Stats", page_icon="🤵", layout = "wide", initial_sidebar_state="collapsed")
custom_sidebar_navigation("Player Wise Stats")

img_column, title_column = st.columns([0.3, 0.7], gap='medium', vertical_alignment='top')

@st.dialog("Help")
def readme_dialog():
    st.info("Read how to use this page")
    

with img_column:
    st.image(f"./static/icons/IPLAnalytica.png", width = 200)

with title_column:
    st.markdown(
        "<div style='text-align: center; font-size: 48px; font-weight: bold'>Search Player Name</div>",
        unsafe_allow_html=True,
    )

    if st.button("Check steps here"):
        readme_dialog()
    
    
player_name = st.selectbox("Choose a player (start typing the last name)", options = PLAYERS, index=120)

st.write(f"Most Successful Bowling Venue: {player_analysis.most_successful_venue(player_name=player_name)[1]}")

st.image(f"./static/players/{player_name}.png")