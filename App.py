import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
a=pd.read_csv('https://api.covid19india.org/csv/latest/state_wise.csv')
a
st.sidebar.title("visualization selector")
