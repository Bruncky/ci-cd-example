import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from api.fast import root

st.write(root())

st.write('This is obviously very simple, in reality one would rather use this page to display API results more nicely! :)')
st.write('Add anythin here')

x = np.linspace(1, 20)
y = np.sin(x)
fig = plt.plot(x,y)

st.write(f'My plot {fig}')