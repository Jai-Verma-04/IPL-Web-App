import os
import streamlit as st
from utils import data

@st.fragment
def header(title, description, right_image="static/icons/ipl logo.png", left_image="static/icons/IPLAnalytica.png"):
    left, center, right = st.columns([0.2, 0.6, 0.2], gap='medium', vertical_alignment='top')

    with left:
        if os.path.exists(left_image): 
            c1, c2, c3 = st.columns([0.2, 0.6, 0.2], gap='small')
            with c2:
                st.image(left_image, width=180)
        else:
            st.write("Image not found")
    
    with center:
        
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 0px;">
                <h1 style="font-size: 2.5em; font-weight: bold; margin-top: -50px;">{title}</h1>
                <p style="font-size: 1.2em; color: gray;">{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        if os.path.exists(right_image): 
            c1, c2, c3 = st.columns([0.2, 0.6, 0.2], gap='small')
            with c2:
                st.image(right_image)
        else:
            st.write("Image not found")


@st.fragment
def footer():
    pass
