import streamlit as st
from analysis import season_analysis as season
from utils.data import SEASONS
from utils.page_layout import header, footer
from utils.image_markdown import img_to_html

st.set_page_config(page_title="Season wise Stats", page_icon="🆚", layout="wide", initial_sidebar_state="collapsed")

header(title="Season Wise Statistics", description="1. Explore how each IPL season unfolded, and who became the crowned team. <br>\
2. Analyze top run-scorers, wicket-takers, and key trends across all IPL seasons. <br> 3. Start by selecting an year from the drop-down below 👇", right_image="static/icons/ipl logo.png")

left_widget,right_widget = st.columns([0.32, 0.67], gap = "medium")

with left_widget:
    selected_season = st.selectbox("Select a Season: ", SEASONS)

with right_widget:
    fact = season.random_fact(selected_season)
    with st.container(border=True):
        st.markdown(
            '''
            <h4> Random Fact about this season </h4>
            ''', unsafe_allow_html=True)
        st.write(fact)


left_col, center_col, right_col = st.columns([0.3, 0.3, 0.3],gap='small')


with left_col:
    
    with st.container(border=True, key="winner"):
        winner = season.winner(selected_season)
        
        st.markdown(
            f"""
                <div style="text-align: center;">
                    <h2 style="font-size: 2em; font-weight: bold; margin-top: 0px;">Winner 🏆</h2>
                </div>
                {img_to_html(f'static/team_logos/{winner}.png', width=130, height=130)}
            """,
            unsafe_allow_html=True
        )

    with st.container(border=True, key="runner up"):
        runner_up = season.runner_up(selected_season)

        st.markdown(
            f"""
                <div style="text-align: center;">
                    <h2 style="font-size: 2em; font-weight: bold; margin-top: 0px;">Runner Up</h2>
                </div>
            {img_to_html(f'static/team_logos/{runner_up}.png', width=130, height=130)}
            """,
            unsafe_allow_html=True
        )


with center_col:
    highest_run_batsman, highest_runs = season.highest_run_scorer(selected_season)[0], season.highest_run_scorer(selected_season)[1]

    with st.container(border=True, key="highest run scorer"):
        st.markdown(
            f"""
                <div style="text-align: center;">
                    <h2 style="font-size: 2em; font-weight: bold; margin-top: -5px; margin-bottom: 10px">Highest Runs Scorer</h2>
            """, 
            unsafe_allow_html=True
        )

        c1, c2 = st.columns([1,1])
        with c1:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center; align-items: center;">
                    <div>
                        {img_to_html(f"static/players/{highest_run_batsman}.png", width=150, height=150)}
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div style="text-align: left;">
                    <h4 style="font-size: 1.5em; font-weight: normal; margin-top: 0px;">
                        <span style="font-weight: bold;">Name:</span> {highest_run_batsman}
                    </h4>
                    <h4 style="font-size: 1.5em; font-weight: normal; margin-top: 0px;">
                        <span style="font-weight: bold;">Runs:</span> {highest_runs}
                    </h4>
                </div>
                """,
                unsafe_allow_html=True
            )

    
    with st.container(border=True, key= "total matches"):
        total_matches_played = season.total_matches_played(selected_season)
        
        st.markdown(f"""
                <div style="text-align: center;">
                <h2 style="font-size: 2em; font-weight: normal; margin-top: -1px;">
                    <span style="font-weight: bold;">Total Matches Played:</span> {total_matches_played}
                </h2>
            """, 
            unsafe_allow_html=True
        )

    with st.container(border=True, key= "total 4s"):
        total_4s = season.total_4s(selected_season)
        
        st.markdown(f"""
                <div style="text-align: center;">
                <h2 style="font-size: 2em; font-weight: normal; margin-top: -2px;">
                    <span style="font-weight: bold;">Total 4s Hit:</span> {total_4s}
                </h2>
            """, 
            unsafe_allow_html=True
        )
        

with right_col:
    highest_wicket_taker, highest_wickets = season.highest_wicket_taker(selected_season)[0], season.highest_wicket_taker(selected_season)[1]


    with st.container(border=True, key="highest wicket taker"):
        st.markdown(f"""
                <div style="text-align: center;">
                    <h2 style="font-size: 2em; font-weight: bold; margin-top: -5px; margin-bottom: 7px">Highest Wicket Taker</h2>
            """, 
            unsafe_allow_html=True
        )

        c1, c2 = st.columns([1,1])

        with c1:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center; align-items: center;">
                    <div>
                        {img_to_html(f"static/players/{highest_wicket_taker}.png", width=150, height=150)}
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div style="text-align: left;">
                    <h4 style="font-size: 1.5em; font-weight: normal; margin-top: 0px;">
                        <span style="font-weight: bold;">Name:</span> {highest_wicket_taker}
                    </h4>
                    <h4 style="font-size: 1.5em; font-weight: normal; margin-top: 0px;">
                        <span style="font-weight: bold;">Wickets:</span> {highest_wickets}
                    </h4>
                </div>
                """,
                unsafe_allow_html=True
            )

    
    with st.container(border=True, key= "total runs"):
        total_runs_scored = season.total_runs_scored(selected_season)
        
        st.markdown(f"""
                <div style="text-align: center;">
                <h2 style="font-size: 2em; font-weight: normal; margin-top: 0px;">
                    <span style="font-weight: bold;">Total Runs Scored:</span> {total_matches_played}
                </h2>
            """, 
            unsafe_allow_html=True
        )

    with st.container(border=True, key= "total 6s"):
        total_6s = season.total_6s(selected_season)
        
        st.markdown(f"""
                <div style="text-align: center;">
                <h2 style="font-size: 2em; font-weight: normal; margin-top: 0px;">
                    <span style="font-weight: bold;">Total 6s Hit:</span> {total_6s}
                </h2>
            """, 
            unsafe_allow_html=True
        )


footer()