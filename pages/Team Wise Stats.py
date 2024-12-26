import streamlit as st
from utils.data import TEAMS
from utils.page_layout import header, footer
from analysis.team_analysis import *
from utils.image_markdown import img_to_html

st.set_page_config(page_title="Team Wise Stats", page_icon="🤼", layout='wide', initial_sidebar_state='collapsed')

header(title="Team Wise Stats", description="1. Delve into the team's IPL journey, including trophies, win rates, and number of matches played.<br>\
2. Explore stats like team and venue dominance, boundary counts, and average powerplay scores.<br>\
3. Highlight the team's leading wicket-takers, run scorers, and toss statistics.")

cols = st.columns([0.23, 0.77], gap='large')

with cols[0]:
    team = st.selectbox("Select a team", options = TEAMS, index=1)
    st.image(f"static/team_logos/{team}.png", width=200)

    st.divider()

    with st.container(border=True):
        trophies = number_of_trophies(team)
        st.write(f"Number of trophies: {str(trophies)}")

        if trophies > 0:
            lst = [1]*trophies
            c = st.columns(lst, gap='small')
            for i in range(len(lst)):
                with c[i]:
                    st.image(f'static/others/ipl-trophy.png', width=50)
    
    with st.container(border=True):
        st.write("Total Matches Played: ", str(number_of_matches_played(team)))
        st.write("Number of Matches Won:", str(number_of_matches_won(team)))
        st.write("Win percentage: ", str(win_percentage(team)))

with cols[1]:
    c = st.columns([1,1.1,1], gap='small')
        
    with c[0]:
        with st.container(border=True, height=200):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Most Wins against team </h3>
            """,    
            unsafe_allow_html=True
            )

            st.write(most_wins_against(team))
            
        with st.container(border=True):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Most Successful Venue </h3>
                <h4 style ='text-align: left; font-size: 18px;'> Venue: {most_matches_won_at_venue(team)[0]}</h4>
                <h4 style ='text-align: left; font-size: 18px;'> Matches Won: {most_matches_won_at_venue(team)[1]}</h4>
            """,
            unsafe_allow_html=True
            )
        with st.container(border=True, height = 70):
            st.markdown(
            f"""
                <div>
                    <span style = 'margin-right:30px; margin-left:20px; font-size: 18px'>Total 4s: {total_4s(team)} </span>  
                    <span style = 'font-size: 18px'> Total 6s: {total_6s(team)} </span>
                </div>
            """, 
            unsafe_allow_html=True
            )
    
    
    with c[1]:
        with st.container(border=True):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Toss and Match Results </h3>
            """,
            unsafe_allow_html=True
            )
            st.write(match_and_toss(team))
        
        with st.container(border=True):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Highest score against a team</h3>
                <h4 style ='text-align: left; font-size: 18px;'> Team: {highest_team_score(team)[0]}</h4>
                <h4 style ='text-align: left; font-size: 18px;'> Score: {highest_team_score(team)[1]:.0f}</h4>

            """,
            unsafe_allow_html=True
            )
        with st.container(border=True):
            st.write(f"Average Powerplay Score: {avg_powerplay_score(team)}")

    with c[2]:
        with st.container(border=True):
            st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Top 3 Run scorers </h3>
                """,
                unsafe_allow_html=True
                )
            st.write(top3_run_scorers(team))

        with st.container(border=True):
            st.markdown(
                f"""
                    <h3 style ='text-align: center; font-size: 24px'> Top 3 Wicket Takers </h3>
                """,
                unsafe_allow_html=True
                )
            st.write(top3_wicket_takers(team))


    with st.container(border=True):
        st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Matches played in each season </h3>
            """,
            unsafe_allow_html=True
            )
        st.write(matches_per_season(team))

footer()
