#Starting point of our WebApp - main 
#pip install Flask

from flask import Flask, request, jsonify
import country

#Using Flask framework
app = Flask(__name__)

#Create - POST API
@app.post('/countries')
def createcountry():
    data = request.json
    return country.createcountry(data)

#Read - GET API
@app.get('/countries')
def getallcountries():
    return country.getallcountries()

#Delete - DELETE API
@app.delete('/countries/<int:country_id>')  #Query string parameter
def deletecountry(country_id):
    return country.deletecountry(country_id)

#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)