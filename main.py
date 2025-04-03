import streamlit as st
import os
from course_gen import generate_outline_stream
 
# Set page config first, before any other st commands
st.set_page_config(page_title="Course Outline Generator", layout="centered")

# Automatically direct to login page if not logged in.
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.set_query_params(page="login")
    st.stop()

# Only import and render sidebar after set_page_config
from pages.sidebar import render_sidebar
menu = render_sidebar()
 
username = st.session_state.username
user_courses_root = os.path.join("users", username, "courses")
 
st.title("📘 Course Outline Generator (Gemma 2B via Ollama)")
 
course_topic = st.text_input("Enter the course topic:", "Data Structures & Algorithms")
generate_button = st.button("🎯 Generate Outline")
 
if 'outline_text' not in st.session_state:
    st.session_state.outline_text = ""
if 'outline_ready' not in st.session_state:
    st.session_state.outline_ready = False
 
if generate_button:
    prompt = (
        f"Create a clear, structured course outline on the topic '{course_topic}'. "
        "Include the course name, followed by 4 to 6 modules. For each module, provide a short description. "
        "Do not include lessons, exercises, or quizzes — only the outline and module summaries."
    )
     
    st.session_state.outline_text = ""
    st.session_state.outline_ready = False
    outline_container = st.empty()
     
    for partial in generate_outline_stream(prompt):
        st.session_state.outline_text = partial
        outline_container.markdown(f"**Generated Course Outline:**\n\n{st.session_state.outline_text}")
     
    st.session_state.outline_ready = True
 
if st.session_state.outline_ready:
    if st.button("✅ OK (Save Outline)"):
        safe_name = "".join(c for c in course_topic if c not in r'<>:"/\|?*').strip()
        course_folder = os.path.join(user_courses_root, safe_name)
        os.makedirs(course_folder, exist_ok=True)
        filename = os.path.join(course_folder, f"{safe_name}.outline")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(st.session_state.outline_text)
        st.success(f"Course outline saved as `{filename}`.")
        st.session_state.selected_outline = filename
        st.set_query_params(page="content_ui")