#!/usr/bin/python3
"""
Models using SQLAlchemmy
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Model for states table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
            passive_deletes=True)

class City(Base):
    """
    Model for city class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True,
            nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
