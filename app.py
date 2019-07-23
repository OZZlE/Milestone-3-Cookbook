import os
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
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

# Get Recipes from Database
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", page_title="Recipes", recipes=mongo.db.recipes.find())
    
# Edit Recipe Page 
# Not Working
@app.route('/edit_recipes', methods=["GET", "POST"])
def edit_recipes():
    recipes=mongo.db.recipes.find()
    edit_recipes = mongo.db.recipes.find_one({"_id": ObjectId()})
    all_categories =  mongo.db.categories.find()
    return render_template("editrecipe.html",  page_title="Edit a Recipe", recipes_id=ObjectId, edit_recipes=edit_recipes, categories=all_categories) 


# Add Recipes Page
@app.route('/add_recipes', methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        print("Recipe Added!")
    return render_template("addrecipes.html", page_title="Add a Recipe",  categories=mongo.db.categories.find())
    
# Display Recipe Page from ID
@app.route('/recipes/{{recipe.url}}')
def get_recipes_id(recipes_id):
    return render_template("recipes_name.html", page_title="{{recipes_name}}", recipes=mongo.db.recipes.find())
    
# Add Recipe to Database
@app.route('/insert_recipes', methods=['POST'])
def insert_recipes():
    recipe =  mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
# Edit Recipes from Database
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipe
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_names':request.form.get('category_names'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe.image': request.form.get('recipe.image'),
        'recipe_ingredients':request.form.get('recipe_ingredients'),
        'recipe_preperation_1':request.form.get('recipe_preperation_1'),
        'recipe_preperation_2':request.form.get('recipe_preperation_2'),
        'recipe_preperation_3':request.form.get('recipe_preperation_3'),
        'recipe_preperation_4':request.form.get('recipe_preperation_4'),
        'recipe.amount':request.form.get('recipe.amount'),
        'recipe.preperation_time':request.form.get('recipe.preperation_time'),
        'recipe.cook_time':request.form.get('recipe.cook_time'),
        'recipe.calories':request.form.get('recipe.calories'),
        'recipe.fat':request.form.get('recipe.fat'),
        'recipe.protein':request.form.get('recipe.protein')
    })
    return redirect(url_for('get_recipes'))


###

# Delete Recipe from Database
@app.route('/delete_recipe/<recipes_id>')
def delete_recipe(recipes_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipes_id)})
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