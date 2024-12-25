import streamlit as st
from analysis.head_to_head_analysis import *
from utils.data import TEAMS
from utils.page_layout import header, footer

st.set_page_config(page_icon="🆚", page_title="Head to Head Stats", layout='wide', initial_sidebar_state='collapsed')

header(title="Head to Head Stats", description="1. Compare team performances in head-to-head matchups across all IPL seasons.<br>\
2. Analyze win-loss records, key players, and memorable moments from iconic rivalries.<br>\
3. Select 2 teams from the below drop-downs to get started")

col = st.columns([0.48, 0.04, 0.48])

with col[0]:
    team_1 = st.selectbox("Select Team: ", TEAMS, key='team_1', index=0)

with col[1]:   
    st.markdown(
        f'''
        <div style="text-align: center;padding-top: 30px"> VS </div>
        ''',
        unsafe_allow_html=True
    )

with col[2]:
    team_2 = st.selectbox("Select Team: ", [team for team in TEAMS if team != team_1], key='team_2', index=0)


column = st.columns([1,1,1])

with column[0]:
    with st.container(border = True, height = 150):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;"> <strong>Total number of matches played</strong></div>
        <h3 style="text-align:center;font-size:24px;padding-top:40px;">{matches_played(team_1, team_2)}</h3>
        ''',
        unsafe_allow_html=True
        )

    with st.container(border=True, height=190):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;"> <strong>Wins by each team</strong></div>
        ''',
        unsafe_allow_html=True
        )

        st.write(total_wins(team_1, team_2))
    
    with st.container(border=True, height = 190):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;"> <strong>Win percentage</strong></div>
        ''',
        unsafe_allow_html=True
        )
        st.write(win_percentage(team_1, team_2))

with column[1]:
    with st.container(border=True, height=180):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;padding-bottom:20px"> <strong>Most runs</strong></div>
        ''',
        unsafe_allow_html=True
        )
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{most_runs(team_1, team_2)[0]}.png', width = 90)

        with c2:
            st.markdown(f"**Name:** {most_runs(team_1, team_2)[0]}")
            st.markdown(f"**Runs:** {most_runs(team_1, team_2)[1]}")

    with st.container(border=True, height=160):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;padding-bottom:20px"> <strong>Highest Score</strong></div>
        <h3 style="text-align:center;font-size:24px;">{highest_score(team_1, team_2)}</h3>
        ''',
        unsafe_allow_html=True
        )

    with st.container(border=True, height=190):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;padding-bottom:20px"> <strong>Last 5 matches</strong></div>
        ''',
        unsafe_allow_html=True
        )
        st.write(recent_form(team_1, team_2))
       

with column[2]:
    with st.container(border=True, height=180):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;padding-bottom:20px"> <strong>Most Wickets</strong></div>
        ''',
        unsafe_allow_html=True
        )
        c1, c2 = st.columns([1,1])
        
        with c1:
            st.image(f'static/players/{most_wickets(team_1, team_2)[0]}.png', width = 90)

        with c2:
            st.markdown(f"**Name:** {most_wickets(team_1, team_2)[0]}")
            st.markdown(f"**Wickets:** {most_wickets(team_1, team_2)[1]}")

    with st.container(border=True, height=160):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;padding-bottom:20px"> <strong>Lowest Score</strong></div>
        <h3 style="text-align:center;font-size:24px;">{lowest_score(team_1, team_2)}</h3>
        ''',
        unsafe_allow_html=True
        )

    with st.container(border=True, height=190):
        st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;padding-bottom:20px"> <strong>Playoffs perfomance</strong></div>
        ''',
        unsafe_allow_html=True
        )
        st.write(playoffs_performance(team_1, team_2))

with st.container(border=True):
    st.markdown(
        f'''
        <div style="text-align: center; font-size: 24px;padding-bottom:20px"> <strong>Best Performance (By victory margin)</strong></div>
        ''',
        unsafe_allow_html=True
        )
    st.write(highest_margin(team_1, team_2))


footer()