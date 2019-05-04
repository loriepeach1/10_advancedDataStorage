import numpy as np

from flask import Flask, jsonify

import sqlite3

import datetime as dt


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

#  3A. Home page. 
#  List all routes that are available.
@app.route("/")
def welcome():
    return (
        f"Welcome to Assignment #10!   Using SQL to obtain surfing weather data in Hawaii!<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"  
        f"/api/v1.0/station_all<br/>"
        f"<br/>"  
        f"/api/v1.0/station_id<br/>"
        f"<br/>"  
        f"/api/v1.0/station_name<br/>"
        f"<br/>"  
        f"/api/v1.0/tobs<br/>"
        f"<br/>"  
        f"/api/v1.0/my_column<br/>"
        f"<br/>"  
        f"/api/v1.0/lorie_test<br>"
        f"<br/>"
        f"/api/v1.0/date<br>"
        f"<br/>"  


    )

###########################################################################################
# 3B. /api/v1.0/precipitation 
# Convert the query results to a Dictionary using date as the key and prcp as the value. 
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():

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

##################################################################
# 3C. /api/v1.0/stations 
# Return a JSON list of stations from the dataset.

#Practice - return all station data
@app.route("/api/v1.0/station_all")
def station_all():

    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT * from station")
    rows = cur.fetchall()
    station_list = []
    for row in rows:
        station_list.append(row)

    return jsonify(station_list)

#return only the station ID
@app.route("/api/v1.0/station_id")
def station_id():

    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT station from station")
    rows = cur.fetchall()
    station_list = []
    for row in rows:
        station_list.append(row[0])

    return jsonify(station_list)

#return the station names
@app.route("/api/v1.0/station_name")
def station_name():
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT name from station")
    rows = cur.fetchall()
    station_list = []
    for row in rows:
        station_list.append(row[0])

    return jsonify(station_list)

############################################################################################
# 3D. /api/v1.0/tobs 
# query for the dates and temperature observations from a year from the last data point. 
# Return a JSON list of Temperature Observations (tobs) for the previous year.




@app.route("/api/v1.0/tobs")
def tobs():

    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()

    #find the date which is the last date  in the dataset.
    cur.execute("SELECT max(date) as maxDate from measurement")  
    rows = cur.fetchall()
 
    for row in rows:
        maxDate = row[0]  # without this, the variable will NOT be saved for later use
    print(row)
    print("maxDate: " +str(maxDate))
    


    #Subtract 365 days from the last date found
    maxDate = dt.datetime.strptime(maxDate, '%Y-%m-%d')
    prev_year = maxDate - dt.timedelta(days=365)
    print("prev_year: " +str(prev_year))
    prevYear_s = str(prev_year)
    print("prevYear_s: " +str(prevYear_s))
    print("prevYear_s type: "+ str(type(prevYear_s)))

    cur.execute("SELECT tobs from measurement where Date(date) >= Date('" + str(prevYear_s) + "') order by date desc")    
    rows = cur.fetchall()
    station_list = []
    for row in rows:
        station_list.append(row[0])

    return jsonify(station_list)


# Lorie Practice (not part of homework)
#Create a query for all contents from the column.
@app.route("/api/v1.0/my_column/<input_column>")
def myColumn(input_column):

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


# Lorie Practice (not part of homework)
# create a query using type string.   No date format.
@app.route("/api/v1.0/lorie_test/<input_column>")
def lorieTest(input_column):
   
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

###############################################
# 3E. /api/v1.0/ and /api/v1.0// 
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range. 
# 3E1. When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date. 


@app.route("/api/v1.0/<input_column>")
def start_date(input_column):

    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    peach = str(input_column)
    print("Peach date:  " + peach)

    cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where Date(date) >= Date('" + str(input_column) + "')")


    rows = cur.fetchall()
    column_list = []
    for row in rows:
        column_list.append(row)

    columndata = dict()
    columndata["seleced date"] = input_column
    columndata["result"] = column_list
    return jsonify(columndata)

#########################################################################################################################################
# 3E. /api/v1.0/ and /api/v1.0// 
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range. 
# 3E2. When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.


@app.route("/api/v1.0/<startS>/<endS>")
def between_date(startS,endS):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    """When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""
    conn = sqlite3.connect("Resources/hawaii.sqlite")
    cur = conn.cursor()
    
    #Convert the input dates to variables
    print("Input Date1:  " + startS)
    print("Input Date2:  " + endS)

    cur.execute("SELECT min(tobs), max(tobs), avg(tobs) from measurement where Date(date) >= Date('" + str(startS) + "') and Date(date) <= Date('" + str(endS) + "')")

    rows = cur.fetchall()
    column_list = []
    for row in rows:
        column_list.append(row)

    columndata = dict()
    columndata["selected start date"] = startS
    columndata["selected end date"] = endS
    columndata["result"] = column_list
    return jsonify(columndata)


if __name__ == "__main__":
    app.run(debug=True)