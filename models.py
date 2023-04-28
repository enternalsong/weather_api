from server import db
class BaseTable(db.Model):
    __tablename__ = 'rain_hour'
    index = db.Column(db.Integer, primary_key=True)
    locationName = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    stationId = db.Column(db.String)
    time = db.Column(db.String)
    elev = db.Column(db.Float)
    hour_12=db.Column(db.Float)
    hour_24=db.Column(db.Float)
    hour_3=db.Column(db.Float)
    hour_6=db.Column(db.Float)
    min_10=db.Column(db.Float)
    Now = db.Column(db.Float)
    rain = db.Column(db.Float)
    latest_2days=db.Column(db.Float)
    latest_3days =db.Column(db.Float)
    attribute = db.Column(db.String)
    city = db.Column(db.String)
    city_sn = db.Column(db.Integer)
    town= db.Column(db.String)
    town_sn = db.Column(db.Integer)

    def __init__(self,index,locationName,lat,lon,stationId,time,elev,hour_12,
                 hour_24,hour_3,hour_6,min_10,Now,rain,latest_2days,latest_3days,attribute,
                 city,city_sn,town,town_sn):
        self.index = index
        self.locationName = locationName
        self.lat = lat
        self.lon = lon
        self.stationId = stationId
        self.time = time
        self.elev = elev
        self.hour_12 = hour_12
        self.hour_24 = hour_24
        self.hour_3 = hour_3
        self.hour_6 = hour_6
        self.min_10 = min_10
        self.Now = Now
        self.rain = rain
        self.latest_2days = latest_2days
        self.latest_3days = latest_3days
        self.attribute = attribute
        self.city = city
        self.city_sn = city_sn
        self.town = town
        self.town_sn = town_sn
        
    def serialize(self):
        return {
            "index": self.index,
            "locationName": self.locationName,
            "lat": self.lat,
            "lon": self.lon,
            "time":self.time,
            "stationId": self.stationId,
            "ELEV": self.elev,
            "Hour_12": self.hour_12,
            "Hour_24": self.hour_24,
            "Hour_3": self.hour_3,
            "Hour_6": self.hour_6,
            "MIN_10": self.min_10,
            "Now": self.Now,
            "RAIN":self.rain,
            "latest_2days": self.latest_2days,
            "latest_3days": self.latest_3days,
            "ATTRIBUTE": self.attribute,
            "CITY": self.city,
            "CITY_SN": self.city_sn,
            "TOWN": self.town,
            "TOWN_SN": self.town_sn
        }

