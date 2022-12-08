from flask import Flask, jsonify
import pandas as pd
from sqlHelper import SQLHelper

app = Flask(__name__)
sqlHelper = SQLHelper()

@app.route("/")
def welcome():
    return(
        f"Welcome to the Hawaii Weather Station API"
    )

@app.route("/api/v1.0/precipitation")
def get_prcp():
    df = sqlHelper.getprcp()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def getStations():
    df = sqlHelper.getstation()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/tobs")
def getTobs():
    df = sqlHelper.gettobs()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>")
def getStart(start):
    df = sqlHelper.getstart(start)
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>/<end>")
def getEnd(start, end):
    df = sqlHelper.getend(start, end)
    data = df.to_dict(orient="records")
    return(jsonify(data))

if __name__ == "__main__":
    app.run(debug=True)