import numpy as np

from flask import Flask, jsonify

import sqlite3

import datetime as dt

justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to Lorie's 2040 Version of Justice League API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/justice-league<br/>"
        f"/api/v1.0/justice-league/Arthur%20Curry<br/>"
        f"/api/v1.0/justice-league/Bruce%20Wayne<br/>"
        f"/api/v1.0/justice-league/Victor%20Stone<br/>"
        f"/api/v1.0/justice-league/Barry%20Allen<br/>"
        f"/api/v1.0/justice-league/Hal%20Jordan<br/>"
        f"/api/v1.0/justice-league/Clark%20Kent/Kal-El<br/>"
        f"/api/v1.0/justice-league/Princess%20Diana<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station_all<br/>"
        f"/api/v1.0/station_id<br/>"
        f"/api/v1.0/station_name<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/my_column<br/>"
        f"/api/v1.0/date<br>"
        f"/api/v1.0/lorie_test<br>"
        f"/api/v1.0/between_date<br>"

    )

@app.route("/api/v1.0/justice-league")
def justice_league():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a Dictionary using date as the key and prcp as the value."""
    """Return the JSON representation of your dictionary."""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
  
    cur.execute("SELECT date, prcp from measurement where date >= '2016-08-23'")
    rows = cur.fetchall()
    precip_list = []
    for row in rows:
        precip_list.append(row)

# Dict with date as the key and prcp as the value
    precip = {date: prcp for date, prcp in precip_list}

    return jsonify(precip)

@app.route("/api/v1.0/station_all")
def station_all():
    """Return the all data as json"""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * from station")
    rows = cur.fetchall()
    station_list = []
    for row in rows:
        station_list.append(row)

    return jsonify(station_list)


@app.route("/api/v1.0/station_id")
def station_id():
    """Return the station id as json"""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT station from station")
    rows = cur.fetchall()
    station_list = []
    for row in rows:
        station_list.append(row[0])

    return jsonify(station_list)

@app.route("/api/v1.0/station_name")
def station_name():
    """Return the station name as json"""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT name from station")
    rows = cur.fetchall()
    station_list = []
    for row in rows:
        station_list.append(row[0])

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return the Temperature Observations (tobs) for the previous year as json"""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT tobs from measurement where date >= '2016-08-24' order by date desc")
    rows = cur.fetchall()
    station_list = []
    for row in rows:
        station_list.append(row[0])

    return jsonify(station_list)

@app.route("/api/v1.0/my_column/<input_column>")
def myColumn(input_column):
    """PRACTICE - return values from a single column when user specifies column"""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT " + str(input_column) + " from measurement")
    rows = cur.fetchall()
    column_list = []
    for row in rows:
        column_list.append(row[0])

    columndata = dict()
    columndata["column name"] = input_column
    columndata["result"] = column_list
    return jsonify(columndata)



@app.route("/api/v1.0/lorie_test/<input_column>")
def lorieTest(input_column):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    """When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    peach = str(input_column)
    print(peach)
    cur.execute("SELECT * from measurement where station =" + str(input_column))


    rows = cur.fetchall()
    column_list = []
    for row in rows:
        column_list.append(row[0])

    columndata = dict()
    columndata["seleced station"] = input_column
    columndata["result"] = column_list
    return jsonify(columndata)


@app.route("/api/v1.0/date/<input_column>")
def start_date(input_column):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    """When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    peach = str(input_column)
    print("Peach date:  " + peach)
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >= '%s' " % peach)
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >=" + str(peach))
    #Sean's help
    cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where Date(date) >= Date(" + str(input_column) + ")")
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >=" + str(input_column))
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >= '%s';" % input_column)
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >= '%s';" % peach)

    rows = cur.fetchall()
    column_list = []
    for row in rows:
        column_list.append(row)

    columndata = dict()
    columndata["seleced date"] = input_column
    columndata["result"] = column_list
    return jsonify(columndata)

@app.route("/api/v1.0/between_date/<in_date1>/<in_date2>")
def between_date(in_date1,in_date2):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    """When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    
    #Convert the input dates to variables
    print("Input Date1:  " + in_date1)
    date1 = str(in_date1)
    print("Date1:  "  + date1)
    
    print("Input Date2:  " + in_date2)
    date2 = str(in_date2)
    print("Date2:  " + date2)

    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >= '%s' " % peach)
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >=" + str(peach))
    #Sean's help
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where Date(date) >= Date(" + str(input_column) + ")")
    cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >=" + str(date1) + " and date <= " + str(date2))
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >= '%s';" % input_column)
    #cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where date >= '%s';" % peach)

    rows = cur.fetchall()
    column_list = []
    for row in rows:
        column_list.append(row)

    columndata = dict()
    columndata["selected start date"] = date1
    columndata["selected end date"] = date2
    columndata["result"] = column_list
    return jsonify(columndata)

@app.route("/api/v1.0/justice-league/<real_name>")
def justice_league_character(real_name):
    """Fetch the Justice League character whose real_name matches
       the path variable supplied by the user, or a 404 if not."""

    canonicalized = real_name.replace(" ", "").lower()
    for character in justice_league_members:
        search_term = character["real_name"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(character)

    return jsonify({"error": f"Character with real_name {real_name} not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)