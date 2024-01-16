#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def list_cities(username, password, database):
    """List all City objects."""
    # Create an SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and retrieve all City objects with relationship to
    # the State object, ordered by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Display results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    # Assign command line arguments to variables
    username, password, database = sys.argv[1:4]

    # Call the function with the provided arguments
    list_cities(username, password, database)
