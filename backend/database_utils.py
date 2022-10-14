
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import User, Base


engine = create_engine(f"sqlite:///twitter_clone.db")

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)

user = User(email="admin", username="admin", hashed_password="123456", first_name="", last_name="",
            about_me="", is_admin=True)
session.add(user)
session.commit()

print(session.query(User).all())
