from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import sqlite3 as lite
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, not_
from sqlalchemy import create_engine
from model import departure, DeptSchema, arrival, ArrSchema

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'flightinfodata.db'))
db = SQLAlchemy(app)
ma = Marshmallow(app)
Session = sessionmaker(bind = engine)
session = Session()

# endpoint to show all users
@app.route("/flights", methods=["GET"])
def get_user():
    flight_info_to_send = []
    for d,a in session.query(departure,arrival).filter(and_(arrival.flightNumber==departure.flightNumber, arrival.airlines == "Qantas",(or_(arrival.airport=="SYD",departure.airport=="SYD")))).all():
        flight = d.flightNumber +" "+d.airlines
        print("the flight number is: {}",format(flight))
        flight_info_model={
            'Flight' : flight,
            'destination' : a.airport,
            'departureTime' : d.scheduled
        }
        flight_info_to_send.append(flight_info_model)
    return jsonify(flight_info_to_send)
        

if __name__ == '__main__':
    app.run(debug=True)

