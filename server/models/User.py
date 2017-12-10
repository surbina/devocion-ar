"""This module contains the class definition for Users."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from server.models.Base import Base
from server.models.Devotional import Devotional
from server.models.Comment import Comment

class User(Base):
    """This class represent the db model for a User."""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))

    devotionals = relationship(Devotional, backref='devotionals')
    comments = relationship(Comment, backref='user_comments')
