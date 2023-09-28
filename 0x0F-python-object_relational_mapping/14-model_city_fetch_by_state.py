#!/usr/bin/python3
""" listing all the state from the hbtn_0e_6_usa """

# importing the needed library
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == '__main__':

    # connecting to mysql database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # print all the cities linked with states
    for state in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print(state[0] + ': (' + str(state[1]) + ') ' + state[2])

    session.close()
