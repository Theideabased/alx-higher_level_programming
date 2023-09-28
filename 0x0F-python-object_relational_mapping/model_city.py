#!/usr/bin/python3
""" this is a class that inherit from Base that will be link to mysql
database using the ORM format """

# importing need library
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


# writing my database class
class City(Base):
    """ This class will create my database
    with my linked mysql database """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column('name', String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
