import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, send_from_directory, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv ("MONGO_URI")
app.secret_key = "super secret key"

mongo = PyMongo(app)



#Display Home page
@app.route('/', methods=["GET", "POST"])
def index():
    the_recipe = mongo.db.recipes.find()
    return render_template("index.html", page_title="Get fit with Fitness Cookbook",  recipe = the_recipe)


# Display Recipes Page
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", page_title="Recipes", recipes=mongo.db.recipes.find())

    
#Display Recipes Page sorted by Calories
@app.route('/get_recipes_calories', methods=["GET"])
def get_recipes_calories():
    recipes=mongo.db.recipes.find().sort('calories', -1)
    return render_template("recipes_by_calories.html", page_title="Recipes by Calories",recipes=recipes)
    
    
#Display Recipes Page sorted by Prep time
@app.route('/get_recipes_time', methods=["GET"])
def get_recipes_time():
    recipes=mongo.db.recipes.find().sort('cook_time', 1)
    return render_template("recipes_by_time.html", page_title="Recipes by Prep Time", recipes=recipes)
    
    
#Display Recipes Page sorted by Popularity
@app.route('/get_recipes_popular', methods=["GET"])
def get_recipes_popular():
    recipes=mongo.db.recipes.find().sort('cooked', -1)
    return render_template("recipes_by_popular.html", page_title="Recipes by Popularity",recipes=recipes)


# Display Edit Recipe Page 
@app.route('/edit_recipes/<recipe_id>', methods=["GET", "POST"])
def edit_recipes(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template("editrecipe.html",  page_title="Edit", recipe=the_recipe, categories=all_categories) 

# Display Delete Recipe Page 
@app.route('/delete_recipes/<recipe_id>', methods=["GET", "POST"])
def delete_recipes(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template("deleterecipe.html",  page_title="Delete", recipe=the_recipe, categories=all_categories)


# Display Add Recipes Page
@app.route('/add_recipes', methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        flash("Thanks, You have added a recipe to the database".format(
        ))
    return render_template("addrecipes.html", page_title="Recipes",  categories=mongo.db.categories.find())
    

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
        'category_name':request.form.get('category_name'),
        'recipe_description': request.form.get('recipe_description'),
        'image': request.form.get('image'),
        'recipe_ingredients':request.form.get('recipe_ingredients'),
        'recipe_preperation_1':request.form.get('recipe_preperation_1'),
        'recipe_preperation_2':request.form.get('recipe_preperation_2'),
        'recipe_preperation_3':request.form.get('recipe_preperation_3'),
        'recipe_preperation_4':request.form.get('recipe_preperation_4'),
        'amount':request.form.get('amount'),
        'preperation_time':request.form.get('preperation_time'),
        'cook_time':request.form.get('cook_time'),
        'calories':request.form.get('calories'),
        'fat':request.form.get('fat'),
        'protein':request.form.get('protein'),
        'carbohydrates':request.form.get('carbohydrates'),
        'label':request.form.get('label'),
        'cooked':request.form.get('cooked') 
    }
    mongo.db.recipes.insert_one(insert_recipes)
    print("Recipe Added!")
    return redirect(url_for('get_recipes'))
    

# Edit Recipes from Database
@app.route('/update_recipe/<recipe_id>', methods=['GET','POST'])
def update_recipe(recipe_id):
    if request.method == "POST":
            recipe = mongo.db.recipes
            recipe.update_one({'_id': ObjectId(recipe_id)},
            {"$set":
                 {'recipe_name':request.form.get('recipe_name'),
        'category_name':request.form.get('category_name'),
        'recipe_description': request.form.get('recipe_description'),
        'image': request.form.get('image'),
        'recipe_ingredients':request.form.get('recipe_ingredients'),
        'recipe_preperation_1':request.form.get('recipe_preperation_1'),
        'recipe_preperation_2':request.form.get('recipe_preperation_2'),
        'recipe_preperation_3':request.form.get('recipe_preperation_3'),
        'recipe_preperation_4':request.form.get('recipe_preperation_4'),
        'amount':request.form.get('amount'),
        'preperation_time':request.form.get('preperation_time'),
        'cook_time':request.form.get('cook_time'),
        'calories':request.form.get('calories'),
        'fat':request.form.get('fat'),
        'protein':request.form.get('protein'),
        'carbohydrates':request.form.get('carbohydrates'),
        'label':request.form.get('label'),
        'cooked':request.form.get('cooked')
                 }
             })
    return redirect(url_for('get_recipes'))
            

# Delete Recipe from Database
@app.route('/delete_recipe/<recipe_id>', methods = ['GET', 'POST'])
def delete_recipe(recipe_id):
    if request.method == "POST":
            recipe = mongo.db.recipes
            recipe.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

    
# Display Login Page
@app.route("/data")
def data():
    return render_template('data.html', page_title="Data Overview")    
    
    
# Login a User
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users =mongo.db.users
        user_login = users.find_one({'name' : request.form['username']})
        
        if user_login:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), user_login['password']) == user_login['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            flash('Invalid username/password combination')
    return render_template('login.html', page_title="Please Login")
    
# Logout a User
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Display Sign up Page
@app.route("/signup")
def signup():
    return render_template('signup.html', page_title="Please Signup")
    
# Sign up a user
@app.route("/insert_user", methods=["POST", "GET"])
def insert_user():
    if request.method == 'POST':
        users = mongo.db.users
        user_existing = users.find_one({'name' : request.form['username']})

        if user_existing is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        flash('That username already exists!')
        return redirect(url_for('signup'))
        
        

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)