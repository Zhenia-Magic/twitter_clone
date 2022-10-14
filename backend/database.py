from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    about_me = Column(String)
    is_admin = Column(Boolean)

    posts = relationship("Post", backref="users")


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    deleted = Column(Boolean)

    posts = relationship(
        "Post", secondary="tags_posts", back_populates="tags"
    )


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    latitude = Column(Integer)
    longitude = Column(Integer)
    deleted = Column(Boolean)

    posts = relationship("Post", backref="countries")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    created_at = Column(Integer)
    deleted = Column(Boolean)
    author_id = Column(Integer, ForeignKey("users.id"))
    country_id = Column(Integer, ForeignKey("countries.id"))
    title = Column(String)

    tags = relationship(
             "Tag", secondary="tags_posts", back_populates="posts"
         )


class TagsPosts(Base):
    __tablename__ = 'tags_posts'

    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)
    post_id = Column(String, ForeignKey("posts.id"), primary_key=True)


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    message = Column(String)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Integer)

    sender = relationship("User", foreign_keys=[sender_id], backref="sent_messages")
    receiver = relationship("User", foreign_keys=[receiver_id], backref="received_messages")


# parent_id = Column(Integer, ForeignKey("parent.id"))
# children = relationship("Child", backref="parent")
# parents = relationship(
#         "Parent", secondary=association_table, back_populates="children"
#     )
