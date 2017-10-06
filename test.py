from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)


@app.route("/stuff")
def login():
    return "thing"

@app.route("/woo", methods=["GET","POST"])
def logged():
    return login()


#necessary to run the app
if __name__ == "__main__":
    app.debug = True
    app.run()
