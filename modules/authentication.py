import streamlit as st
import pandas as pd
import os

USER_CSV_FILE = "data/users.csv"

def load_users():
    if not os.path.exists(USER_CSV_FILE):
        os.makedirs("data", exist_ok=True)
        df = pd.DataFrame(columns=["username", "name", "password", "age", "education"])
        df.to_csv(USER_CSV_FILE, index=False)

    df = pd.read_csv(USER_CSV_FILE, dtype={
        "username": str,
        "name": str,
        "password": str,
        "age": str,
        "education": str
    })

    users = {}
    for _, row in df.iterrows():
        key = str(row["username"]).strip()
        users[key] = {
            "name": str(row["name"]).strip(),
            "password": str(row["password"]).strip(),
            "age": str(row.get("age", "")).strip(),
            "education": str(row.get("education", "")).strip()
        }
    return users

def save_user(username, name, password, age, education):
    username = str(username).strip()
    name = str(name).strip()
    password = str(password).strip()
    age = int(age)
    education = str(education).strip()

    df = pd.DataFrame([[username, name, password, age, education]],
                      columns=["username", "name", "password", "age", "education"])
    df.to_csv(USER_CSV_FILE, mode="a", index=False, header=not os.path.exists(USER_CSV_FILE))

def register():
    st.title("📝 Register for AI Tutor")

    username = st.text_input("Choose a Username").strip()
    name = st.text_input("Full Name").strip()
    password = st.text_input("Create Password", type="password").strip()
    age = st.number_input("Age", min_value=10, max_value=19, step=1)
    education = st.selectbox("Education Level", ["Elementary School", "Middle School", "High School"])

    if st.button("Register"):
        if username == "" or name == "" or password == "":
            st.warning("Please fill in all fields.")
            return

        users = load_users()
        if username in users:
            st.error("Username already exists!")
        else:
            save_user(username, name, password, age, education)
            st.success("🎉 Registration successful. You can now log in!")

def login():
    st.title("🔐 Login to AI Tutor")
    username_input = st.text_input("Username").strip()
    password = st.text_input("Password", type="password").strip()

    if st.button("Login"):
        users = load_users()
        matched_username = None
        for stored_username in users:
            if stored_username.strip().lower() == username_input.lower():
                matched_username = stored_username
                break

        if matched_username is None:
            st.error("Username not found.")
        elif users[matched_username]["password"] != password:
            st.error("Incorrect password.")
        else:
            st.session_state["logged_in"] = True
            st.session_state["username"] = matched_username
            st.rerun()