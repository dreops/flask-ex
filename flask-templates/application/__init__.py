# import Flask class from the flask module
from flask import Flask
# craete a new instance of Flask and store it in app
app = Flask(__name__)
# import the ./applicaiton/routes.py file
from application import routes