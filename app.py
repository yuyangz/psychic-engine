#Ibnul Jahan and Daria Shifrina
#SoftDev pd 7
#HW07 -- Do I Know You?
#2017-10-04

#lots to import
from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)

#creates String of 26 random characters
app.secret_key = os.urandom(26)

#initial login page will render form if not logged in already, and will render a greeting otherwise
@app.route("/")
def login():
    #initializes username
    username = ""
    #"username" is the key that would be in the session dictionary if the user is logged in after inputting data into the form
    if "username" in session:
        username = session["username"]
        #return the greeting page if the user is logged in
        return render_template("greet.html", username= username)
    #return the login page if thet are not
    return render_template("form.html", username = username)

#woo will check to see the inputted username and password combination match the one on record
@app.route("/woo", methods=["GET","POST"])
def logged():
    #if someone is currently in session, it logs them out after the form is filled
    if "username" in session:
        session.pop("username")
    username = request.form["username"]
    password = request.form["password"]

    #poo is our account username, and pee is the respective password
    if(username == "poo" and password == "pee"):
        session["username"] = username
        #if both username and password match, show them the greet page
        return render_template("greet.html", username= username)
    #tell user their username is wrong if it does not match
    if(username != "poo"):
        return "Your <b>username</b> is incorrect. You entered <i>" + username + "</i>, but we do not have this account on record. <a href='/'>Try again</a>.<br>Remember, usernames are case-sensitive."
    #tell user their password is wrong if it does not match
    if(password != "pee"):
        return "Your <b>password</b> is incorrect. <a href='/'>Try again</a>.<br>Remember, passwords are case-sensitive."

#Removes user from the session (if they were in it to begin with), and then tells them
@app.route("/loggedout", methods=["GET","POST"])
def loggedput():
    #removes the username saved from the session
    if "username" in session:
        session.pop("username")
        return "You have been successfully logged out. Go <a href='/'>back</a>"
    return "You were never logged in. Try signing in  <a href='/'>here</a>"

#necessary to run the app
if __name__ == "__main__":
    app.debug = True
    app.run()
