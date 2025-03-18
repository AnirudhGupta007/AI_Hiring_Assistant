import streamlit as st
import requests

# Streamlit UI Setup
st.set_page_config(page_title="AI Hiring Assistant 🤖", layout="wide")
st.title("AI Hiring Assistant 🤖")
st.subheader("Your smart interview partner!")

# Sidebar: Collect Candidate Info
st.sidebar.header("Candidate Information ✍️")
name = st.sidebar.text_input("Full Name")
email = st.sidebar.text_input("Email")
phone = st.sidebar.text_input("Phone")
experience = st.sidebar.number_input("Years of Experience", min_value=0, max_value=50, step=1)
position = st.sidebar.text_input("Desired Position")
location = st.sidebar.text_input("Current Location")
tech_stack = st.sidebar.text_area("Tech Stack (comma-separated)").split(",")

if st.sidebar.button("Start Interview 🚀"):
    candidate_data = {
        "full_name": name,
        "email": email,
        "phone": phone,
        "years_of_experience": experience,
        "desired_position": position,
        "current_location": location,
        "tech_stack": tech_stack,
    }
    response = requests.post("http://127.0.0.1:8000/collect_info", json=candidate_data)
    if response.status_code == 200:
        questions = response.json()["questions"]
        st.session_state["messages"] = [("🤖", "Thanks! Let's start your interview.")]
        for question in questions:
            st.session_state["messages"].append(("🤖", question))

# Chat Interface
st.markdown("### Interview Chat 💬")
if "messages" in st.session_state:
    for sender, msg in st.session_state["messages"]:
        st.write(f"**{sender}**: {msg}")

# User Input Box
user_input = st.text_input("Your Answer ✍️")
if st.button("Send") and user_input:
    st.session_state["messages"].append(("👤", user_input))




