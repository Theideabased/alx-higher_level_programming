#!/usr/bin/env python3
""" listing all the state from the hbtn_0e_6_usa """

# importing the needed library
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connecting to mysql database
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root",
    "hbtn_0e_6_usa"), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# writing my query with python object oriented programming
result = session.query(State).first()
print(result)
session.close()
