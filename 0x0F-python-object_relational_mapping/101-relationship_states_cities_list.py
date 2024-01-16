#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_states_cities(username, password, database):
    """List all State objects and corresponding City objects."""
    # Create an SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and retrieve all State and City objects with relationship,
    # ordered by states.id and cities.id
    results = session.query(State).order_by(State.id).all()

    # Display results
    for state in results:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

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
    list_states_cities(username, password, database)
