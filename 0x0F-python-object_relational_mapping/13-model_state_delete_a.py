#!/usr/bin/python3
"""
Script that deletes State objects with a name containing the letter 'a'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> \
            <database>".format(sys.argv[0]))
        sys.exit(1)

    # Assign command line arguments to variables
    username, password, database = sys.argv[1:]

    try:
        # Create the engine and bind it to the Base class
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        with Session() as session:
            # Query and retrieve State objects with names containing 'a'
            states_to_delete = session.query(State).filter(
                State.name.like('%a%')
                ).all()

            # Delete the retrieved State objects
            for state in states_to_delete:
                session.delete(state)

            session.commit()

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)
