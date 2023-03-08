#Define all services for Country and City
from flask import Flask, request, jsonify
import conn

#Create a country record
def createcountry(data):
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL
    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s, %s, %s, %s)"
    values = (countryid, name, population, continent)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()
    


#Gets all records from Country table using SQL
def allcountriesService():
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


#Update a country record
def updateCountryService(country_id, data):
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    name = data['Name']
    population = data['Population']
    continent = data['Continent']

    #Execute the SQL
    mysql = "UPDATE Country SET Name = %s, Population=%s, Continent=%s WHERE CountryId = %s"
    values = (name, population, continent, country_id)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    mycursor.close()
    conn.myconn.close()


#Delete a country record
def deleteCountryService(country_id):
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    print(country_id)
    #Execute the SQL
    mysql = "DELETE FROM Country WHERE CountryId = %s"
    values = [(country_id)]
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()