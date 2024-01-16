from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base

class City(Base):
    """Define the City class to represent cities in the database.

    Attributes:
        id (int): Unique identifier for the city, auto-incremented.
        name (str): Name of the city, up to 128 characters.
        state_id (int): Foreign key linking to the 'states.id' column.

    Relationships:
        state (relationship): Many-to-One relationship with the State class.

    Table Information:
        __tablename__ (str): Name of the database table for cities.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)  # Define foreign key

    # Define the relationship with the State class
    state = relationship('State', back_populates='cities')
