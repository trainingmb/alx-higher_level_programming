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
    results = session.query(State)
    results = results.filter(State.name.contains('a'))
    results = results.order_by(State.id)
    for i in results:
        session.delete(i)
    session.commit()
