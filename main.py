import streamlit as st
import pandas as pd
import altair as alt

# App title
st.title("🌍 MBTI Distribution by Country")
st.write("Select an MBTI type to see the **Top 10 countries** with the highest ratio.")

# Load data
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI type selection
mbti_types = df.columns[1:]  # skip 'Country'
selected_type = st.selectbox("🔎 Choose MBTI type", mbti_types)

# Top 10 countries for the selected MBTI
top10 = df[['Country', selected_type]].sort_values(by=selected_type, ascending=False).head(10)

# Altair bar chart
chart = (
    alt.Chart(top10)
    .mark_bar(color="teal")
    .encode(
        x=alt.X(selected_type, title=f"{selected_type} ratio"),
        y=alt.Y("Country", sort='-x'),
        tooltip=["Country", selected_type]
    )
    .interactive()
)

st.altair_chart(chart, use_container_width=True)
