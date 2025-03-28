import streamlit as st
import pandas as pd
import os

def load_quiz_df(education):
    path_map = {
        "Elementary School": "data/Elementary_MCQ_Full_Set.csv",
        "Middle School": "data/Middle_School_MCQ_Test_Full.csv",
        "High School": "data/High_School_MCQ_Test_Full.csv"
    }
    df = pd.read_csv(path_map[education])
    if "Answer Key" in df.columns:
        df = df.rename(columns={"Answer Key": "Correct Answer"})
    return df

def calculate_difficulty(score, total_questions):
    percentage = (score / total_questions) * 100
    if percentage < 30:
        return "Easy"
    elif 30 <= percentage <= 70:
        return "Medium"
    else:
        return "Hard"

def preassessment(username, education):
    csv_path = "data/assessments.csv"
    # Check if a preassessment record exists for the current user
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        if not df[df["username"].str.lower() == username.lower()].empty:
            st.info("Test already Taken")
            return

    st.subheader(f"🧪 Pre-Assessment: {education} Level")

    # Only sample once per session
    if "quiz_data" not in st.session_state:
        df = load_quiz_df(education)
        st.session_state["quiz_data"] = df.sample(n=50).reset_index(drop=True)

    sample = st.session_state["quiz_data"]
    user_answers = {}

    for i, row in sample.iterrows():
        q = row["Question"]
        options = [row["Option A"], row["Option B"], row["Option C"], row["Option D"]]
        user_answers[i] = st.radio(f"{i+1}. {q}", options, key=f"pre_q_{i}")

    if st.button("Submit Pre-Assessment"):
        correct = 0
        for i, row in sample.iterrows():
            answer_key = row["Correct Answer"].strip().upper()
            correct_option = {
                "A": row["Option A"],
                "B": row["Option B"],
                "C": row["Option C"],
                "D": row["Option D"]
            }.get(answer_key, "")
            if user_answers[i].strip() == correct_option.strip():
                correct += 1

        st.success(f"✅ You scored {correct} out of {len(sample)}")

        difficulty = calculate_difficulty(correct, len(sample))
        st.write(f"Course Difficulty: **{difficulty}**")

        # Save results to CSV
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(csv_path):
            pd.DataFrame(columns=["username", "education", "score", "difficulty"]).to_csv(csv_path, index=False)

        pd.DataFrame([[username, education, correct, difficulty]], 
                     columns=["username", "education", "score", "difficulty"])\
            .to_csv(csv_path, mode="a", index=False, header=False)

        st.balloons()

        # Clear quiz for future reuse if needed
        del st.session_state["quiz_data"]