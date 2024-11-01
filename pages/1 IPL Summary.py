import streamlit as st
from analysis.IPL_Summary import *

a = Summary()

st.set_page_config(
    page_title = "Summary",
    page_icon="🏏", 
    initial_sidebar_state="auto",
    layout="wide"
    )

st.markdown("<h1 style='text-align: center;'> SUMMARY OF IPL (2007-2024)</h1>", unsafe_allow_html=True)

imgcol, headercol = st.columns([1,7], gap = 'small', vertical_alignment='top')

with imgcol:
    st.image("./static/icons/ipl logo.png", clamp=False, use_column_width=True)

with headercol:
    c1, c2, c3 = st.columns(3)
    
    with c1:
        with st.container(border=True):
            st.markdown(
            f"""
                <h2 style ='text-align: center;'> Total Seasons </h2>
                <h3 style='text-align: center;'>{a.get_total_seasons}</h3>
            """,
            unsafe_allow_html=True
            )

    with c2:
        with st.container(border=True):
            st.header("Total runs made")
            st.markdown(
            f"""
                <h3 style='text-align: center;'>{a.get_total_runs:,}</h3>
            """,
            unsafe_allow_html=True
            )
    with c3:
        with st.container(border=True):
            st.header("Total Wickets")
            st.markdown(
            f"""
                <h3 style='text-align: center;'>{a.get_total_wickets:,}</h3>
            """,
            unsafe_allow_html=True
            )

col1, col2, col3, col4 = st.columns(spec=[1,1,1,1], gap='medium', vertical_alignment='top')

with col1:
    with st.container(border=True, height=175):
        st.header(f"Total ball bowled:", anchor=False)
        st.text(f"{a.get_total_balls:,}")

    with st.container(border=True, height=175):
        st.header(f"Total boundaries:", anchor=False)
        st.text(f"{a.get_total_boundaries:,}")

    with st.container(border=True, height=175):
        st.header(f"Highest Team Score:", anchor=False)
        st.text(f"{a.get_highest_team_score[0]}")
        st.text(f"{a.get_highest_team_score[1]:.0f}")
        st.image(f"static/team_logos/{a.get_highest_team_score[0]}.png")

with col2:
    with st.container(border=True):
        st.markdown(f"""<h3 style = 'text-align: center'>Most Runs:</h3>""", unsafe_allow_html=True)
        c1, c2 = st.columns([1,1])
        with c1:
            st.image('static/icons/ipl logo.png', width = 75)
        
        with c2:
            st.markdown(f"**Name:** {a.get_most_runs[0]}")
            st.markdown(f"**Runs:** {a.get_most_runs[1]}")

    with st.container(border=True, height=175):
        st.header(f"Most 6s:", anchor=False)
        st.text(f"{a.get_most_6s[0]}")
        st.text(f"{a.get_most_6s[1]}")

    with st.container(border=True, height=175):
        st.header(f"Highest individual score:", anchor=False)
        st.text(f"Player: {a.get_highest_individual_score[0]}")
        st.text(f"Runs: {a.get_highest_individual_score[1]}")


with col3:
    with st.container(border=True, height=175):
        st.header(f"Most Wickets:", anchor=False)
        st.text(f"{a.get_most_wickets[0]}")
        st.text(f"{a.get_most_wickets[1]}")

    with st.container(border=True, height=175):
        st.header(f"Most 4s:", anchor=False)
        st.text(f"{a.get_most_4s[0]}")
        st.text(f"{a.get_most_4s[1]}")
    
    with st.container(border=True, height=175):
        st.header(f"Most 50s:", anchor=False)
        st.text(f"{a.get_most_50s[0]}")
        st.text(f"{a.get_most_50s[1]}")
    

with col4:
    with st.container(border=True, height=175):
        st.header(f"Most catches:", anchor=False)
        st.text(f"{a.get_most_catches[0]}")
        st.text(f"{a.get_most_catches[1]}")

    with st.container(border=True, height = 175):
        st.header(f"Most POTM: ", anchor=False)
        st.text(f"{a.get_most_potm[0]}")
        st.text(f"{a.get_most_potm[1]}")

    with st.container(border=True, height=175):
        st.header(f"Most 100s:", anchor=False)
        st.text(f"{a.get_most_100s[0]}")
        st.text(f"{a.get_most_100s[1]}")