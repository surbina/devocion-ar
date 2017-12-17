"""This module contains the User graphql type definition."""

from graphene import ObjectType, String, ID
from server.models.User import UserModel

class User(ObjectType):
    """User graphql type definition."""
    id = ID()
    email = String()
    first_name = String()
    last_name = String()

    @classmethod
    def get_model(cls, id):
        """Singleton method to get a User instance"""
        model = UserModel.query.filter_by(id=id).first()

        return cls(
            id=model.id,
            email=model.email,
            first_name=model.first_name,
            last_name=model.last_name
        )
