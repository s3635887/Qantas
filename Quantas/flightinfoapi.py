from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import sqlite3 as lite


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flightinfodata.db')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class departure(db.Model):
    flightNumber = db.Column(db.String(80), primary_key=True)
    airline = db.Column(db.String(80), nullable=False)
    scheduled = db.Column(db.DateTime, nullable = False)
    airport = db.Column(db.String(150), nullable = False)

    def __init__(self, flightNumber, airline, scheduled, airport):
        self.flightNumber = flightNumber
        self.airline = airline
        self.scheduled = scheduled
        self.airport = airport

class DeptSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('flightNumber', 'airline', 'scheduled', 'airport')

class arrival(db.Model):
    flightNumber = db.Column(db.String(80), primary_key=True)
    airline = db.Column(db.String(80), nullable=False)
    scheduled = db.Column(db.DateTime, nullable = False)
    airport = db.Column(db.String(150), nullable = False)

    def __init__(self, flightNumber, airline, scheduled, airport):
        self.flightNumber = flightNumber
        self.airline = airline
        self.scheduled = scheduled
        self.airport = airport

class ArrSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('flightNumber', 'airline', 'scheduled', 'airport')


dept_schema = DeptSchema()
depts_schema = DeptSchema(many=True)
arr_schema = ArrSchema()
arrs_schema = ArrSchema(many=True)

# endpoint to show all users
@app.route("/flights", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(debug=True)

