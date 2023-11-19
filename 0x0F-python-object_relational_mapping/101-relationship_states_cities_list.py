#!/usr/bin/python3
"""
List all states using SQLAlchemy
"""
import sys
from relationship_state import Base, State, City

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
    res = session.query(State). \
        join(City). \
        order_by(State.id). \
        order_by(City.id). \
        all()
    for i in res:
        print("{}: {}".format(i.id, i.name))
        for j in i.cities:
            print("\t{}: {}".format(j.id, j.name))
