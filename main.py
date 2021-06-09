'''

Main class used to interface with all modules

@author jasonnmnd

'''

from dataParser import *

FILE_TO_READ = "data_Fri 04 Jun 2021 12:00:00 am.csv"

def main():
    readCSV(FILE_TO_READ)
    print(getAirplanes()[0].getHexID())
    print(getAirplanes()[0].getAltitude())
    print(getAirplanes()[0].getClock())
    print(getAirplanes()[0].getLatitude())
    print(getAirplanes()[0].getLongitude())
    print(getAirplanes()[0].getSpeed())
    print("Data Analysis Finished")


#Tester used to run main with custom commands
if __name__ == "__main__":
    main()