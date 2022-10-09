# This dependency will enable your code to access all that Flask has to offer
from flask import Flask

# Create a new Flask app instance
app = Flask(__name__)

# Create our first route. Define the starting point, also known as the root
@app.route('/')
# create a function called hello_world().Whenever you make a route in Flask, you put the code you want in that specific route below @app.route()
def hello_world():
    return 'Hello world'

