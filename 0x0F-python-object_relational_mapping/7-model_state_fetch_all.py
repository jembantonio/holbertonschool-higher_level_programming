#!/usr/bin/python3
''' a script that lists all State objects from the database hbtn_0e_6_usa
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine(
            '''mysql+mysqldb://{}:{}@localhost/{}'''.
            format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for st_id, name in session.query(State.id, State.name).order_by(State.id):
        print("{}: {}".format(st_id, name))
