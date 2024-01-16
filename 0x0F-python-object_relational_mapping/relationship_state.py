from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Define the State class to represent states in the database.

    Attributes:
        id (int): Unique identifier for the state, auto-incremented.
        name (str): Name of the state, up to 128 characters.

    Relationships:
        cities (relationship): One-to-Many relationship with the City class. Deletes linked City objects when the State is deleted.

    Table Information:
        __tablename__ (str): Name of the database table for states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Define the relationship with the City class
    cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
