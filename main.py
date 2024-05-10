import streamlit as st
from utils import get_wikipedia_answer

st.title("Ask the Wikipedia using Tools")
st.write("*Query*")
query = st.text_input("Enter your query Here")

if query:
    st.write(get_wikipedia_answer(query))
