import streamlit as st
from modules.authentication import login, register, load_users
from modules.profiles import profile
from modules.preassessment import preassessment
from modules.course_generator import generate_course

def main():
    st.set_page_config(page_title="AI Tutor", page_icon="📚")
    st.sidebar.title("🎓 AI Tutor Navigation")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""

    if st.session_state["logged_in"]:
        # Retrieve education level from the users CSV
        username = st.session_state.get("username", "")
        users = load_users()
        education = users.get(username, {}).get("education", "High School")
        
        page = st.sidebar.radio("Choose a page", [
            "Profile",
            "Pre-Assessment",
            "AI Course Generator"
        ])

        if page == "Profile":
            profile()

        elif page == "Pre-Assessment":
            preassessment(username, education)

        elif page == "AI Course Generator":
            # Inject custom CSS to widen the container on this page only.
            st.markdown(
                """
                <style>
                .reportview-container .main .block-container{
                    max-width: 100% !important;
                    padding-left: 2rem;
                    padding-right: 2rem;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.title("🧠 AI-Powered Course Generator")
            container = st.empty()
            with container.container():
                subject = st.text_input("Enter the subject you want to learn:")
                generate_button = st.button("Generate Course")
            if generate_button and subject:
                container.empty()  # Clear the input container
                generate_course(subject, education)

    else:
        auth_option = st.sidebar.radio("Choose an option", ["Login", "Register"])
        if auth_option == "Login":
            login()
        else:
            register()

if __name__ == "__main__":
    main()