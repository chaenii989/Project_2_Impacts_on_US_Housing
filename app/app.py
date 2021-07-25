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




#################################################
# API Routes (start with '/api/')
#################################################
@app.route("/api/average_home_price")
def avg_price():
    results = db.session.query(average_home_price.date, average_home_price.average_home_price).all()

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


@app.route("/api/home_units")
def h_unit():
    results = db.session.query(home_units.date, home_units.units_constructed_thousands).all()

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


@app.route("/api/homeownership_rates")
def o_rates():
    results = db.session.query(homeownership_rates.date, homeownership_rates.homeownership_rate).all()

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




@app.route("/api/house_permits")
def permited():
    results = db.session.query(hhouse_permits.date, house_permits.new_permits_thousands).all()

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

    return jsonify(permits)


@app.route("/api/monthly_house_supply")
def supply():
    results = db.session.query(monthly_house_supply.date, monthly_house_supply.ratio_for_sale_to_sold).all()

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


@app.route("/api/interst_rate_2020")
def rates2020():
    results = db.session.query(new_2020.date, new2020.ten_y_2020, new2020.twenty_y_2020, new2020.thirty_y_2020).all()

    date = [result[0] for result in results]
    ten_y_2020 = [result[1] for result in results]
    twenty_y_2020 = [result[2] for result in results]
    thirty_y_2020 = [result[3] for result in results]
    

    interset_2020 = [{
        
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

    return jsonify(interset_2020)


@app.route("/api/monthly_house_supply")
def rates2021():
    results = db.session.query(monthly_house_supply.date, monthly_house_supply.ratio_for_sale_to_sold).all()

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


@app.route("/api/interst_rate_2021")
def h_unit():
    results = db.session.query(new_20201.date, new2021.ten_y_2021, new2021.twenty_y_2021, new2021.thirty_y_2021).all()

    date = [result[0] for result in results]
    ten_y_2021 = [result[1] for result in results]
    twenty_y_2021 = [result[2] for result in results]
    thirty_y_2021 = [result[3] for result in results]
    

    interset_2021 = [{
        
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

    return jsonify(interset_2021)


#################################################
# Fontend Routes
#################################################
# create route that renders index.html template
# @app.route("/")
# def home():
#     return render_template("index.html")




if __name__ == "__main__":
    app.run()
