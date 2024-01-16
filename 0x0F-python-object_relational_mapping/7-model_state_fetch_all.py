#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Assign command line arguments to variables
    username, password, database = sys.argv[1:]

    try:
        # Create the engine and bind it to the Base class
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(engine)
        # Create a session to interact with the database
        session = Session()

        # Query and retrieve all State objects, sorted by id
        states = session.query(State).order_by(State.id).all()

        # Display results
        for state in states:
            print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the session
        if 'session' in locals() and session:
            session.close()
