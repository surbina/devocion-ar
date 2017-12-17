"""Base clase for our db Models."""

from sqlalchemy import create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

BaseModel = declarative_base()
# We will need this for querying
BaseModel.query = db_session.query_property()
