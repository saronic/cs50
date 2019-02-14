import os

from flask import Flask, render_template, request
from models1 import db, Flight, Passenger

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db.init_app(app)


@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number")

    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight")

    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template("success.html")


@app.route("/flights")
def flights():
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight")

    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template("flight.html", passengers=passengers, flight=flight)
