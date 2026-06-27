# import streamlit as st
# import requests

# st.set_page_config(page_title="Docker Demo")

# st.title("Docker + Streamlit Demo")

# name = st.text_input("Enter your name")

# if st.button("Submit"):

#     response = requests.get(
#         f"http://localhost:8000/greet/{name}"
#     )

#     data = response.json()

#     st.success(data["message"])


import streamlit as st
import requests
import os

st.set_page_config(page_title="Docker Demo")
st.title("Docker + Streamlit Demo")

# Fetch the backend URL from the environment, defaulting to localhost for local testing
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

name = st.text_input("Enter your name")

if st.button("Submit"):
    # Route the request using the environment variable
    response = requests.get(f"{BACKEND_URL}/greet/{name}")
    
    if response.status_code == 200:
        data = response.json()
        st.success(data["message"])
    else:
        st.error("Failed to connect to the backend.")