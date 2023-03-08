#Starting point of our WebApp - main 
#pip install Flask

from flask import Flask, request, jsonify
import country
from flask_wtf.csrf import CSRFProtect

#Using Flask framework
app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

#Create - POST API
@app.post('/countries')
def createCountry():
    data = request.json
    return country.createCountry(data)

#Read - GET API
@app.get('/countries')
def getAllCountries():
    return country.getCountries()



#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)