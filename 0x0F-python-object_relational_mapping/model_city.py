#!/usr/bin/python3
"""model city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """City class inherits from Base and links to the MySQL table cities.

    Attributes:
        id (int): Unique identifier for the city, auto-incremented.
        name (str): Name of the city, up to 128 characters.
        state_id (int): Foreign key linking to the 'states.id' column.

    Relationships:
        state (relationship): Many-to-One relationship with the State class.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    # Define foreign key
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

