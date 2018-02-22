from pymongo import MongoClient
import datetime
import json
import os
def main():
        client = MongoClient('mongodb://localhost:27017') 
        db = client.karoth4
        collection = db['cities']
        with open("worldcities.csv","rb") as mFile:
                next(mFile)
                for mLine in mFile:
                        [city,city_ascii,lat,lng,pop,country,iso2,iso3,province] = mLine.split(",")
                        latt = float(lat)
                        lngg = float(lng)
                        geoString = {'city': city, 'loc': {'type' : 'Point', 'coordinates' : [lngg, latt]}}
                        print geoString
                        db.cities.insert(geoString)
if __name__ == '__main__':
        main()




