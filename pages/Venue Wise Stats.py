import streamlit as st

from analysis.venue_analysis import average_first_innings_score, most_wickets, toss_decision, win_percentage
from utils import data

venues = data.STADIUMS

selected = st.selectbox("Choose a venue ", options=venues)

st.write(average_first_innings_score(selected))
st.dataframe(win_percentage(selected), use_container_width=True, hide_index=True)
st.write(most_wickets(selected))
st.write(toss_decision  (selected))
