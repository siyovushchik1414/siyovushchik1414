import streamlit as st
import base64
import requests

st.set_page_config(page_title='Hamidov Siyovush', page_icon=None, initial_sidebar_state='auto')
st.title("  Hamido1 Siyovush's")
st.title("Certificates and Courses")

st.markdown(f'**Website:** [Exploratory Data Analysis for Machine Learning]({https://www.coursera.org/account/accomplishments/verify/B32838V98B53})')


from pdf2image import convert_from_path

# Замените 'path/to/file.pdf' на соответствующее значение
images = convert_from_path('Exploratory Data Analysis for Machine Learning.pdf')

for image in images:
    st.image(image)
