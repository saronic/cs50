import csv
import os

from flask import Flask
from models1 import db, Flight, Passenger

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)


def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"add {origin} to {destination}")

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        main()
