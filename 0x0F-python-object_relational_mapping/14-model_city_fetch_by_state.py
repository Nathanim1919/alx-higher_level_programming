#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

if __name__ == '__main__':

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    all_citie = session.query(State, City).join(City, State.id == City.state_id).all()

    for state, city in all_citie:
        print('{} ({}) {}'.format(state.name, city.id, city.name))

    session.close()
