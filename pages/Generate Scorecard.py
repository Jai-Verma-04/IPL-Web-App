import streamlit as st
from utils.data import SEASONS, TEAMS
from analysis.scorecard_analysis import *
from utils.page_layout import header, footer

st.set_page_config(page_title="Generate Scorecard", page_icon="💯", layout='wide', initial_sidebar_state='collapsed')
header(title="Generate Scorecard", description="Generate scorecard of your favourite ipl match. <br> 1. Select the teams from the drop-downs. <br> 2. Select the season for which they competed.\
       <br>3. Finally, select the match_id from the matches list to generate the scorecard.")

c = st.columns([0.38, 0.04, 0.38, 0.20])

with c[0]:
    team_1 = st.selectbox('Choose a team: ', TEAMS, key = 'team_1')
with c[1]:
    st.markdown("""
            <div style="text-align: center; padding-top: 35px">
                VS
            </div>
    """, unsafe_allow_html=True)

with c[2]:
    team_2 = st.selectbox('Choose a team: ', [team for team in TEAMS if team!=team_1], key = 'team_2')

with c[3]:
    season = st.selectbox('Choose a season', SEASONS, key='season')


c1 = st.columns([4, 1])
with c1[0]:
    matches_list = display_matches(team_1, team_2, season)

    if len(matches_list)==0:
        st.write("No matches available for the selected combination")
        st.stop()
    else:
        st.table(matches_list)

with c1[1]:
    st.text("")
    st.text("")
    st.text("")
    match_id = st.selectbox("Choose Match ID: ", matches_list['id'], key='match_id')

st.divider()

a=MatchInfo(match_id)
st.markdown("""
        <div style="text-align: center; font-size: 36px;">
        <strong> Match Information </strong>
        </div>
""", unsafe_allow_html=True)

st.divider()

cols = st.columns([1, 2], gap='large')
with cols[0]:
    st.write("Match: ",a.match_name)
    st.write("Date: ", a.match_date)
    st.write(f"Toss: {a.toss[0]} won the toss and opt to {a.toss[1]}")
    st.write(f"Umpires: {a.umpires[0]} and {a.umpires[1]}")
    st.write("Match Result:", a.result)

with cols[1]:
    col = st.columns([1,1], gap='large')

    with col[0]:
        st.image(f"static/players/{a.potm}.png", width=250)
        st.write("Player of the Match: ", a.potm)

    with col[1]:
        team = a.result.split()[0]
        st.image(f"static/stadiums/{a.venue[0]}.png", use_column_width=True)
        st.write(f"Venue: {a.venue[0].split(',')[0].strip()}, {a.venue[1]}")

st.divider()


inning_1, inning_2 = st.tabs(["First Innings", "Second Innings"])

def display_results(inning):    
    """display the results in proper format
    Args:
        inning (int): the inning number for which the results are to be displayed
    """
    batting, bowling = st.tabs(['Batting', 'Bowling'])
    
    with batting:
        cols = st.columns([2, 1], gap='medium')

        with cols[0]:
            st.markdown("""
            <div style="text-align: left; font-size: 24px;padding-left: 300px">
                <strong>Batting Scorecard</strong>
            </div>  
            """, unsafe_allow_html=True)

            score=ScoreCard(match_id, inning=inning)
            st.write(score.batting_data)

        with cols[1]:
            st.image(f"static/players/{score.key_batter}.png", width=250)
            st.write("Key Batter: ", score.key_batter)

        st.markdown("""
        <div style="text-align: center; font-size: 24px; padding-bottom: 20px">
            <strong> Batting Summary </strong>
        </div>
        """, unsafe_allow_html=True)

        col_1 = st.columns([1,1,1,1,1])
        
        with col_1[0]:
            st.write("Total Overs: ", score.batting_summary[0])
        with col_1[1]:
            st.write("Total Runs: ", score.batting_summary[1])
        with col_1[2]:
            st.write("Total Wickets: ", score.batting_summary[2])
        with col_1[3]:
            st.write("Run Rate: ", score.batting_summary[3])
        with col_1[4]:
            st.write("Extras: ", score.batting_summary[4])
        
    with bowling:
        cols = st.columns([2, 1, 1], gap='small')
        with cols[0]:
            st.markdown("""
            <div style="text-align: left; font-size: 24px; padding-left: 100px; padding-bottom: 10px">
                <strong>Bowling Scorecard</strong>
            </div>  
            """, unsafe_allow_html=True)            
            st.write(score.bowler_data)

        with cols[1]:
            st.markdown("""
            <div style="font-size: 24px; padding-bottom: 10px">
                <strong>Fall of Wickets</strong>
            </div>  
            """, unsafe_allow_html=True) 

            st.write(score.fall_of_wickets)

        
        with cols[2]:
            st.image(f"static/players/{score.key_bowler}.png")
            st.write("Key Bowler: ",score.key_bowler)
        
with inning_1:
    display_results(1)

with inning_2:
    display_results(2)

footer()