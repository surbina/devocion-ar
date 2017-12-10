"""This module contains the class definition for Devotionals."""

from sqlalchemy import Column, Integer, Text, String, Date, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from server.models.Base import Base
from server.models.Comment import Comment

class Devotional(Base):
    """This class represent the db model for a Devotional."""
    __tablename__ = 'devotionals'
    id = Column(Integer, primary_key=True)
    title = Column(String(120))
    passage = Column(String(120))
    body = Column(Text(5000))
    creation_date = Column(DateTime)
    publish_date = Column(Date)
    publish_status = Column(Enum('DRAFT', 'PUBLISHED'))
    author_id = Column(Integer, ForeignKey('users.id'))

    comments = relationship(Comment, backref='comments_list')
