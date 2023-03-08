#Starting point of our WebApp - main 
#pip install Flask

from flask import Flask, request, jsonify
import country

#Using Flask framework
app = Flask(__name__)

#Create - POST api
@app.post('/countries')
def createcountryapi():
    data = request.json
    return country.createcountryview(data)

#Read - GET api
@app.get('/countries')
def getallcountriesapi():
    return country.getallcountriesview()

#Update - PUT api
@app.put('/countries/<int:country_id>')  #Query string parameter
def updatecountryapi(country_id):
    data = request.json
    return country.updatecountryview(country_id, data)

#Delete - DELETE api
@app.delete('/countries/<int:country_id>')  #Query string parameter
def deletecountryapi(country_id):
    return country.deletecountryview(country_id)



#Execute on the terminal
if __name__ == '__main__':
    app.run(debug=True)