import streamlit as st
from analysis.venue_analysis import *
from utils.data import STADIUMS
from utils.page_layout import header, footer
from utils.image_markdown import img_to_html

st.set_page_config(page_title="Venue Wise Stats", page_icon="🏟️", layout='wide', initial_sidebar_state='collapsed')

header(title="Venue Wise Stats", description="1. Uncover key statistics and trends for matches played at various IPL venues.<br>\
2. Analyze team and player performances at specific stadiums across seasons, compare scoring patterns and win percentages across different locations.")

cols = st.columns([0.23, 0.77], gap='small')

with cols[0]:
    venue = st.selectbox("Select a venue", options = STADIUMS, index=1)
    st.divider()
    st.image(f"static/stadiums/{venue}.png")

    with st.container(border=True):
        st.write("Total Matches Played: ", str(total_matches_played(venue)))
        st.write("Total Boundaries Hit:", str(total_boundaries(venue)))
        st.write("Average First Innings Score:", str(average_first_innings_score(venue)))

with cols[1]:
    c = st.columns([1, 1, 1])

    with c[0]:
        with st.container(border=True, height=260):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Highest Team Total </h3>
                <h4 style ='text-align: center; font-size: 18px;'> Team: {highest_team_total(venue)[0]}</h4>
                <h4 style ='text-align: center; font-size: 18px;'> Highest Score: {highest_team_total(venue)[1]}</h4>
                {img_to_html(f'static/team_logos/{highest_team_total(venue)[0]}.png', width=70, height=70)}
            """,
            unsafe_allow_html=True
            )
        
        with st.container(border=True, height=260):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Most Runs </h3>
                <h4 style ='text-align: center; font-size: 18px;'> Name: {most_runs(venue)[0]}</h4>
                <h4 style ='text-align: center; font-size: 18px;'> Runs: {most_runs(venue)[1]}</h4>
                {img_to_html(f'static/players/{most_runs(venue)[0]}.png', width=70, height=70)}
            """,
            unsafe_allow_html=True
            )
        


    with c[1]:
        with st.container(border=True, height=260):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Lowest Team Total </h3>
                <h4 style ='text-align: left; font-size: 18px;'> Team: {lowest_team_total(venue)[0]}</h4>
                <h4 style ='text-align: left; font-size: 18px;'> Lowest Score: {lowest_team_total(venue)[1]}</h4>
                {img_to_html(f'static/team_logos/{lowest_team_total(venue)[0]}.png', width=70, height=70)}

            """,
            unsafe_allow_html=True
            )

        with st.container(border=True, height=260):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Most Wickets </h3>
                <h4 style ='text-align: left; font-size: 18px;'> Name: {most_wickets(venue)[0]}</h4>
                <h4 style ='text-align: left; font-size: 18px;'> Wickets: {most_wickets(venue)[1]}</h4>
                {img_to_html(f'static/players/{most_wickets(venue)[0]}.png', width=70, height=70)}

            """,
            unsafe_allow_html=True
            )


    with c[2]:
        with st.container(border=True, height=260):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Most Successful Team</h3>
                <h4 style ='text-align: left; font-size: 18px;'> Team: {most_successful_team(venue)[0]}</h4>
                <h4 style ='text-align: left; font-size: 18px;'> Win Percentage: {most_successful_team(venue)[1]} % </h4>
                {img_to_html(f'static/team_logos/{most_successful_team(venue)[0]}.png', width=70, height=70)}

            """,
            unsafe_allow_html=True
            )

        with st.container(border=True, height=260):
            st.markdown(
            f"""
                <h3 style ='text-align: center; font-size: 24px'> Toss Decisions</h3>
            """,
            unsafe_allow_html=True
            )
            st.write(toss_decision(venue))

        
    






footer()
