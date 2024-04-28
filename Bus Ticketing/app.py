from flask import Flask, request

app = Flask(__name__)

@app.route("/Login")
def loginPage():
    return loginPage

@app.route("/")
def homePage():
    return homePage