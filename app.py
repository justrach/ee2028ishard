import time
import streamlit as st

import plotly.express as px
import main as mainfolder
import matplotlib as plt
start_button = st.empty()
placeholder = st.empty()
threeDeeplaceholder = st.empty()
def radar_chart(comments):  
    df = comments
    fig = px.line_polar(df, r='temperature', theta='pressure_sensor', line_close=True)
    placeholder.write(fig)
def threeDgraph(df):
    fig = px.scatter_3d(df, x='x', y='y', z='z',color = "temperature")
    threeDeeplaceholder.write(fig)

    

while True:
    comments = mainfolder.databaseAccess()
    time.sleep(1)
    radar_chart(comments)
    threeDgraph(comments)

