from server import db
class BaseTable(db.Model):
    __tablename__ = 'rain_hour'
    index = db.Column(db.Integer, primary_key=True)
    locationame = db.Column(db.String)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    stationid = db.Column(db.String)
    time = db.Column(db.String)
    elev = db.Column(db.Float)
    hour_12=db.Column(db.Float)
    hour_24=db.Column(db.Float)
    hour_3=db.Column(db.Float)
    hour_6=db.Column(db.Float)
    min_10=db.Column(db.Float)
    now = db.Column(db.Float)
    rain = db.Column(db.Float)
    latest_2days=db.Column(db.Float)
    latest_3days =db.Column(db.Float)
    attribute = db.Column(db.String)
    city = db.Column(db.String)
    city_sn = db.Column(db.Integer)
    town= db.Column(db.String)
    town_sn = db.Column(db.Integer)

    def __init__(self,index,locationame,lat,lon,stationid,time,elev,hour_12,
                 hour_24,hour_3,hour_6,min_10,now,rain,latest_2days,latest_3days,attribute,
                 city,city_sn,town,town_sn):
        self.index = index
        self.locationame = locationame
        self.lat = lat
        self.lon = lon
        self.stationid = stationid
        self.time = time
        self.elev = elev
        self.hour_12 = hour_12
        self.hour_24 = hour_24
        self.hour_3 = hour_3
        self.hour_6 = hour_6
        self.min_10 = min_10
        self.now = now
        self.rain = rain
        self.latest_2days = latest_2days
        self.latest_3days = latest_3days
        self.attribute = attribute
        self.city = city
        self.city_sn = city_sn
        self.town = town
        self.town_sn = town_sn
        
    def serialize(self):
        if self.rain==-998:
            self.rain=0
        if self.hour_3==-998:
            self.hour_3=0
        if self.hour_6==-998:
            self.hour_6=0
        if self.min_10==-998:
            self.min_10=0
        return {
            "index": self.index,
            "locationName": self.locationame,
            "lat": self.lat,
            "lon": self.lon,
            "time":self.time,
            "stationId": self.stationid,
            "elev": self.elev,
            "hour_12": self.hour_12,
            "hour_24": self.hour_24,
            "hour_3": self.hour_3,
            "hour_6": self.hour_6,
            "min_10": self.min_10,
            "now": self.now,
            "rain":self.rain,
            "latest_2days": self.latest_2days,
            "latest_3days": self.latest_3days,
            "attribute": self.attribute,
            "city": self.city,
            "city_sn": self.city_sn,
            "town": self.town,
            "town_sn": self.town_sn
        }

