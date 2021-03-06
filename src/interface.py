import streamlit as st
import time
import numpy as np
import pandas as pd
from streamlit.server.server import Server
from gauss_p_pivoting import Gauss_partial_pivoting


st.title("Método da Eliminação de Gauss com Pivoteamento")
st.write("#")

st.header("Sistema")
st.write("#")


col1, col2, col3,col4,col5, col6 = st.columns([2.5,2.5,2.5,0.5,0.5,2.5])
with col1:
    a00 = st.number_input("a00", min_value = -99, max_value=99, value=4, step=1)
    a10 = st.number_input("a10", min_value = -99, max_value=99, value=15, step=1)
    a20 = st.number_input("a20", min_value = -99, max_value=99, value=5, step=1)
    

with col2:
    a01 = st.number_input("a01", min_value = -99, max_value=99, value=2, step=1)
    a11 = st.number_input("a11", min_value = -99, max_value=99, value=4, step=1)
    a21 = st.number_input("a21", min_value = -99, max_value=99, value=8, step=1)

with col3:
    a02 = st.number_input("a02", min_value = -99, max_value=99, value=20, step=1)
    a12 = st.number_input("a12", min_value = -99, max_value=99, value=10, step=1)
    a22 = st.number_input("a22", min_value = -99, max_value=99, value=5, step=1)

with col4:
    st.write("#")
    st.write("  x0")
    st.write("#")
    st.write("  x1")
    st.write("#")
    st.write("  x2")

with col5:
    st.write("#")
    st.write("=")
    st.write("#")
    st.write("=")
    st.write("#")
    st.write("=")

with col6:
    b0 = st.number_input("b0", min_value = -99, max_value=99, value=4, step=1)
    b1 = st.number_input("b1", min_value = -99, max_value=99, value=5, step=1)
    b2 = st.number_input("b2", min_value = -99, max_value=99, value=8, step=1)

gauss = Gauss_partial_pivoting(a00,a10,a20,a01,a11,a21,a02,a12,a22,b0,b1,b2)

a = gauss.elimination()


pivot_list = a["pivot_list"]
equation_list = a["equation_list"]
matrix_list = a["matrix_list"]
matrix_solution_list = a["matrix_solution_list"]
results_list = a["results_list"]

st.markdown("***")
st.header("Resultado do Sistema:")
for i in range(len(results_list)):
    st.write(results_list[i])

for i in range(len(equation_list)):
    st.markdown("### Pivô: " + str(pivot_list[i]))

    st.markdown("### Equação: " + str(equation_list[i]))
    st.write("#")

    col1, col2 = st.columns([2,1])
    with col1:
        st.write(matrix_list[i])
    with col2:
        st.write(matrix_solution_list[i])
