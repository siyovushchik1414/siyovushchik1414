import streamlit as st
import base64
import requests

st.set_page_config(page_title='Hamidov Siyovush', page_icon=None, initial_sidebar_state='auto')
st.title("  Hamido1 Siyovush's")
st.title("Certificates and Courses")

pdf_url = "https://drive.google.com/uc?id=11AnC1jZwve4YsvSbr9-mS-v6q5ZmpoAm"
pdf_viewer_url = f"http://docs.google.com/gview?url={pdf_url}&embedded=true"

st.components.v1.iframe(pdf_viewer_url, width=800, height=1000)
