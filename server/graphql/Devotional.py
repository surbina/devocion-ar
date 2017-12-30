"""This module contains the Devotional graphql type definition."""

from graphene import ObjectType, String, ID, Enum, Field
from graphene.types.datetime import DateTime, Date
from server.models.Devotional import DevotionalModel

class PublishStatus(Enum):
    """PublishStatus graphql enum definition"""
    DRAFT = 1
    PUBLISHED = 2


class Devotional(ObjectType):
    """Devotional graphql type definition."""
    id = ID()
    title = String()
    passage = String()
    body = String()
    creation_date = DateTime()
    publish_date = Date()
    author = Field(lambda: User)

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    @classmethod
    def get_devotional(cls, id):
        """Class method to get a Devotional instance given an id"""
        model = DevotionalModel.query.filter_by(id=id).first()

        return cls.create_devotional_from_model(model)

    @classmethod
    def create_devotional_from_model(cls, model):
        """
        Class method to create a Devotional instance given an SQLAlchemy model
        """
        return cls(
            id=model.id,
            title=model.title,
            passage=model.passage,
            body=model.body,
            creation_date=model.creation_date,
            publish_date=model.publish_date,
            model=model
        )

    def resolve_author(self, info):
        """Author resolver"""
        return User.create_user_from_model(self.model.author)

from server.graphql.User import User
