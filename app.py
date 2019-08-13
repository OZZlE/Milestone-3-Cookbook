import os
from flask import Flask, render_template, redirect, request, url_for, send_from_directory, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv ('MONGO_URI','mongodb+srv://root:root@myfirstcluster-vay7y.mongodb.net/cook_book?retryWrites=true&w=majority')

mongo = PyMongo(app)

#Display Home page
@app.route('/')
def index():
    return render_template("index.html")

# Display Recipes Page
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", page_title="Recipes", recipes=mongo.db.recipes.find())
    
# Display Edit Recipe Page 
@app.route('/edit_recipes/<recipe_id>', methods=["GET", "POST"])
def edit_recipes(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    if request.method == "POST":
        flash("Thanks, You have edited a recipe from the database".format(
        ))
    return render_template("editrecipe.html",  page_title="Edit", recipe=the_recipe, categories=all_categories) 

# Display Delete Recipe Page 
@app.route('/delete_recipes/<recipe_id>', methods=["GET", "POST"])
def delete_recipes(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    if request.method == "POST":
        flash("Thanks, You have deleted a recipe from the database".format(
        ))
    return render_template("deleterecipe.html",  page_title="Delete", recipe=the_recipe, categories=all_categories)


# Display Add Recipes Page
@app.route('/add_recipes', methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        flash("Thanks, You have added a recipe to the database".format(
        ))
    return render_template("addrecipes.html", page_title="Add a Recipe",  categories=mongo.db.categories.find())
    

# Route for viewing a single recipe in detail.
@app.route('/recipe_page/<recipe_id>', methods=['GET', 'POST'])
def recipe_page(recipe_id):
    a_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe_name.html', page_title="Get Cooking", recipes=a_recipe)

    
# Add Recipe to Database
@app.route('/insert_recipes', methods=['POST'])
def insert_recipes():
    insert_recipes = {
        'recipe_name':request.form.get('recipe_name'),
        'category_names':request.form.get('category_names'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_image': request.form.get('recipe_image'),
        'recipe_ingredients':request.form.get('recipe_ingredients'),
        'recipe_preperation_1':request.form.get('recipe_preperation_1'),
        'recipe_preperation_2':request.form.get('recipe_preperation_2'),
        'recipe_preperation_3':request.form.get('recipe_preperation_3'),
        'recipe_preperation_4':request.form.get('recipe_preperation_4'),
        'recipe_amount':request.form.get('recipe_amount'),
        'recipe_preperation_time':request.form.get('recipe_preperation_time'),
        'recipe_cook_time':request.form.get('recipe_cook_time'),
        'recipe_calories':request.form.get('recipe_calories'),
        'recipe_fat':request.form.get('recipe_fat'),
        'recipe_protein':request.form.get('recipe_protein') 
    }
    mongo.db.recipes.insert_one(insert_recipes)
    print("Recipe Added!")
    return redirect(url_for('get_recipes'))
    

# Edit Recipes from Database
#sends to update_recipe page?
@app.route('/update_recipe/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
	if request.method == "POST":
            recipe = mongo.db.recipes
            recipe.update_one({'_id': ObjectId(recipe_id)},
       {'recipe_name':request.form.get('recipe_name'),
        'category_names':request.form.get('category_names'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_image': request.form.get('recipe_image'),
        'recipe_ingredients':request.form.get('recipe_ingredients'),
        'recipe_preperation_1':request.form.get('recipe_preperation_1'),
        'recipe_preperation_2':request.form.get('recipe_preperation_2'),
        'recipe_preperation_3':request.form.get('recipe_preperation_3'),
        'recipe_preperation_4':request.form.get('recipe_preperation_4'),
        'recipe_amount':request.form.get('recipe_amount'),
        'recipe_preperation_time':request.form.get('recipe_preperation_time'),
        'recipe_cook_time':request.form.get('recipe_cook_time'),
        'recipe_calories':request.form.get('recipe_calories'),
        'recipe_fat':request.form.get('recipe_fat'),
        'recipe_protein':request.form.get('recipe_protein')})
            return redirect(url_for('get_recipes'))
	return render_template('edit_recipes')


###

# Delete Recipe from Database
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    
    

# Get Category from Database
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html', page_title="Categories",
                           categories=mongo.db.categories.find())

# Delete Category from Database
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))

# Edit Category from Database
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html', page_title="Edit a Category", 
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))

# Insert Category from Database
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))

# Display Category from Database
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html', page_title="Add a Category")
    
# Display Login Page
@app.route("/login")
def login():
    return render_template('login.html', page_title="Signup or Login")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)