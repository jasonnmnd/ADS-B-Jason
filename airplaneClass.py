'''
Airplane class used to represent airplane object

@author jasonnmnd
'''

class Airplane:
    def __init__(self, hexID):
        self.hexID = hexID
        self.altitude = []
        self.clock = []
        self.speed = []
        self.latitude = []
        self.longitude = []

    def setHexID(self, x):
        self.hexID = x

    def getHexID(self):
        return self.hexID

    def setAltitude(self, x):
        self.altitude.append(x)

    def getAltitude(self):
        return self.altitude

    def setClock(self, x):
        self.clock.append(x)

    def getClock(self):
        return self.clock

    def getPosition(self):
        return self.position

    def setSpeed(self, x):
        self.speed.append(x)

    def getSpeed(self):
        return self.speed

    def setLatitude(self, x):
        self.latitude.append(x)

    def getLatitude(self):
        return self.latitude

    def setLongitude(self, x):
        self.longitude.append(x)

    def getLongitude(self):
        return self.longitude

