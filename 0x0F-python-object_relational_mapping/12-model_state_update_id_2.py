#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
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
            # Query and retrieve the State object with id=2
            state_to_update = session.query(State).filter_by(id=2).first()

            # If the state with id=2 exists, update its name to "New Mexico"
            if state_to_update:
                state_to_update.name = "New Mexico"
                session.commit()

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)
