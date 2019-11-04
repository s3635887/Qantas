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
    airline = db.Column(db.String(80), nullable=False)


    def __init__(self, flightNumber,airline, scheduled, airport):
        self.flightNumber = flightNumber
        self.scheduled = scheduled
        self.airport = airport
        self.airline = airline

class DeptSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('flightNumber', 'scheduled', 'airport','airline')

class arrival(db.Model):
    flightNumber = db.Column(db.String(80), primary_key=True)
    scheduled = db.Column(db.String(100), nullable = False)
    airport = db.Column(db.String(150), nullable = False)
    airline = db.Column(db.String(80), nullable=False)


    def __init__(self, flightNumber, scheduled, airport):
        self.flightNumber = flightNumber
        self.scheduled = scheduled
        self.airport = airport
        self.airline = airline

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
    print("Hello, this in the api")
    # flight_details = session.query(departure,arrival).filter(and_(arrival.flightNumber=departure.flightNumber,arrival.airline=="Qantas",(or_(arrival.airport=="SYD",departure.airport=="SYD")))).all()
    for d,a in session.query(departure,arrival).filter(and_(arrival.flightNumber=departure.flightNumber,arrival.airline=="Qantas",(or_(arrival.airport=="SYD",departure.airport=="SYD")))).all():
        print("this is the airline:{}".format(d.airline))
    
    # result = arrs_schema.dump(flight_details)
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True)

