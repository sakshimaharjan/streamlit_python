import streamlit as st
from src.student.create import multiplicationtable, check_primenum

number = st.slider('Choose a number: ', 0, 130, 25)

if check_primenum(number):
    multiplicationtable(number)
else:
    st.write("Not prime")