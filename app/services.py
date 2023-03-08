#Define all services for Country and City
from flask import Flask, request, jsonify
import conn

#Create a country record
def createcountry(data):
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryId = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL
    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
    values = (countryId, name, population, continent)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()
    


#Gets all records from Country table using SQL
def allcountries():
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("SELECT * FROM Country")
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()
    
    return results



