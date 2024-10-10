import streamlit as st

st.header("The greenest people of the month ")
st.subheader("how green are you?")

import tabulate

head = ["Username", "Score"]

mydata = [
    ["alona", "100"],
    ["mia", "92"],
    ["alisa", "79"],
      ["elia", "66"]
]

table = tabulate.tabulate(mydata, headers=head)
st.text(f"{table}")