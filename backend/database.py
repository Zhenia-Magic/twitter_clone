from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    hashed_password = Column(String)
    first_name = Column(String)
    is_admin = Column(Boolean)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    deleted = Column(Boolean)


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Integer)
    longitude = Column(Integer)
    deleted = Column(Boolean)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    created_at = Column(Integer)
    deleted = Column(Boolean)
    hashtags = Column(String)
    author = Column(String)
    country = Column(String)
    title = Column(String)


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    message = Column(String)
    sender = Column(String)
    reciever = Column(String)
    date = Column(Integer)


# parent_id = Column(Integer, ForeignKey("parent.id"))
# children = relationship("Child", backref="parent")
# parents = relationship(
#         "Parent", secondary=association_table, back_populates="children"
#     )
