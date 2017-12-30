"""This module contains the User graphql type definition."""

from graphene import ObjectType, String, ID, List
from server.models.User import UserModel

class User(ObjectType):
    """User graphql type definition."""
    id = ID()
    email = String()
    first_name = String()
    last_name = String()
    devotionals = List(lambda: Devotional)

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    @classmethod
    def get_user(cls, id):
        """Singleton method to get a User instance"""
        model = UserModel.query.filter_by(id=id).first()

        return cls.create_user_from_model(model)

    @classmethod
    def create_user_from_model(cls, model):
        """
        Class method to create a User instance given an SQLAlchemy model
        """
        return cls(
            id=model.id,
            email=model.email,
            first_name=model.first_name,
            last_name=model.last_name,
            model=model
        )

    def resolve_devotionals(self, info):
        """Devotionals resolver"""
        return [Devotional.create_devotional_from_model(d) for d in self.model.devotionals]

from server.graphql.Devotional import Devotional
