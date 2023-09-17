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
for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}: {state.name}")
session.close()
