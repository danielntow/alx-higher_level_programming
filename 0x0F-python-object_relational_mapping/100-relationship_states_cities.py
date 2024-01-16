#!/usr/bin/python3
"""Create the State "California" with the City "San Francisco"."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <username> <password> <database>")
        exit(1)

    # Assign command line arguments to variables
    username, password, database = argv[1:4]

    # Create an SQLAlchemy engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    session = Session(engine)

    # Create the State "California" with the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco")

    # Link the City to the State
    california.cities.append(san_francisco)

    # Add the State to the session and commit changes
    session.add(california)
    session.commit()

    # Close the session
    session.close()
