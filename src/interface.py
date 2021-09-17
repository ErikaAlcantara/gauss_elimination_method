import streamlit as st
import time
import numpy as np
import pandas as pd
from streamlit.server.server import Server


st.title('Método da Eliminação de Gauss')

# order = st.sidebar.number_input("Ordem do sistema: ", min_value = -10, max_value=10, value=0, step=1) 

st.header("Sistema")


col1, col2, col3,col4 = st.columns(4)
with col1:
    x0 = st.number_input("x0", min_value = -10, max_value=10, value=0, step=1)
    x1 = st.number_input("x1", min_value = -10, max_value=10, value=0, step=1)
    x2 = st.number_input("x2", min_value = -10, max_value=10, value=0, step=1)
    

with col2:
    y0 = st.number_input("y0", min_value = -10, max_value=10, value=0, step=1)
    y1 = st.number_input("y1", min_value = -10, max_value=10, value=0, step=1)
    y2 = st.number_input("y2", min_value = -10, max_value=10, value=0, step=1)

with col3:
    z0 = st.number_input("z0", min_value = -10, max_value=10, value=0, step=1)
    z1 = st.number_input("z1", min_value = -10, max_value=10, value=0, step=1)
    z2 = st.number_input("z2", min_value = -10, max_value=10, value=0, step=1)

with col4:
    r0 = st.number_input("r0", min_value = -10, max_value=10, value=0, step=1)
    r1 = st.number_input("r1", min_value = -10, max_value=10, value=0, step=1)
    r2 = st.number_input("r2", min_value = -10, max_value=10, value=0, step=1)

st.markdown("***")
st.header("Resultado") 
st.markdown("### Pivô: ")
st.markdown("### Equação: ")
st.write("#")


col1, col2, col3,col4 = st.columns(4)
with col1:
    st.write(x0)
    st.write(x1)
    st.write(x2)

with col2:
    st.write(y0)
    st.write(y1)
    st.write(y2)

with col3:
    st.write(z0)
    st.write(z1)
    st.write(z2)

with col4:
    st.write(r0)
    st.write(r1)
    st.write(r2)

