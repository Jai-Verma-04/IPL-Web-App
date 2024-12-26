import os
import streamlit as st
import datetime
from utils.image_markdown import img_to_html

@st.fragment
def header(title, description, right_image="static/icons/ipl logo.png", left_image="static/icons/IPLAnalytica.png"):
    left, center, right = st.columns([0.2, 0.6, 0.2], gap='medium', vertical_alignment='top')

    with left:
        if os.path.exists(left_image): 
            c = st.columns([0.2, 0.6, 0.2], gap='small')
            with c[1]:
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
            c = st.columns([0.2, 0.6, 0.2], gap='small')
            with c[1]:
                st.image(right_image)
        else:
            st.write("Image not found")


import datetime

@st.fragment
def footer():
    current_year = datetime.datetime.now().year
    st.divider()
    cols = st.columns([1, 1, 1], gap='medium')
    
    with cols[1]:
        st.write(f"© {current_year} IPL Analytica")
        st.write("[Contact](mailto:vermajai2004@gmail.com)")

    with cols[0]:
        center_cols = st.columns([1, 1, 1], gap="small")
        
        with center_cols[0]:
            st.image("static/icons/linkedin.png", width=50)
            st.write("[LinkedIn](https://linkedin.com/in/jai-verma)")
        
        with center_cols[1]:
            st.image("static/icons/github.png", width=50)
            st.write("[GitHub](https://github.com/Jai-Verma-04)")

    with cols[2]:
        st.write("[Portfolio - Coming Soon]()")
        st.write("[Get data used in the project here 📌](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)")
            


