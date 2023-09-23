#!/usr/bin/python3
""" this is a class that inherit from Base that will be link to mysql
database using the ORM format """

# importing need library
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


# writing my database class
class State(Base):
    """ This class will create my database
    with my linked mysql database """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column('name', String(128), nullable=False)
