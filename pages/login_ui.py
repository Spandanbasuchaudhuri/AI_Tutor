import streamlit as st
from auth.login import verify_user
from auth.register import register_user
from auth.profiles import get_user_profile
import os

# Make the page wide
st.set_page_config(layout="wide")

current_page = st.query_params.get("page", ["login"])[0]  # default to "login"

# Create a top-level 3‑column layout so everything is centered.
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    if current_page == "login":
        st.title("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # -- Center the Login button in a new row of columns
        login_btn_left, login_btn_mid, login_btn_right = st.columns([2, 1, 2])
        with login_btn_mid:
            if st.button("Login", use_container_width=True):
                if username and password:
                    user = verify_user(username, password)
                    if user:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.user_profile = user
                        st.query_params["page"] = "main"
                        full_name = user.get("full_name", username)
                        st.success(f"Login successful! Hello {full_name}, it's great to see you again.")
                        st.rerun()
                    else:
                        st.error("Invalid username or password")
                else:
                    st.error("Please enter both username and password")

        # -- Insert "OR" in a separate row of columns and center the text
        or_text_left, or_text_mid, or_text_right = st.columns([2, 1, 2])
        with or_text_mid:
            st.markdown("<p style='text-align: center; font-weight: bold;'>OR</p>", unsafe_allow_html=True)

        # -- Center the "Register New User" button in its own row
        reg_btn_left, reg_btn_mid, reg_btn_right = st.columns([2, 1, 2])
        with reg_btn_mid:
            if st.button("Register New User", use_container_width=True):
                st.query_params["page"] = "register"
                st.rerun()

    elif current_page == "register":
        st.title("Register")

        full_name = st.text_input("Full Name")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        age = st.text_input("Age")
        school_level = st.selectbox(
            "School Level", ["Elementary School", "Middle School", "High School", "College"]
        )

        # Make "Create Account" wide, centered
        create_btn_left, create_btn_mid, create_btn_right = st.columns([2, 1, 2])
        with create_btn_mid:
            if st.button("Create Account", use_container_width=True):
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

        # Center + widen the "Back to Login" button
        back_btn_left, back_btn_mid, back_btn_right = st.columns([2, 1, 2])
        with back_btn_mid:
            if st.button("Back to Login", use_container_width=True):
                st.query_params["page"] = "login"
                st.rerun()