import streamlit as st
import base64
import requests

st.set_page_config(page_title='Hamidov Siyovush', page_icon=None, initial_sidebar_state='auto')
st.title("  Hamido1 Siyovush's")
st.title("Certificates and Courses")

ExpData = '11AnC1jZwve4YsvSbr9-mS-v6q5ZmpoAm'
FundScal = '1hzgd6LaYpzyCELeQ9kTL4F4uy3du7JYP'
ToolsForDS = '13a2T84g1JNiKfEMmvKs9Z7BFcEJK2VEB'
Django = '103zM5cLiqrxm4P8GQ1saP9a9rUQIuN5q'

ExpDataURL = f'https://drive.google.com/file/d/{ExpData}/view'
FundScalURL = f'https://drive.google.com/file/d/{FundScal}/view'
ToolsForDSURL = f'https://drive.google.com/file/d/{ToolsForDS}/view'
DjangoURL = f'https://drive.google.com/file/d/{Django}/view'

st.markdown(f'**PDF:** [Exploratory Data Analysis for Machine Learning]({ExpDataURL})')
st.markdows('https://www.coursera.org/account/accomplishments/verify/B32838V98B53]')
