from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


# parent_id = Column(Integer, ForeignKey("parent.id"))
# children = relationship("Child", backref="parent")
# parents = relationship(
#         "Parent", secondary=association_table, back_populates="children"
#     )
