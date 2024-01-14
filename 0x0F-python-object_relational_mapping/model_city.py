#!/usr/bin/python3
"""
This script define a City class
to work with on MySQLAlchemy ORM.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): The table instance name of the class
        id (int): The id of the class CITY
        name (str): The stringify method name of the class
        state_id (int): The state the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
