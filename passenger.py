from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute("select * from flights").fetchall()
    for flight in flights:
        print(f"{flight.id}:{flight.origin} to {flight.destination},{flight.duration}")

    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("select * from flights where id=:id", {"id": flight_id}).fetchone()

    if flight is None:
        print("Error:no such flight")
        return

    passengers = db.execute("select * from passengers where flight_id=:flight_id", {"flight_id": flight.id}).fetchall()

    if len(passengers) == 0:
        print("Info: no passengers")

    for passenger in passengers:
        print(f"name: {passenger.name}")


if __name__ == "__main__":
    main()
