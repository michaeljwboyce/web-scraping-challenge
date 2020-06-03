from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape
import os

app=Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    mars_scrapes = mongo.db.mars_scrapes.find()
    return render_template("index.html", mars_scrapes=mars_scrapes)


@app.route("/scrape")
def scrape():
    # drop any data that is in the db
    db.mars_results.drop()
    mars_data = scrape_mars.scrape()

    db.mars_results.insert_one(mars_data)

    # Using Flask' redirect function

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)