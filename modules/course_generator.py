import streamlit as st
import pandas as pd
import ollama
import os
from fpdf import FPDF  # Ensure you have fpdf installed via pip install fpdf

# Define main folder for PDF outputs (named "Users")
PDF_USERS_FOLDER = "Users"

# Ensure the main Users folder exists
if not os.path.exists(PDF_USERS_FOLDER):
    os.makedirs(PDF_USERS_FOLDER)

ASSESS_CSV = "data/assessments.csv"

def get_latest_preassess_difficulty(username):
    if not os.path.exists(ASSESS_CSV):
        return "Medium"
    df = pd.read_csv(ASSESS_CSV)
    df = df[df["username"].str.lower() == username.lower()]
    if df.empty:
        return "Medium"
    return df.iloc[-1]["difficulty"]

def build_prompt(course, education_level, difficulty):
    prompt = f"""
You are an AI tutor. Generate a detailed course outline for a {education_level} student on the course "{course}" tailored to a {difficulty} level.
Follow these instructions strictly:
- Use Markdown formatting.
- Output the course title as a top-level heading (e.g., "# Course Title: {course}").
- Then, for each module, output the module name as a numbered second-level heading (e.g., "## Module 1: [Module Title]") followed by the module content in essay format.
- The module content should be a continuous narrative that describes the topic, key concepts, and practical applications.
- Do not include any extra text such as greetings, follow-up questions, or redundant labels.
"""
    return prompt

def generate_course(course, education_level):
    username = st.session_state.get("username", "")
    difficulty = get_latest_preassess_difficulty(username)
    prompt = build_prompt(course, education_level, difficulty)
    
    placeholder = st.empty()
    full_response = ""
    
    with st.spinner("Generating course outline..."):
        response_stream = ollama.chat(
            model='gemma:2b',  # using the model gemma:2b
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        for chunk in response_stream:
            content = chunk['message']['content']
            full_response += content
            placeholder.markdown(full_response, unsafe_allow_html=True)
    
    st.success("Course generation complete!")
    
    # Provide two separate buttons for further action
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Study this course"):
            # Create a folder for the current user under the "Users" folder
            user_folder = os.path.join(PDF_USERS_FOLDER, username)
            if not os.path.exists(user_folder):
                os.makedirs(user_folder)
            # Create a folder for the course using the course name (spaces replaced by underscores)
            course_folder = os.path.join(user_folder, course.replace(" ", "_"))
            if not os.path.exists(course_folder):
                os.makedirs(course_folder)
            # Save the generated course outline as a PDF in the course folder
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, full_response)
            pdf_filename = os.path.join(course_folder, f"Course_Outline_{course.replace(' ', '_')}.pdf")
            pdf.output(pdf_filename)
            st.info(f"Course saved as PDF: {pdf_filename}")
    with col2:
        if st.button("Pick a different course"):
            st.info("Please use the course input above to generate a new course.")