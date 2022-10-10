# Dependencies 
import datetime as dt
import numpy as np
import pandas as pd

# Dependencies we need for SQLAlchemy,
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Add the code to import the dependencies for Flask, This dependency will enable your code to access all that Flask has to offer
from flask import Flask, jsonify

# Set up our database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes.
Base = automap_base()

# Python Flask function to reflect the tables
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database 
session = Session(engine)


# *** All of your routes should go after the app = Flask(__name__) line of code. Otherwise, your code may not run properly.
# Define our Flask app
app = Flask(__name__)

# Define the welcome route , also known as the root (first route)
@app.route("/")

# Create a function welcome() with a return statement, add the precipitation, stations, tobs, and temp routes
# Use f-strings
# Naming convention /api/v1.0/ followed by the name of the route signifies that this is version 1 of our application. This line can be updated to support future versions of the app as well.
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# create the route for precipitation analysis
@app.route("/api/v1.0/precipitation")

# Create the precipitation() function.
def precipitation():
    # Add the line of code that calculates the date one year ago from the most recent date in the database
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   # Write a query to get the date and precipitation for the previous year
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   # Create a dictionary with the date as the key and the precipitation as the value
   precip = {date: prcp for date, prcp in precipitation}
   # Jsonify() is a function that converts the dictionary to a JSON file
   return jsonify(precip)

# Create the route for stations
@app.route("/api/v1.0/stations")

# Create a new function called stations()
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results)) # unraveling our results into a one-dimensional array, with results as our parameter.
    return jsonify(stations=stations)

# Return the temperature observations for the previous year
@app.route("/api/v1.0/tobs")

# Create a function called temp_monthly()
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()

    # Unravel the results into a one-dimensional array and convert that array into a list  
    temps = list(np.ravel(results))

    # Jsonify our temps
    return jsonify(temps=temps)

# Last route will be to report on the minimum, average, and maximum temperatures with a both a starting and ending date
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create a function called stats()
def stats(start=None, end=None): # add parameters to our stats()function: a start parameter and an end parameter

    # Create a query to select the minimum, average, and maximum temperatures with a list called sel
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Determine the starting and ending date, add an if-not statement 
    if not end:
        # Asterisk sel is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    # Create our next query, which will get our statistics data calculating the temperature minimum, average, and maximum with the start and end dates.

    temps = list(np.ravel(results))
    return jsonify(temps)

   #*** copy and paste the web address ,fix this by entering any date in the dataset as a start and end date.For example, let's say we want to find the minimum, maximum, and average temperatures for June 2017
   # /api/v1.0/temp/2017-06-01/2017-06-30 ****