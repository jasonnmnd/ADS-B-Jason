'''
Class used to parse all data

@author jasonnmnd
'''
import numpy as np
import pandas as pd
import csv
from AirplaneClass import Airplane

# Global Variables
seenAircraft = []
aircraftObjects = []

FILE_TO_READ = "data_Fri 04 Jun 2021 12:00:00 am.csv"


def readCSV(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
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
        # indexLatitude = row.index("latitude") + 1
        # indexLongitude = row.index("longitude") + 1

        if row[indexHex] not in seenAircraft:
            seenAircraft.append(row[indexHex])
            newAirplane = Airplane(row[indexHex])
            aircraftObjects.append(newAirplane)

            newAirplane.setAltitude(row[indexAlt])
            newAirplane.setClock(row[indexClock])
            newAirplane.setPosition(row[indexPosition])
            newAirplane.setSpeed(row[indexSpeed])

        else:
            indexHex = row.index("hexid") + 1
            indexPlaneObject = 0

            for ap in aircraftObjects:
                if ap.getHexID() == row[indexHex]:
                    indexPlaneObject = aircraftObjects.index(ap)

            aircraftObjects[indexPlaneObject].setAltitude(row[indexAlt])
            aircraftObjects[indexPlaneObject].setClock(row[indexClock])
            aircraftObjects[indexPlaneObject].setPosition(row[indexPosition])
            aircraftObjects[indexPlaneObject].setSpeed(row[indexSpeed])

readCSV(FILE_TO_READ)
#print(seenAircraft)
#print(aircraftObjects)