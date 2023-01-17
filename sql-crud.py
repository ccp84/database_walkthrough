from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a new instance of session maker class from the database link
Session = sessionmaker(db)
# open a session by calling the session subclass
session = Session()


# create database from declarative base subclass
base.metadata.create_all(db)