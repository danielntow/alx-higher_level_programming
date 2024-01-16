#!/usr/bin/python3
"""script that prints the State object with the name
   passed as argument
   from the database hbtn_0e_6_usa (SQL injection free)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database>\
        <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Assign command line arguments to variables
    username, password, database, state_name = sys.argv[1:]

    try:
        # Create the engine and bind it to the Base class
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        with Session() as session:
            # Query and retrieve the State object with the given name
            state = session.query(State).filter_by(name=state_name).first()

            # Display results
            if state:
                print("{}".format(state.id))
            else:
                print("Not found")

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)
