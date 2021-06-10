'''
Class used to parse all data

@author jasonnmnd
'''
import numpy as np
import pandas as pd
import csv
from airplaneClass import Airplane

# Global Variables
seenAircraft = []
aircraftObjects = []


def readCSV(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            parseRow(row)

        csv_file.close()


def parseRow(row):
    if "hexid" in row and "alt" in row and "position" in row and "speed" in row:

        indexHex = row.index("hexid") + 1
        indexAlt = row.index("alt") + 1
        indexClock = row.index("clock") + 1
        indexPosition = row.index("position") + 1
        indexSpeed = row.index("speed") + 1

        if row[indexHex] not in seenAircraft:
            seenAircraft.append(row[indexHex])
            newAirplane = Airplane(row[indexHex])
            aircraftObjects.append(newAirplane)

            newAirplane.setAltitude(row[indexAlt].split(' ')[0])
            newAirplane.setClock(row[indexClock])
            newAirplane.setLatitude(latLongHelper(row[indexPosition]).split(' ')[0])
            newAirplane.setLongitude(latLongHelper(row[indexPosition]).split(' ')[1])
            newAirplane.setSpeed(row[indexSpeed].split(' ')[0])

        else:
            indexHex = row.index("hexid") + 1
            indexPlaneObject = 0

            for ap in aircraftObjects:
                if ap.getHexID() == row[indexHex]:
                    indexPlaneObject = aircraftObjects.index(ap)

            aircraftObjects[indexPlaneObject].setAltitude(row[indexAlt].split(' ')[0])
            aircraftObjects[indexPlaneObject].setClock(row[indexClock])
            aircraftObjects[indexPlaneObject].setLatitude(latLongHelper(row[indexPosition]).split(' ')[0])
            aircraftObjects[indexPlaneObject].setLongitude(latLongHelper(row[indexPosition]).split(' ')[1])
            aircraftObjects[indexPlaneObject].setSpeed(row[indexSpeed].split(' ')[0])


def latLongHelper(coordinates):
    start = coordinates.find("{") + 1
    end = coordinates.find("}")
    tmpString = coordinates[start:end]
    return tmpString


def getAirplanes():
    return aircraftObjects

# print(seenAircraft)
# print(aircraftObjects)
