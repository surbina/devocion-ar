"""This module contains the Comment graphql type definition."""

from graphene import ObjectType, String, ID, Enum, Field
from server.models.Comment import CommentModel

class Comment(ObjectType):
    """Comment graphql type definition."""
    id = ID()
    body = String()
    author = Field(lambda: User)
    devotional = Field(lambda: Devotional)

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    @classmethod
    def get_comment(cls, id):
        """Class method to get a Comment instance given an id"""
        model = CommentModel.query.filter_by(id=id).first()

        return cls.create_comment_from_model(model)

    @classmethod
    def create_comment_from_model(cls, model):
        """
        Class method to create a Comment instance given an SQLAlchemy model
        """
        print('id: {}'.format(model.id))
        print('body: {}'.format(model.body))

        return cls(
            id=model.id,
            body=model.body,
            model=model
        )

    def resolve_author(self, info):
        """Author resolver"""
        return User.create_user_from_model(self.model.author)

    def resolve_devotional(self, info):
        """Devotional resolver"""
        return Devotional.create_devotional_from_model(self.model.devotional)


from server.graphql.User import User
from server.graphql.Devotional import Devotional
