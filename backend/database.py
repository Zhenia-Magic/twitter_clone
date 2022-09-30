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

# parent_id = Column(Integer, ForeignKey("parent.id"))
# children = relationship("Child", backref="parent")
# parents = relationship(
#         "Parent", secondary=association_table, back_populates="children"
#     )
