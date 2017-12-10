"""This module contains the class definition for Comments."""

from sqlalchemy import Column, Integer, Text, ForeignKey
from server.models.Base import Base

class Comment(Base):
    """This class represent the db model for a Comment."""
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    body = Column(Text(500))
    author_id = Column(Integer, ForeignKey('users.id'))
    devotional_id = Column(Integer, ForeignKey('devotionals.id'))
