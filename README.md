# A cookbook website were you can create new recipes, read existing recipes, update existing recipes, and delete recipes.

## [Fitness Cookbook](https://cook-book-application.herokuapp.com/ "Milestone #3") 

#### To start the app in AWS type python3 app.py in the terminal and click the preview running app.

##### Keep it(mongodb key) in an environment variable and use `os.getenv()` or `os.environ.get()` to fetch it.

To do:
4. login / sign up 



### CREATE AN ONLINE COOKBOOK:

> Create a web application that allows users to store and easily access cooking recipes
    Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
    
>    2. Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation
    
 >   Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure) (Y)
 

## A website to help the hungry stay healthy and fit in the kitchen and in life.

### UX

I created this website to help hungry people who are looking to eat healthy and help decide what to eat. I made it so users who would be ready to cook in the kitchen would have the information they needed and nothing else.

**User Story 1:**
John Doe is curious about the recipe of the day. He can click on the home page to see what it is.

**User Story 2:**
Jane Doe wants to browse the recipes. She can do that by clicking "recipes" in the nav bar.

**User Story 3:**
Jeff Doe wants to read more about a specific recipe. He can do that by clicking on its name in the recipes page.

**User Story 4:**
Jerry Doe wants to add  new recipe. He can so by clicking the "Add a recipe" in the nav bar and filling out the following form.

**User Story 5:**
Jane Doe wants to edit an incorrect recipe. She can do so by clicking the "edit recipe" button in the specific recipe page and filling out the following form.

**User Story 6:**
John Doe wants to delete a recipe. He can do so by clicking the "delete recipe" button in the specific recipe page and filling out the following form.

**User Story 7:**
Jeff Doe wants to view the data about all of the recipes. He can do so by clicking on "Data" in the navbar.

**User Story 8:**
Jane Doe wants to login. She can do so by clicking on "login/Signup" in the navbar and filling out the following form.

**User Story 9:**
John Doe wants to sign up. She can do so by clicking on "login/Signup" in the navbar and filling out the following form.

### Features

- User is able to view the recipe of the day by clicking the home page.

- User is able to view all the recipes by clicking the "recipes" on the navbar.

- User is able to view all the data by clicking "Data" on the navbar.

- User is able to add a recipe by clicking "add a recipe" on the navbar and filling out the form.

- User is able to login or sign up by clicking "login/signup" on the navbar and filling out the form.

- User is able to read about a specific recipe by clicking its name in the recipes page. 

- User is able to edit a specific recipe by clicking "edit Recipe" at the bottom of the recipe page and filling out the form. 

- User is able to delete a specific recipe by clicking "delete Recipe" at the bottom of the recipe page and comfiming on the next page. 

- User is able to sort the recipes by clicking "Popular" or "calories" or "cook time" on the recipes page.

- User is able to clear the sort by clicking "clear" and returning to the recipes page.

### Technologies Used

- **HTML**

- **CSS**

- **Bootstrap**  - The project uses bootstrap for the navbar, modals, and responsiveness.

- **jQuery**  - The project uses JQuery to simplify DOM manipulation.

- **Google Fonts**  - The project uses Google fonts in order to use the Roboto Font.

- **Font Awesome**  - The project uses Font Awesome in order to display various icons for social media and the hamburger menu in mobile view.

- **Python** - This project uses python to execute the logic.

- **Flask** - This project uses Flask to display the webpages.

- **Mongodb** - This project uses Mongodb to store and access its recipe information.

### Testing

This site was tested across various browsers and browser sizes. Multiple times I used [JSHint](https://jshint.com/) to double check my javascript and [W3 validator](https://validator.w3.org/)  to debug and remove extra tags in my code.

### Deployment

This website was deployed through Heroku directly from the master branch. In order to run the code locally simply download the files, start up Visual Studio Code or your IDE of choice to check it out. You must have python installed. The difference between the development version and deployment version are little to none.

### Things to do in the Future

-Add a working login / sign up feature.

- More Recipes with better photos.

### Credits

Photos from

-[pixabay](https://pixabay.com/)

### Acknowledgements

- I received inspiration for this project from the 5/5  [example project](https://code-institute-solutions.github.io/StudentExampleProjectGradeFive/)

- The recipes I used are from the wonderful cookbook [The Ultimate Bodybuilding Cookbook: High-Impact Recipes to Make You Stronger Than Ever by Kendall Lou Schmidt](https://www.amazon.com/Ultimate-Bodybuilding-Cookbook-High-Impact-Stronger/dp/162315765X)

- Specials Thanks to the student slack channels, my mentor and stackoverflow.

## Mock ups

![]()
