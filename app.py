import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv ('MONGO_URI','mongodb+srv://root:root@myfirstcluster-vay7y.mongodb.net/cook_book?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
    
@app.route('/add_recipes')
def add_recipes():
    return render_template("addrecipes.html")
    
    
@app.route('/get_catagories')
def get_catagories():
    return render_template("catagories.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)