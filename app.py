from flask import Flask, render_template
import requests
import json

from AnalyseCountry import AnalyseCountry
from AnalyseState import AnalyseState
from SearchCountry import SearchCountry
from SearchState import SearchState
from StateDatabase import StateDatabase

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/updatestate")
def updatestate():
    instance = StateDatabase()
    return instance.update()

@app.route("/analysestate/<state>")
def analysestate(state):
    instance = AnalyseState()
    return instance.analyse_state(state)


@app.route("/analysecountry/<country>")
def analysecountry(country):
    instance = AnalyseCountry()
    return instance.analyse_country(country)

@app.route("/searchcountry/<country>/<date>")
def countrysearch(country, date):
    instance = SearchCountry()
    return instance.search(date, country)


@app.route("/searchstate/<state>/<date>")
def searchstate(state, date):
    instance = SearchState()
    return instance.search(date, state)

@app.route("/state/<state>")
def statedata(state):
    state = state.upper()
    response = requests.get("https://localcoviddata.com/covid19/v1/high-level-policy?country=USA&state=" + state)
    objectresponse = json.loads(response.text)

    res = {"source": objectresponse["Source"],
           "gather": objectresponse["Community_regulations"]["Gathering_Restriction_Code"],
           "nonessentialbus": objectresponse["Community_regulations"]["Non_Essential_Business_Closure_Code"],
           "resturant": objectresponse["Community_regulations"]["Restaurant_Restrictions_Code"]}

    return json.dumps(res)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header["Access-Control-Allow-Headers"] = '*'
    return response


if __name__ == '__main__':
    app.run()
