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
    return render_template("addrecipes.html", categories=mongo.db.categories.find())
    
    
@app.route('/get_categories')
def get_categories():
    return render_template("categories.html", categories=mongo.db.categories.find())

       
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipes')
# add <task_id> after /edit_recipes after assinging recipe_id
def edit_recipes(recipes_id):
    return render_template("edit_recipes.html")
    # the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    # all_categories =  mongo.db.categories.find()
    # return render_template('editrecipe.html', recipe=the_recipe,
    #                       categories=all_categories)


@app.route('/update_recipe/<recipes_id>', methods=["POST"])
def update_recipe(recipes_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipes_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_name':request.form.get('category_name'),
        'recipe_description': request.form.get('recipe_description')
        # 'due_date': request.form.get('due_date'),
        # 'is_urgent':request.form.get('is_urgent')
    })
# return redirect(url_for('get_recipes'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)