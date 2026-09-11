import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="IPL Analytics",
    page_icon="🏏",
    layout="wide"
)

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login Form
st.title("IPL Analytics")
st.subheader("Login / Sign In")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username == "Thrishika" and password == "thrishika4152":
        st.session_state.logged_in = True

        st.success("Login successful!")

        st.switch_page("pages/1_About_Project.py")

    else:
        st.error("Invalid username or password.")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False

    st.switch_page("app.py")
