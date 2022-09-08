import streamlit as st
from app import user_store
from storage import LOGGED_IN, INCORRECT_PASSWORD, NO_USER_FOUND

st.title("Users")

user_option = st.radio("Do you want to log in or sign up?",
                       ("Log In", "Sign Up"), index=0)

if user_option == "Log In":
    st.subheader("Log In Form")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    login_button = st.button("Log In")
    if login_button:
        st.write(user_store.users)
        result = user_store.verify_user(email, password)
        if result == NO_USER_FOUND:
            st.write("User is not found.")
        elif result == LOGGED_IN:
            st.write(f"User with email {email} and password {password} is logged in.")
        elif result == INCORRECT_PASSWORD:
            st.write("Password is not correct.")

elif user_option == "Sign Up":
    st.subheader("Sing Up Form")
    email = st.text_input("Email")
    username = st.text_input('Username')
    first_name = st.text_input('First name')
    last_name = st.text_input('Last name')
    password = st.text_input("Create a password", type="password")
    conf_password = st.text_input("Confirm a password", type="password")
    sign_up_button = st.button("Sign Up")
    if sign_up_button:
        if password != conf_password:
            st.write('Passwords do not match')
            conf_password = st.text_input("Confirm a password", type="password")
        st.write(user_store.users)
        result = user_store.add_user(email, password, username, first_name, last_name)
        st.write(f"User with email {email} and password {password} is signed up.")

