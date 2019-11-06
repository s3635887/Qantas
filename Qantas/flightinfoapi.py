from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import sqlite3 as lite
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, not_
from sqlalchemy import create_engine

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'flightinfodata.db'))
db = SQLAlchemy(app)
ma = Marshmallow(app)
Session = sessionmaker(bind = engine)
session = Session()

class departure(db.Model):
    flightNumber = db.Column(db.String(80), primary_key=True)
    scheduled = db.Column(db.String(100), nullable = False)
    airport = db.Column(db.String(150), nullable = False)
    airlines = db.Column(db.String(80), nullable=False)


    def __init__(self, flightNumber,airlines, scheduled, airport):
        self.flightNumber = flightNumber
        self.scheduled = scheduled
        self.airport = airport
        self.airlines = airlines

class DeptSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('flightNumber', 'scheduled', 'airport','airline')

class arrival(db.Model):
    flightNumber = db.Column(db.String(80), primary_key=True)
    scheduled = db.Column(db.String(100), nullable = False)
    airport = db.Column(db.String(150), nullable = False)
    airlines = db.Column(db.String(80), nullable=False)


    def __init__(self, flightNumber,airlines, scheduled, airport):
        self.flightNumber = flightNumber
        self.scheduled = scheduled
        self.airport = airport
        self.airlines = airlines

class ArrSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('flightNumber', 'scheduled', 'airport', 'airline')
        
dept_schema = DeptSchema()
depts_schema = DeptSchema(many=True)
arr_schema = ArrSchema()
arrs_schema = ArrSchema(many=True)

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

