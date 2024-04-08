import streamlit as st 
import matplotlib as plt
import pandas as pd

st.write('cmpd traffic stops')

@st.cache_data
def load_data(csv):
        df=pd.read_csv(csv)
        return df



stops=pd.read_csv("Data/Officer_Traffic_Stops.csv")


