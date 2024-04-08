import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

@st.cache_data
def load_data(csv):
        df=pd.read_csv(csv)
        return df



stops=load_data("Data/Officer_Traffic_Stops.csv")

data=stops[['Driver_Age']]
plt.hist(data, bins=70 , color='blue', alpha=0.7) 
plt.xlabel('Driver_Age')
plt.ylabel('Frequency')
plt.title('Histogram')

st.pyplot(plt)

# Adding a violin plot!
sns.violinplot(data=stops, x="Was_a_Search_Conducted", y='Driver_Age')