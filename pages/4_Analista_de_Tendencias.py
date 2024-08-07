import streamlit as st
import pandas as pd
from langchain_community.tools.google_trends import GoogleTrendsQueryRun
from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper
import time
from utils import search_google_trends #import SERPAPI_API_KEY,
from streamlit_extras.app_logo import add_logo

#add_logo("https://www.python.org/static/community_logos/python-powered-w-100x40.png", height=1)
st.title('Analista de Google Trends')

# Input keyword from user
keyword = st.text_input("Ingrese palabra claves a buscar en Google Trends", "Ex: Python")

# Get data for the keyword
try:
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.subheader('Google Trends Data Wrapper')
        with st.spinner('Pensando...'):
            tool = GoogleTrendsQueryRun(api_wrapper=GoogleTrendsAPIWrapper())
            response = tool.run(keyword)
            st.write(response)

    with col2:
        st.subheader('Google Trends SerpAPI')
        with st.spinner('Pensando...'):
            response = search_google_trends(keyword)
            st.write(response)

except Exception as e:
    st.error(e)


