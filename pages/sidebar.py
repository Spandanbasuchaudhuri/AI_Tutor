# pages/sidebar.py
import streamlit as st

def render_sidebar():
    # Render a radio button in the sidebar with the pages in the desired order
    menu = st.sidebar.radio("Navigation", ["Login", "Preassessment", "Course Selection", "Content UI", "MCQ"])
    
    # Update query parameters using the new method
    if menu == "Login":
        st.query_params.update(page="login")
    elif menu == "Preassessment":
        st.query_params.update(page="preassessment")
    elif menu == "Course Selection":
        st.query_params.update(page="Course Selection")
    elif menu == "Content UI":
        st.query_params.update(page="content_ui")
    elif menu == "MCQ":
        st.query_params.update(page="mcq")
    
    return menu