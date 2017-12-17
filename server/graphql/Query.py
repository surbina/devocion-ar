"""This module presents the Query class for our graphql endpoint"""

from graphene import ObjectType, Field, String
from server.graphql.User import User

class Query(ObjectType):
    """Graphql Query type"""
    user = Field(User, id=String())

    def resolve_user(self, info, id):
        """Given an id, return the proper User"""
        return User.get_model(id)
