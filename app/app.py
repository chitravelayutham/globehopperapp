#Starting point of our WebApp - main 
#pip install Flask

from flask import Flask, request, jsonify
import country

#Using Flask framework
app = Flask(__name__)

#Create - POST API
@app.post('/countries')
def createcountryAPI():
    data = request.json
    return country.createcountryView(data)

#Read - GET API
@app.get('/countries')
def getallcountriesAPI():
    return country.getallcountriesView()

#Update - PUT API
@app.put('/countries/<int:country_id>')  #Query string parameter
def updatecountryAPI(country_id):
    data = request.json
    return country.updatecountryView(country_id, data)

#Delete - DELETE API
@app.delete('/countries/<int:country_id>')  #Query string parameter
def deletecountryAPI(country_id):
    return country.deletecountryView(country_id)



#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)