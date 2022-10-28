from models import User
from utils import email_is_valid


def add_user_to_db(session, email, username, last_name, first_name,
                   hashed_password, about_me, is_admin):
    if len(username) < 1:
        raise ValueError("Username must be longer than 1 symbol")
    if not email_is_valid(email):
        raise ValueError("Email is invalid")
    if len(first_name) < 1:
        raise ValueError("First name must be longer than 1 symbol")
    if len(last_name) < 1:
        raise ValueError("Last name must be longer than 1 symbol")
    if len(hashed_password) < 8:
        raise ValueError("Password must be longer than 8 symbols")

    user = User(email=email, username=username, hashed_password=hashed_password,
                first_name=first_name, last_name=last_name,
                about_me=about_me, is_admin=is_admin)
    session.add(user)
    session.commit()


def check_username(session, username):
    return session.query(User).where(User.username == username).first() is not None


def check_password_by_username(session, username, password):
    if not check_username(session, username):
        raise ValueError("User does not exist")
    return session.query(User).where(User.username == username).first().hashed_password == password


def check_email(session, email):
    return session.query(User).where(User.email == email).first() is not None


def check_password_by_email(session, email, password):
    if not check_email(session, email):
        raise ValueError("User does not exist")
    return session.query(User).where(User.email == email).first().hashed_password == password
