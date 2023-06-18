#!/usr/bin/python3
"""prints the State object with the name passed as argument from
the database hbtn_0e_6_usa"""

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print('{}'.format(state.id))
    else:
        print('Not found')

    session.close()
