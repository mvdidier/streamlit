import streamlit as st

st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)
# Disable widgets to remove interactivity:
st.slider("Pick a number", 0, 100, disabled=True)
