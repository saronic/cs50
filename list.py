from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



def main():
    flights = db.execute("select * from flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}")


if __name__ == "__main__":
    main()
