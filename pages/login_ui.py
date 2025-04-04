import streamlit as st
from auth.login import verify_user
from auth.register import register_user
from auth.profiles import get_user_profile
import os

# Set page config
st.set_page_config(page_title="Login", layout="centered")

# Get the current page from query parameters
current_page = st.query_params.get("page", "login")

# Main login page
if current_page == "login":
    st.title("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            if username and password:
                user = verify_user(username, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.user_profile = user
                    st.query_params["page"] = "main"
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid username or password")
            else:
                st.error("Please enter both username and password")
    with col2:
        if st.button("Register"):
            st.query_params["page"] = "register"
            st.rerun()

# Register page
elif current_page == "register":
    st.title("Register")
    
    full_name = st.text_input("Full Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    age = st.text_input("Age")
    school_level = st.selectbox("School Level", ["Elementary School", "Middle School", "High School", "College"])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Create Account"):
            if full_name and username and password and confirm_password and age:
                if password != confirm_password:
                    st.error("Passwords do not match")
                else:
                    success, message = register_user(full_name, username, password, age, school_level)
                    if success:
                        st.success(message)
                        st.query_params["page"] = "login"
                        st.rerun()
                    else:
                        st.error(message)
            else:
                st.error("Please fill in all fields")
    with col2:
        if st.button("Back to Login"):
            st.query_params["page"] = "login"
            st.rerun()