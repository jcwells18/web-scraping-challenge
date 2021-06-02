#import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

#create instance of Flask aspp
app = Flask(__name__)

#use pymongo to establish Mongo connection
mongo = PyMongo(app,uri="mongodb://localhost:27017/mars_app")

#create route that renders index.html template
@app.route("/")
def home():
    mars_dict= mongo.db.mars_dict.find_one()
    return render_template("index.html",mars=mars_dict)

@app.route("/scrape")
def scrape():
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape()

    mars_dict.update({}, mars_data,upsert=True)

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
