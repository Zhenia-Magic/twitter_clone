import streamlit as st
from backend.utils import email_is_valid
from backend.storage import LOGGED_IN, INCORRECT_PASSWORD, NO_USER_FOUND
from backend.models import User
from backend.api import verify_user
from backend.database import session
from backend.database_utils import add_user_to_db

st.title("Users")

user_option = st.radio("Do you want to log in or sign up?",
                       ("Log In", "Sign Up"), index=0)

if user_option == "Log In":
    st.subheader("Log In Form")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    login_button = st.button("Log In")
    if login_button:
        result = verify_user(session, email, password)
        if result == NO_USER_FOUND:
            st.write("User is not found.")
        elif result == LOGGED_IN:
            st.write(f"User with email {email} and password {password} is logged in.")
        elif result == INCORRECT_PASSWORD:
            st.write("Password is not correct.")

elif user_option == "Sign Up":
    invalid_input_pass = False
    invalid_input_conf_pass = False
    invalid_input_email = False
    invalid_input_last_name = False
    invalid_input_first_name = False
    invalid_input_username = False
    st.subheader("Sing Up Form")
    email = st.text_input("Email")

    if email_is_valid(email):
        invalid_input_email = False
    else:
        invalid_input_email = True
        st.error("Email is not valid")

    username = st.text_input('Username')
    if len(username) < 2:
        invalid_input_username = True
        st.error("username must be longer than 1 symbol")
    else:
        invalid_input_username = False
    first_name = st.text_input('First name')
    if len(first_name) < 2:
        invalid_input_first_name = True
        st.error("First name must be longer than 1 symbol")
    else:
        invalid_input_first_name = False
    last_name = st.text_input('Last name')
    if len(last_name) < 2:
        invalid_input_last_name = True
        st.error("Last name must be longer than 1 symbol")
    else:
        invalid_input_last_name = False
    password = st.text_input("Create a password", type="password")

    if len(password) < 8:
        invalid_input_pass = True
        st.error("Password must be longer than 8 symbols")
    else:
        invalid_input_pass = False

    conf_password = st.text_input("Confirm a password", type="password")

    if password != conf_password:
        invalid_input_conf_pass = True
        st.error("Passwords are not the same")
    else:
        invalid_input_conf_pass = False

    if any([invalid_input_pass, invalid_input_conf_pass, invalid_input_email]):
        sign_up_button = st.button("Sign Up", disabled=True)
    else:
        sign_up_button = st.button("Sign Up")

    if sign_up_button:
        if password != conf_password:
            st.write('Passwords do not match')
        else:
            if verify_user(session, email, password) == NO_USER_FOUND:
                result = add_user_to_db(session, email, username, last_name, first_name, password, '', False)
                st.write(f"User with email {email} and password {password} is signed up.")
            else:
                st.write('User already exist')
