#!/usr/bin/python3
"""
script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa
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
            # Create a new State object and add it to the session
            new_state = State(name="Louisiana")
            session.add(new_state)
            session.commit()

            # Print the new states.id after creation
            print(new_state.id)

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)
