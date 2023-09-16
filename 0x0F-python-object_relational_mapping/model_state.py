#!/usr/bin/env python3
""" this is a class that inherit from Base that will be link to mysql
database using the ORM format """

# importing need library
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
Base = declarative_base()

# connecting to mysql database
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", \
        "root", "hbtn_0e_6_usa"), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# writing my database class
class State(Base):
    """ This class will create my database
    with my linked mysql database """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(128))
    
    def __init__(self, id, name):
        """ initalizing the class atribute """
        self.id = id
        self.name = name
session.commit()
session.close()
