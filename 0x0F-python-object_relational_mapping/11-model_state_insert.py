#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    new_state = State(name = 'Louisiana')
    session.add(new_state)
    session.commit()

    print('{}'.format(new_state.id))

    session.clse()
