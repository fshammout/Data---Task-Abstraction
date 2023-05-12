import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import io
from pandas_profiling import ProfileReport


df = pd.read_csv("losses2015_transformed.csv")



buffer = io.StringIO()
df.info(buf=buffer)
df_info = buffer.getvalue()

st.write(df)

#1-#3
st.text(df_info)

#4
st.text("\nState Code: refers to the index of the state being used, as in 37 refers to NC and is of type int64\n")
st.text("State Abv: refers to the abreviation of the state being used, as in NC refers to North Carolina and is of type object\n")
st.text("Damage Code: refers to the index of the damage type being described, as in 97 refers to earthquake and is of type int64\n")
st.text("Damage Descp: refers to the type of damage being described, as in Earthquake refers to damage cause by an earthquake and is of type object\n")
st.text("Ammount: refers to the cost of damage that is being filed for and is of type int64\n")


#5 - 1
unique_state_abv = df['State_Abv'].unique()
print("#1 Unique values in State_Abv are : " , "\n")

for i in unique_state_abv :
    print(i)

#5 - 2
unique_damage_descp = df['Damage_Descp'].unique()
print("#2 Unique values in Damage_Descp are : " , "\n")

for i in unique_damage_descp :
    print(i)


#5 - 3
numeric_columns = df.select_dtypes(include = np.number)

min_df = numeric_columns.min()
print("Please find below minimum from each column of data with Numerical fields","\n", min_df, "\n")

max_df = numeric_columns.max()
print("Please find below maximum from each column of data with Numerical fields","\n", max_df)

# 6
st.text("Q1) What state had the highest loss ammount\n")
st.text("Q2) What was the most frequent Damage type\n")

#7 

st.text("Q1 - Can use a chart to compare. fields needed: State_Abv or State_Code and Amount. No transformation needed, no type change. Yes all data is provided. --> State_Code is 29 with 466744931 as highest amount\n")
st.text("Q2 - Can use a chart to compare but does not need one. fields needed Damage_Descp or Damage_Code. No transformation needed, no type change. Yes all data is provided. --> Damage_Code is 31 with 48 occurences\n")


#8

df2 = df[['State_Code','Amount']]

st._arrow_bar_chart(df2)