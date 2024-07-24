import streamlit as st
st.set_page_config(
    page_title="My Custom Streamlit App",
    page_icon='Vector (1).png',
    layout="centered",
)
input1 = st.text_input('')
btn1 = st.button('sumbit')
title = ''
if btn1:
    title = st.write('###',input1)