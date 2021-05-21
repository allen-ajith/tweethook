from flask import Flask
from os import environ

app = Flask(__name__)
app.run(environ.get('PORT'))