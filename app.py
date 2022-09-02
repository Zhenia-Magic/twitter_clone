import streamlit as st
from storage import UserStorage
from models import User

user_store = UserStorage()
user_store.add_user(User(email="admin", username="admin", hashed_password="123456", first_name="", last_name="",
                         about_me="", is_admin=True))

st.title("Main Page")
