from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

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