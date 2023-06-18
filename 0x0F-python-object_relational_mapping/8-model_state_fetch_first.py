#!/usr/bin/python3
"""a script that prints the first State object from the database hbtn_0e_6_usa"""


if __name__ == "__main__":


    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm  import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base .metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
