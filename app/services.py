#Define all services for Country and City
from flask import Flask, request, jsonify
import conn

############################################# COUNTRY ########################################
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
def allcountriesservice():
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
def updatecountryservice(country_id, data):
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
def deletecountryservice(country_id):
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

############################################# CITY ########################################
#Create a city record
def createcityservice(data):
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    cityid = data['CityId']
    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    first = data['FirstLandmark']
    second = data['SecondLandmark']
    third = data['ThirdLandmark']

    #Execute the SQL
    mysql = "INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (cityid, name, countryid, capital, first, second, third)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    conn.myconn.close()
    


#Gets all records from city table using SQL
def allcitiesservice():
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mycursor.execute("SELECT * FROM city")
    results = mycursor.fetchall()

    #Close connection
    mycursor.close()
    conn.myconn.close()
    
    return results


#Update a city record
def updatecityservice(city_id, data):
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    first = data['FirstLandmark']
    second = data['SecondLandmark']
    third = data['ThirdLandmark']

    #Execute the SQL
    mysql = "UPDATE City SET Name = %s, CountryId= %s, Capital= %s, FirstLandmark= %s, SecondLandmark= %s, ThirdLandmark= %s WHERE cityId = %s"
    values = (name, countryid, capital, first, second, third, city_id)
    mycursor.execute(mysql, values)

    #Close connection
    mycursor.close()
    mycursor.close()
    conn.myconn.close()


#Delete a city record
def deletecityservice(city_id):
    #OPen connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #Execute the SQL
    mysql = "DELETE FROM City WHERE CityId = %s"
    values = [(city_id)]
    mycursor.execute(mysql, values)
    print(city_id)
    #Close connection
    mycursor.close()
    conn.myconn.close()