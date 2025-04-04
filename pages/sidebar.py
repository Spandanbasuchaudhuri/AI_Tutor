# pages/sidebar.py
import streamlit as st

def render_sidebar():
    """
    Renders the navigation sidebar and handles page routing.
    Returns the selected menu item.
    """
    # Only show navigation options if user is logged in
    if not st.session_state.get("logged_in", False):
        return None
    
    # Render a radio button in the sidebar with the pages in the desired order
    menu = st.sidebar.radio("Navigation", ["Main", "Preassessment", "Course Selection", "Content UI", "MCQ"])
    
    # Update query parameters using consistent naming convention
    if menu == "Main":
        st.query_params["page"] = "main"
    elif menu == "Preassessment":
        st.query_params["page"] = "preassessment"
    elif menu == "Course Selection":
        st.query_params["page"] = "course_selection"
    elif menu == "Content UI":
        st.query_params["page"] = "content_ui"
    elif menu == "MCQ":
        st.query_params["page"] = "mcq"
    
    return menu