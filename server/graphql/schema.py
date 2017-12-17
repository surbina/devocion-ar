"""This module is in charge of initializing the graphql endpoint"""

from graphene import Schema
from flask_graphql import GraphQLView
from server.graphql.Query import Query

def init_graphql(app):
    """Initialize graphql endpoint"""
    schema = Schema(query=Query)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        )
    )
