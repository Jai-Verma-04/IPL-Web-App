import streamlit as st
from analysis.player_analysis import *
from utils.data import PLAYERS
from utils.page_layout import header, footer

st.set_page_config(page_title="Player Wise Stats", page_icon="🏏", layout = "wide", initial_sidebar_state="collapsed")

header(title="Player Wise Stats", description="\
1. Explore comprehensive stats, including runs scored, strike rates, and wickets taken.<br>\
2. Analyze key metrics like powerplay runs, batting averages, and bowling economy.<br>\
3. Discover the most successful venues and teams for both batsmen and bowlers.<br>")

cols = st.columns([0.2, 0.9], gap='large')

with cols[0]:
    player = st.selectbox("Choose a player (start typing the last name)", options = PLAYERS, index=1)
    st.image(f"static/players/{player}.png")
    st.write(f"Matches Played: {total_matches_played(player)}")
    st.write(f"POTM Awards: {potm_awards(player)}")

with cols[1]:
    batting_stats, bowling_stats = st.tabs(['Batting Stats', "Bowling Stats"])

    with batting_stats:
        col = st.columns([1,1,1], gap='small')
        with col[0]:
            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Total Runs Scored </h3>
                    <h4 style ='text-align: center; font-size: 18px'> {runs_scored(player)} </h4>
                """,    
                unsafe_allow_html=True
                )

            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Highest Individual Score </h3>
                    <h4 style ='text-align: center; font-size: 18px'> {highest_individual_score(player)} </h4>
                """,    
                unsafe_allow_html=True
                )

            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Strike Rate </h3>
                    <h4 style ='text-align: center; font-size: 18px'> {strike_rate(player)} </h4>
                """,    
                unsafe_allow_html=True
                )


        with col[1]:
            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Powerplay Runs </h3>
                    <h4 style ='text-align: center; font-size: 18px'> {runs_scored_in_powerplay(player)} </h4>
                """,    
                unsafe_allow_html=True
                )

            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Death Over Runs </h3>
                    <h4 style ='text-align: center; font-size: 18px'> {runs_scored_in_death_overs(player)} </h4>
                """,    
                unsafe_allow_html=True
                )

            
            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Most Successful Venue </h3>
                    <h4 style ='text-align: center; font-size: 18px'> {most_successful_venue(player)[0]} </h4>
                """,    
                unsafe_allow_html=True
                )

        with col[2]:
            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Total 4s </h3>
                    <h4 style ='text-align: center; font-size: 18px'> {total_4s_hit(player)} </h4>
                """,    
                unsafe_allow_html=True
                )

            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Total 6s </h3>
                    <h4 style ='text-align: center; font-size: 18px'> {total_6s_hit(player)} </h4>
                """,    
                unsafe_allow_html=True
                )

            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Batting Average</h3>
                    <h4 style ='text-align: center; font-size: 18px'> {batting_average(player)} </h4>
                """,    
                unsafe_allow_html=True
                )

        c1=st.columns([0.5, 1, 0.5])   

        with c1[1]: 
            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Most Runs against </h3>
                """,    
                unsafe_allow_html=True
                )
                st.write(favorite_teams_to_score(player))
    
    
    with bowling_stats:
        cols = st.columns([1,1], gap='medium')

        with cols[0]:
            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Total Wickets taken </h3>
                    <h4 style ='text-align: center; font-size: 24px'> {wickets_taken(player)}</h4>
                """,    
                unsafe_allow_html=True
                )

            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Bowling Average </h3>
                    <h4 style ='text-align: center; font-size: 24px'> {bowling_average(player)}</h4>
                """,    
                unsafe_allow_html=True
                )
            
        with cols[1]:
            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Total Runs conceded </h3>
                    <h4 style ='text-align: center; font-size: 24px'> {runs_conceded(player)}</h4>
                """,    
                unsafe_allow_html=True
                )

            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Most Successful Venue </h3>
                    <h4 style ='text-align: center; font-size: 24px'> {most_successful_venue(player)[1]}</h4>
                """,    
                unsafe_allow_html=True
                )

        c1 = st.columns([1,1,1])
        with c1[1]:
            with st.container(border=True):
                st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Most wickets against </h3>
                """,    
                unsafe_allow_html=True
                )
                st.write(favorite_team_for_bowlers(player))

footer()
