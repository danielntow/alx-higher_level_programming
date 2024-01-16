#!/usr/bin/python3
"""Fetch cities by states."""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_states(username, password, database):
    # Create an SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and retrieve cities by states, ordered by city id
    cities = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()

    # Display results
    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    # Check if all arguments are provided
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <username> <password> <database>")
        exit(1)

    # Assign command line arguments to variables
    username, password, database = argv[1:4]

    # Call the function with the provided arguments
    fetch_cities_by_states(username, password, database)
