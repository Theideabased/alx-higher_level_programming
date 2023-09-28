#!/usr/bin/python3
""" listing all the state from the hbtn_0e_6_usa """

# importing the needed library
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    # connecting to mysql database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # add the new state
    new_state = State(name = "Louisiana")
    session.add(new_state)

    # writing my query with python object oriented programming
    instance = session.query(State).filter(State.name == "Louisiana")
    print(instance[0].id)
    session.commit()
