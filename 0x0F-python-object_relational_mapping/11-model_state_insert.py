#!/usr/bin/python3
"""
List all states using SQLAlchemy
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def engine_session_creator(gurl):
    """
    Create the Engine and Session to be used
    """
    engine = create_engine(gurl,
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    return engine, session



if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                sys.argv[2], sys.argv[3])
    engine, Session = engine_session_creator(url)
    session  = Session()
    new_state = State()
    new_state.name = "Louisiana"
    session.add(new_state)
    session.commit()

