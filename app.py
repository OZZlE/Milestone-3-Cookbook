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
    return render_template("recipes.html", page_title="Recipes", recipes=mongo.db.recipes.find())
    
@app.route('/get_recipes/<recipe_name>')
def recipes(recipe_name):
    recipe_name = {}
    
    with open("mongo.db.recipes", "r") as mongodb:
        mongo.db.recipes = recipes=mongo.db.recipes.find()
        for obj in mongo.db.recipes:
            if obj["url"] == recipe_name:
                recipe_name = obj
    return render_template("recipe_name.html", recipes=recipes, page_title="<recipe_name>")    

    
@app.route('/add_recipes', methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        print("Recipe Added!")
        
    return render_template("addrecipes.html", page_title="Add a Recipe",  categories=mongo.db.categories.find())
    
    
@app.route('/get_categories')
def get_categories():
    return render_template("categories.html", page_title="Categories" , category_names=mongo.db.categories.find())

       

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)