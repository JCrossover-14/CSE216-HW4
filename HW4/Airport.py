import math


class Airport:
    def __init__(self,code,latitudeDegrees,latitudeMinutes,longitudeDegrees,longitudeMinutes):
        self.code=code
        self.latitudeDegrees = latitudeDegrees
        self.latitudeMinutes = latitudeMinutes
        self.longitudeDegrees = longitudeDegrees
        self.longitudeMinutes = longitudeMinutes

    def getCode(self):
        return self.code
    
    def getLatitudeDegrees(self):
        return self.latitudeDegrees
    
    def getLatitudeMinutes(self):
        return self.latitudeMinutes
    
    def getLongitudeMinutes(self):
        return self.longitudeMinutes
    
    def getLongitudeDegrees(self):
        return self.longitudeDegrees
    
    def calculateDistance (self,a1,a2):
        PI_F=3.14159265358979
        RADIAN_FACTOR= 180.0/PI_F
        EARTH_RADIUS=3963.0

        lat1 = a1.getLatitudeDegrees()+(a1.getLatitudeMinutes()/60.0)
        lat1 = lat1/RADIAN_FACTOR
        long1 = -(a1.getLongitudeDegrees()+a1.getLongitudeMinutes()/60.0)
        long1 = long1/RADIAN_FACTOR
        lat2 = a2.getLatitudeDegrees()+a2.getLatitudeMinutes()/60.0
        lat2 = lat2/RADIAN_FACTOR 
        long2 = -(a2.getLongitudeDegrees()+a2.getLongitudeMinutes()/60.0)
        long2 = long2/RADIAN_FACTOR

        x = (math.sin(lat1)*math.sin(lat2))+(math.cos(lat1)*math.cos(lat2)*math.cos(long2-long1))
        x2= math.sqrt(1.0-(x*x)/x)
        
        return EARTH_RADIUS*math.atan(x2)