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
# gauss = Gauss_partial_pivoting(4,15,5,2,4,8,20,10,5,4,5,8)

a = gauss.elimination()
print(a)

pivot_list = a["pivot_list"]
equation_list = a["equation_list"]
matrix_list = a["matrix_list"]
matrix_solution_list = a["matrix_solution_list"]
results_list = a["results_list"]
results = list(results_list)
matrix = list(matrix_list)

st.markdown("***")
st.header("Resultado do Sistema:")
st.write(str(results_list[0]).split())

st.write(matrix_list)



# st.write("x0 =  " + str(results_list[0]))
# st.write("x1 =  " + str(results_list[1]))
# st.write("x2 =  " + str(results_list[2]))

for i in range(len(equation_list) - 1):
    st.markdown("### Pivô: " + str(pivot_list[i]))

    st.markdown("### Equação: " + str(equation_list[i]))
    st.write("#")

    st.write(matrix_list)

    col1, col2, col3,col4,col5, col6 = st.columns(6)
    with col1:
        st.write(matrix_list[i])
        st.write(a10)
        st.write(a20)

    with col2:
        st.write(a01)
        st.write(a11)
        st.write(a21)

    with col3:
        st.write(a02)
        st.write(a12)
        st.write(a22)

    with col4:
        st.write("x0")
        st.write("x1")
        st.write("x2")

    with col5:
        st.write("=")
        st.write("=")
        st.write("=")

    with col6:
        st.write(b0)
        st.write(b1)
        st.write(b2)
