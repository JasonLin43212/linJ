#A Dill Pickle -- Adil Gondal and Jason Lin
#SoftDev1 pd07
#K15 -- Oh yes, perhaps I do...
#2018-10-02

from flask import Flask, render_template, request
from flask import session, url_for, redirect, flash
import os
app = Flask(__name__) # instantiates an instance of Flask

app.secret_key = os.urandom(32) #generates a secret key

@app.route("/")
def login():
    if "username" in session: # checks if there was a previous session
        return redirect(url_for("welcome")) # redirects to welcome page if there was
    else:
        return render_template("login.html") # login page if no previous session

@app.route("/auth", methods=["POST"])
def auth():
    username=request.form["username"] # gets the username and password from form
    password= request.form["password"]
    if username == "Adil": # checks if username is correct
            if password=="Jason":
                session["username"] = username # if username and password is correct, creates a session
                return redirect(url_for("welcome")) # redirects to welcome page
            else:
                flash("Wrong Password")
                return redirect(url_for("login")) # redirects to error page (wrong password)
    else:
        flash("Wrong Username")
        return redirect(url_for("login")) #redirects to error page (wrong username)

@app.route("/welcome")
def welcome():
    if "username" in session: # checks if there was a previous session
        return render_template("welcome.html",user=session["username"]) #brings user to a welcome page
    else:
        return redirect(url_for("login")) # if no previous session, gives the login page
    
@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("login")) # removes username from session and goes back to login page


if __name__ == "__main__":
    app.debug = True
    app.run()
