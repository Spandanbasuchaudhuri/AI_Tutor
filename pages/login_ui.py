import streamlit as st
from auth.login import verify_user
from auth.register import register_user

st.set_page_config(page_title="User Login and Registration", layout="centered")
st.title("User Login and Registration")

# Initialize session state for login status and page navigation.
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# Check if user is already logged in
if st.session_state.logged_in:
    st.header(f"WELCOME BACK {st.session_state.username}")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.user_profile = None
        st.session_state.page = "login"
        st.rerun()
else:
    # Use a radio button in the sidebar to switch between Login and Register views.
    menu_choice = st.sidebar.radio("Menu", ["Login", "Register"], key="login_menu")

    if menu_choice == "Login":
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = verify_user(username, password)
            if user:
                st.success("Logged in successfully!")
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.user_profile = user
                # Instead of updating query parameters, update a session state variable.
                st.session_state.page = "main"
                st.rerun()  # Rerun the app to show the welcome message
            else:
                st.error("Invalid username or password")

    elif menu_choice == "Register":
        st.header("Register")
        full_name = st.text_input("Full Name")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        # Age input is restricted between 8 and 21.
        age = st.number_input("Age", min_value=8, max_value=21, step=1)
        school_level = st.selectbox("School Level", ["Elementary School", "Middle School", "High School"])
        if st.button("Register"):
            success, message = register_user(full_name, username, password, age, school_level)
            if success:
                st.success(message)
            else:
                st.error(message)