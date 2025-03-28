import streamlit as st
from modules.authentication import load_users
import pandas as pd

USER_CSV_FILE = "data/users.csv"

def profile():
    users = load_users()
    username = st.session_state.get("username")

    if username not in users:
        st.error("User not found.")
        return

    user = users[username]

    st.title("👤 User Profile")
    st.write(f"**Username**: {username}")
    st.write(f"**Full Name**: {user['name']}")
    st.write(f"**Age**: {user.get('age', 'N/A')}")
    st.write(f"**Education Level**: {user.get('education', 'N/A')}")

    st.markdown("---")
    st.subheader("✏️ Edit Profile")

    new_name = st.text_input("Full Name", value=user["name"])

    try:
        age_value = int(user.get("age", 10))
        if age_value < 10 or age_value > 19:
            age_value = 10
    except:
        age_value = 10

    new_age = st.number_input("Age", min_value=10, max_value=19, step=1, value=age_value)

    edu_levels = ["Elementary School", "Middle School", "High School"]
    current_edu = user.get("education", "High School")
    if current_edu not in edu_levels:
        current_edu = "High School"
    index = edu_levels.index(current_edu)

    new_edu = st.selectbox("Education Level", edu_levels, index=index)

    if st.button("Update Profile"):
        df = pd.read_csv(USER_CSV_FILE, dtype={"username": str})
        df["username"] = df["username"].astype(str)
        df.loc[df["username"].str.lower() == username.lower(), "name"] = new_name
        df.loc[df["username"].str.lower() == username.lower(), "age"] = int(new_age)
        df.loc[df["username"].str.lower() == username.lower(), "education"] = new_edu
        df.to_csv(USER_CSV_FILE, index=False)
        st.success("Profile updated! Refreshing...")
        st.rerun()