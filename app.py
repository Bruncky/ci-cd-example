import streamlit as st

from api.fast import root

st.write(root())

st.write('ah! This is obviously very simple, in reality one would rather use this page to display API results more nicely! :)')
