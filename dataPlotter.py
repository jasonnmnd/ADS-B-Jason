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


def plotSingularPlane(latitudeList, longitudeList):
    # Math to calculate distance in miles from latitude and longitude

    differenceLatitudeList = []
    differenceLongitudeList = []
    degreesList = []
    radiusList = []

    for lat in latitudeList:
        newLat = differenceLatitudeCalculator(lat)
        differenceLatitudeList.append(newLat)

    for long in longitudeList:
        newLong = differenceLongitudeCalculator(long)
        differenceLongitudeList.append(newLong)

    degreesList, radiusList = rectangularToPolarConverter(differenceLatitudeList, differenceLongitudeList)

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # Compute areas and colors
    N = 150
    r = radiusList
    theta = degreesList
    area = 500
    colors = theta

    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')
    c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.show()


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
        deg = math.degrees(math.atan(float(lat) / float(longitudeList[indexLong])))
        indexLong = indexLong + 1
        degreesList.append(deg)

    return radiusList, degreesList
