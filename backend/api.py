from database_utils import check_password_by_email
NO_USER_FOUND = "No user found with this email"
INCORRECT_PASSWORD = "Incorrect password"
LOGGED_IN = "Logged In"


def verify_user(session, email, password):
    try:
        logged_in = check_password_by_email(session, email, password)
    except ValueError:
        return NO_USER_FOUND
    if logged_in:
        return LOGGED_IN
    else:
        return INCORRECT_PASSWORD
