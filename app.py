import streamlit as st
import requests
import base64
  
def main():
  st.set_page_config(page_title='Hamidov Siyovush', page_icon=None, initial_sidebar_state='auto')
  st.title("  Hamidov Siyovush's")
  st.title("Certificates and Courses")

  pdf_url = "https://drive.google.com/uc?id=11AnC1jZwve4YsvSbr9-mS-v6q5ZmpoAm"
  
  # Download the PDF file from Google Drive
  response = requests.get(pdf_url)
  pdf_content = response.content
  
  # Encode the PDF content using base64 and display it using st.markdown
  base64_pdf = base64.b64encode(pdf_content).decode('utf-8')
  pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
  st.markdown(pdf_display, unsafe_allow_html=True)

if __name__ == "__main__":
  main()


