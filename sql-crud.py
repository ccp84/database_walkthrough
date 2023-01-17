from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")
base = declarative_base()


# create class based Programmer table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# create a new instance of session maker class from the database link
Session = sessionmaker(db)
# open a session by calling the session subclass
session = Session()


# create database from declarative base subclass
base.metadata.create_all(db)
