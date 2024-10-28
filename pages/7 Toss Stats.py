import streamlit as st
import plotly.express as px

# Cache data loading
@st.cache_data
def load_data():
    return px.data.gapminder()

# Cache chart creation
@st.cache_data
def create_chart(df):
    return px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", log_x=True)


# Load and cache data
df = load_data()

if 'chart' not in st.session_state:
    st.session_state['chart'] = create_chart(df)

st.plotly_chart(st.session_state['chart'])
