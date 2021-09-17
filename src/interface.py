import streamlit as st
import time
import numpy as np
import pandas as pd
from bissection import Bissection

st.title('Método da Eliminação de Gauss')

order = st.sidebar.number_input("Ordem do sistema: ", min_value = -10, max_value=10, value=0, step=1) 
st.markdown("## Sistema")

st.markdown("## Pivô")


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")