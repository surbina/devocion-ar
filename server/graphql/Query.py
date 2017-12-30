"""This module presents the Query class for our graphql endpoint"""

from graphene import ObjectType, Field, String
from server.graphql.User import User
from server.graphql.Devotional import Devotional

class Query(ObjectType):
    """Graphql Query type"""
    user = Field(User, id=String())
    devotional = Field(Devotional, id=String())

    def resolve_user(self, info, id):
        """Given an id, return the proper User"""
        return User.get_user(id)

    def resolve_devotional(self, info, id):
        """Given an id, return the proper Devotional"""
        return Devotional.get_devotional(id)
