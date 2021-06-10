'''
Class used to plot data

Resources used from matplotlib.org

@author jasonnmnd
'''
import math

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math as m

REF_LATITUDE = 39.79
REF_LONGITUDE = -84.09
REF_EARTH_CIRCUM = 24981.91


def plotSingularPlane(hexID, latitudeList, longitudeList):
    # Math to calculate distance in miles from latitude and longitude

    differenceLatitudeList, differenceLongitudeList = normalizeAirplaneDistance(latitudeList, longitudeList)
    radiusList, degreesList = rectangularToPolarConverter(differenceLatitudeList, differenceLongitudeList)

    # Plotting
    r = radiusList
    theta = np.deg2rad(degreesList)

    # Compute areas and colors
    ax = plt.subplot(projection='polar')
    # ax.plot(r, theta)
    plt.scatter(theta, r)
    ax.set_rlabel_position(0)
    ax.grid(True)
    plt.title("Plot of Singular Aircraft Path HEXID: " + str(hexID))
    plt.show()


def plotMultipleAirplane(airplaneList):
    ax = plt.subplot(projection='polar')

    for plane in airplaneList:
        differenceLatitudeList, differenceLongitudeList = normalizeAirplaneDistance(plane.getLatitude(),
                                                                                    plane.getLongitude())
        radiusList, degreesList = rectangularToPolarConverter(differenceLatitudeList, differenceLongitudeList)

        r = radiusList
        theta = np.deg2rad(degreesList)
        plt.scatter(theta, r, c='b', marker='s', label=str(plane.getHexID()))

    plt.legend(loc='best')
    plt.show()


def normalizeAirplaneDistance(latitudeList, longitudeList):
    differenceLatitudeList = []
    differenceLongitudeList = []

    for lat in latitudeList:
        newLat = differenceLatitudeCalculator(lat)
        differenceLatitudeList.append(newLat)

    for long in longitudeList:
        newLong = differenceLongitudeCalculator(long)
        differenceLongitudeList.append(newLong)

    return differenceLatitudeList, differenceLongitudeList


def differenceLatitudeCalculator(singleLatitude):
    # Calculates degree difference
    distanceLatitude = float(singleLatitude) - REF_LATITUDE
    return distanceLatitude * (REF_EARTH_CIRCUM / 360)


def differenceLongitudeCalculator(singleLongitude):
    distanceLongitude = float(singleLongitude) - REF_LONGITUDE
    return distanceLongitude * (REF_EARTH_CIRCUM / 360)


def rectangularToPolarConverter(latitudeList, longitudeList):
    degreesList = []
    radiusList = []

    # Calculate the radius w/ distance formula
    indexLong = 0
    for lat in latitudeList:
        r = m.sqrt(float(lat) ** 2 + float(longitudeList[indexLong]) ** 2)
        indexLong = indexLong + 1
        radiusList.append(r)

    indexLong = 0
    for lat in latitudeList:
        deg = np.rad2deg(np.arctan2(float(lat), float(longitudeList[indexLong])))
        indexLong = indexLong + 1
        degreesList.append(deg)

    return radiusList, degreesList
