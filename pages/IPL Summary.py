import streamlit as st
from analysis.IPL_Summary import *
from utils.page_layout import header, footer

st.set_page_config(page_icon="📝", page_title="Summary", layout='wide', initial_sidebar_state='collapsed')

header(title="IPL Summary", description="1. Discover key records and statistics from the tournament's inception to the latest season.<br>\
       <br>\
2. Get a quick summary of total matches, runs, wickets, and iconic players that defined the IPL.")

st.divider()

summary = Summary()

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown(
        f"""
            <h2 style ='text-align: center;'> Total Seasons </h2>
            <h3 style='text-align: center;'>{summary.get_total_seasons}</h3>
        """,
        unsafe_allow_html=True
        )

with c2:
    with st.container(border=True):
        st.markdown(
        f"""
            <h2 style ='text-align: center;'> Total Runs Scored</h2>
            <h3 style='text-align: center;'>{summary.get_total_runs:,}</h3>
        """,
        unsafe_allow_html=True
        )
with c3:
    with st.container(border=True):
        st.markdown(
        f"""
            <h2 style ='text-align: center;'> Total Wickets taken</h2>
            <h3 style='text-align: center;'>{summary.get_total_wickets:,}</h3>
        """,
        unsafe_allow_html=True
        )


col1, col2, col3, col4 = st.columns(spec=[1,1,1,1], gap='medium', vertical_alignment='top')

with col1:
    with st.container(border=True, height=175):
        st.markdown(
        f"""
            <h2 style ='text-align: center; font-size: 30px'>Total Balls Bowled</h2>
            <h3 style='text-align: center;'>{summary.get_total_balls:,}</h3>
        """,
        unsafe_allow_html=True
        )


    with st.container(border=True, height=175):
        st.markdown(
        f"""
            <h2 style ='text-align: center;font-size: 30px'> Total Boundaries</h2>
            <h3 style='text-align: center;'>{summary.get_total_boundaries:,}</h3>
        """,
        unsafe_allow_html=True
        )


    with st.container(border=True, height=210):
        st.markdown(
            f"""<h2 style ='text-align: center;font-size: 30px'> Highest Team Score</h2>""", unsafe_allow_html=True)
        
        c = st.columns([1,1])
        with c[1]:
            st.markdown(f"""<h3 style='text-align: center; padding-top: 20px'>{summary.get_highest_team_score[1]:.0f}</h3>""",
            unsafe_allow_html=True)

        with c[0]:
            st.image(f"static/team_logos/{summary.get_highest_team_score[0]}.png")


with col2:
    with st.container(border=True, height=175):
        st.markdown(f"""<h3 style = 'text-align: center'>Most Runs</h3>""", unsafe_allow_html=True)
        
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_most_runs[0]}.png', width = 80)

        with c2:
            st.markdown(f"**Name:** {summary.get_most_runs[0]}")
            st.markdown(f"**Runs:** {summary.get_most_runs[1]}")

    with st.container(border=True, height=175):
        st.markdown(f"""<h3 style = 'text-align: center'>Most 6s</h3>""", unsafe_allow_html=True)
        
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_most_6s[0]}.png', width = 80)

        with c2:
            st.markdown(f"**Name:** {summary.get_most_6s[0]}")
            st.markdown(f"**Runs:** {summary.get_most_6s[1]}")

    with st.container(border=True, height=200):
        st.markdown(f"""<h3 style = 'text-align: center'>Highest Player score</h3>""", unsafe_allow_html=True)
        
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_highest_individual_score[0]}.png', width = 90)

        with c2:
            st.markdown(f"**Name:** {summary.get_highest_individual_score[0]}")
            st.markdown(f"**Runs:** {summary.get_highest_individual_score[1]}")



with col3:
    with st.container(border=True, height=175):
        st.markdown(f"""<h3 style = 'text-align: center'>Most Wickets</h3>""", unsafe_allow_html=True)
        
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_most_wickets[0]}.png', width = 85)

        with c2:
            st.markdown(f"**Name:** {summary.get_most_wickets[0]}")
            st.markdown(f"**Wickets:** {summary.get_most_wickets[1]}")


    with st.container(border=True, height=175):
        st.markdown(f"""<h3 style = 'text-align: center'>Most 4s</h3>""", unsafe_allow_html=True)
        
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_most_4s[0]}.png', width = 85)

        with c2:
            st.markdown(f"**Name:** {summary.get_most_4s[0]}")
            st.markdown(f"**Total 4s:** {summary.get_most_4s[1]}")


    with st.container(border=True, height=200):
        st.markdown(f"""<h3 style = 'text-align: center'>Most 50s</h3>""", unsafe_allow_html=True)
        
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_most_50s[0]}.png', width = 90)

        with c2:
            st.markdown(f"**Name:** {summary.get_most_50s[0]}")
            st.markdown(f"**50s:** {summary.get_most_50s[1]}")



with col4:
    with st.container(border=True, height=175):
        st.markdown(f"""<h3 style = 'text-align: center'>Most Catches</h3>""", unsafe_allow_html=True)
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_most_catches[0]}.png', width = 85)

        with c2:
            st.markdown(f"**Name:** {summary.get_most_catches[0]}")
            st.markdown(f"**Catches:** {summary.get_most_catches[1]}")


    with st.container(border=True, height = 175):
        st.markdown(f"""<h3 style = 'text-align: center'>Most POTM Awards</h3>""", unsafe_allow_html=True)
            
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_most_potm[0]}.png', width = 85)

        with c2:
            st.markdown(f"**Name:** {summary.get_most_potm[0]}")
            st.markdown(f"**Awards:** {summary.get_most_potm[1]}")

    with st.container(border=True, height=200):
        st.markdown(f"""<h3 style = 'text-align: center'>Most 100s</h3>""", unsafe_allow_html=True)
            
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{summary.get_most_100s[0]}.png', width = 90)

        with c2:
            st.markdown(f"**Name:** {summary.get_most_100s[0]}")
            st.markdown(f"**100s:** {summary.get_most_100s[1]}")


footer()