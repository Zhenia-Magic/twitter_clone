from importlib import resources

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


with resources.path(
        "project.data", "author_book_publisher.db"
) as sqlite_filepath:
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
