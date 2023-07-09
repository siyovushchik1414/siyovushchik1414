import streamlit as st
import base64
import requests

st.set_page_config(page_title='Hamidov Siyovush', page_icon=None, initial_sidebar_state='auto')
st.title("  Hamido1 Siyovush's")
st.title("Certificates and Courses")

file_id = '11AnC1jZwve4YsvSbr9-mS-v6q5ZmpoAm'
file_url = f'https://drive.google.com/file/d/{file_id}/view'

st.markdown(f'**PDF:** [link]({file_url})')
