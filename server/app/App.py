"""Main App module."""

from flask import Flask
from flask_cors import CORS
from server.api.Api import init_api
from server.graphql.schema import init_graphql
from server.models.Base import engine, db_session, BaseModel

APP = Flask(__name__)

# Allow CORS for local development
CORS_CONFIG = CORS(APP, resources={r"/api/*": {"origins": ["http://localhost:3000"]}})

# Init database
@APP.before_first_request
def create_databse():
    """Create databa if not already created"""
    BaseModel.metadata.create_all(bind=engine)

# Close db session
@APP.teardown_appcontext
def shutdown_session(exception=None):
    """Closes db session when app is terminated"""
    db_session.remove()

# Init API
init_api(APP)

# Init GraphQL
init_graphql(APP)

@APP.route("/")
def hello():
    """Response to hello world"""
    return "Hello World!"
