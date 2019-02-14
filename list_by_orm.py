import csv
import os

from flask import Flask
from models1 import db, Flight, Passenger

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)


def main():
    flights = Flight.query.all()
    print(flights)
    for flight in flights:
        print(f"type(flight):{type(flight)}")
        # print(f"{flight.origin} --> {flight.destination} with {flight.duration}")
        print(flight)


if __name__ == "__main__":
    with app.app_context():
        main()
