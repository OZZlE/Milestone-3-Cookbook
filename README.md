# A cookbook website were you can create new recipes, read existing recipes, update existing recipes, and delete recipes.

## [Fitness Cookbook](https://cook-book-application.herokuapp.com/ "Milestone #3") 

#### To start the app in AWS type python3 app.py in the terminal and click the preview running app.

##### Keep it(mongodb key) in an environment variable and use `os.getenv()` or `os.environ.get()` to fetch it.

To do:
1. like/cooked button
2. search function (up not functioning)
3. sort by vegitarian, high protein, low carb, etc
4. health labels like high protien, low carb, low fat etc
5. login / sign up (page up not functioning)
6. single recipe overview
7. data overview 



### CREATE AN ONLINE COOKBOOK:

> Create a web application that allows users to store and easily access cooking recipes
    Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
    
   > 1. Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course)
    
>    2. Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation
    
 >   3. Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). 
    
  >  4. Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large
    
   > 4. Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions
    
>    5. Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages
   
 >   Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)

