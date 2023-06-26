#!/usr/bin/python3
"""
Databse handling through sqlalchemy
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def createsessionmaker(eng):
    """
    Creates a session maker and returns it
    """
    return sessionmaker(bind=engine)


if __name__ == "__main__":
    host = 'mysql+mysqldb://{}:{}@localhost/{}'
    host = host.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(host, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = createsessionmaker(engine)
    session = Session()
    st = session.query(State.id, State.name).filter(State.name == sys.argv[4]).first()
    if st is None:
        print("Not Found")
    else:
        print("{}".format(st.id))
