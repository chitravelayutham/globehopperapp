#Define all functions related to Country APIs

from flask import Flask, request, jsonify
import services

#Function to get all countries and return as a JSON object
#Create a country record
def createcountryView(data):
    services.createcountryService(data)
    return jsonify({'message' : 'Data inserted successfully'})

#Get all countries
def getallcountriesView():
    results = services.allcountriesService()

    data = []
    #Converted a list to dict
    for row in results:
        data.append({
            "CountryId" : row[0],
            "Name" : row[1],
            "Population" : row[2],
            "Continent" : row[3]
        })

    return jsonify(data)


#Update a country record
def updatecountryView(country_id, data):
    services.updateCountryService(country_id, data)
    return jsonify({'message' : 'Data updated successfully'})


#Delete a country record
def deletecountryView(country_id):
    services.deleteCountryService(country_id)
    return jsonify({'message' : 'Data deleted successfully'})