# Example Template

# import necessary libraries
import os

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from config import username, password, host, port, database

import psycopg2

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
# (https://help.heroku.com/ZKNTJQSK/
# why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL')
    .replace('postgres://', 'postgresql://', 1)
    )
# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Lumber_steel = Base.classes.lumber_steel

# Create our session (link) from Python to the DB
session = Session(engine)

#from .models import Pet

#################################################
# API Routes (start with '/api/')
#################################################
@app.route("/api/lumber_steel")
def commodities():
    # Query the database and send the jsonified results
    results = db.session.query(Lumber_steel.date, Lumber_steel.lumber_prc_change, Lumber_steel.steel_prc_change).all()

    date = [result[0] for result in results]
    lumber_prc_change = [result[1] for result in results]
    steel_prc_change = [result[2] for result in results]

    commodity_data = [{
        
        "Date": date,
        "Lumber Percent Change": lumber_prc_change,
        "Steel Perfcent Change": steel_prc_change,
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]
    return jsonify(results)
#################################################
# Fontend Routes
#################################################
# create route that renders index.html template
#@app.route("/")
#def home():
    #return render_template("index.html")


# Query the database and send the jsonified results
"""@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["petName"]
        lat = request.form["petLat"]
        lon = request.form["petLon"]

        pet = Pet(name=name, lat=lat, lon=lon)
        db.session.add(pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")"""


if __name__ == "__main__":
    app.run()