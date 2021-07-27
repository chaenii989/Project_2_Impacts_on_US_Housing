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
database_url = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Lumber_steel = Base.classes.lumber_steel
Average_home_price = Base.classes.average_home_price
#Homeownership_rates= Base.classes.homeownership_rate
Home_units = Base.classes.home_units
Monthly_house_supply= Base.classes.monthly_house_supply
#House_permits = Base.classes.house_permits
New_2020= Base.classes.new_2020
New_2021= Base.classes.new_2021


# Create our session (link) from Python to the DB
session = Session(engine)

"""stmt = sqlalchemy.select("*").select_from(Lumber_steel)
result = session.execute(stmt).fetchall()
print(result)"""
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

@app.route("/api/average_home_price")
def avg_price():
    results = db.session.query(Average_home_price.date, Average_home_price.average_home_price).all()

    date = [result[0] for result in results]
    average_home_price = [result[1] for result in results]
    

    home_price = [{
        
        "Date": date,
        "Average Home Price": average_home_price,
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(home_price)

"""@app.route("/api/homeownership_rate")
def o_rates():
    results = db.session.query(Homeownership_rates.date, Homeownership_rates.homeownership_rate).all()

    date = [result[0] for result in results]
    home_rate = [result[1] for result in results]
    

    ownership_rate = [{
        
        "Date": date,
        "Home Ownership Rate": home_rate,
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(ownership_rate)
"""

@app.route("/api/home_units")
def h_unit():
    results = db.session.query(Home_units.date, Home_units.units_constructed_thousands).all()

    date = [result[0] for result in results]
    units_contructed = [result[1] for result in results]
    

    unit_homes = [{
        
        "Date": date,
        "Home Unites Contructed": units_contructed,
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(unit_homes)

"""@app.route("/api/house_permits")
def permited():
    results = db.session.query(House_permits.date, House_permits.new_permits_thousands).all()

    date = [result[0] for result in results]
    new_permits = [result[1] for result in results]
    

    permits = [{
        
        "Date": date,
        "New Home Permits": new_permits,
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(permits)"""


@app.route("/api/monthly_house_supply")
def supply():
    results = db.session.query(Monthly_house_supply.date, Monthly_house_supply.ratio_for_sale_to_sold).all()

    date = [result[0] for result in results]
    sale_sold_ratio = [result[1] for result in results]
    
    home_supply = [{
        
        "Date": date,
        "Ratio of Sale/Sold": sale_sold_ratio,
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(home_supply)


@app.route("/api/interest_rate_2020")
def rates2020():
    results = db.session.query(New_2020.date, New_2020.ten_y_2020, New_2020.twenty_y_2020, New_2020.thirty_y_2020).all()

    date = [result[0] for result in results]
    ten_y_2020 = [result[1] for result in results]
    twenty_y_2020 = [result[2] for result in results]
    thirty_y_2020 = [result[3] for result in results]
    

    interest_2020 = [{
        
        "Date": date,
        "Ten Year": ten_y_2020,
        "Twenty Year" : twenty_y_2020,
        "Thirty Year": thirty_y_2020,
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(interest_2020)



@app.route("/api/interest_rate_2021")
def rates2021():
    results = db.session.query(New_2021.date, New_2021.ten_y_2021, New_2021.twenty_y_2021, New_2021.thirty_y_2021).all()

    date = [result[0] for result in results]
    ten_y_2021 = [result[1] for result in results]
    twenty_y_2021 = [result[2] for result in results]
    thirty_y_2021 = [result[3] for result in results]
    

    interest_2021 = [{
        
        "Date": date,
        "Ten Year": ten_y_2021,
        "Twenty Year" : twenty_y_2021,
        "Thirty Year": thirty_y_2021,
        "marker": {
            "size": 15,
            "line": {
                "color": "rgb(8,8,8)",
                "width": 1
            },
        }
    }]

    return jsonify(interest_2021)
#################################################
# Fontend Routes
#################################################
# create route that renders index.html template
# @app.route("/")
# def home():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run()

#session.close()