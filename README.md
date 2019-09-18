# [Fitness Cookbook](https://cook-book-application.herokuapp.com/ "Milestone #3") 

### A website to help the hungry stay healthy and fit in the kitchen and in life. This site focuses on calories, popularity and cooking time so the user can get the recipe they need and start cooking right away.

### UX

I created this website to help hungry people who are looking to eat healthy and help decide what to eat. I made it so users who would be ready to cook in the kitchen would have the information they needed and nothing else.

**User Story 1:**
John Doe is curious about the purpose of the site. He can read about the reason it was created on the home page.

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

- User is able to view all the recipes by clicking the "recipes" on the navbar.

- User is able to view all the data by clicking "Data" on the navbar.

- User is able to add a recipe after logging in or signing up by clicking "add a recipe" on the navbar and filling out the form.

- User is able to login or sign up by clicking "login/signup" on the navbar and filling out the form.

- User is able to read about a specific recipe by clicking its name in the recipes page. 

- User is able to edit a specific recipe after logging in or signing up by clicking "edit Recipe" at the bottom of the recipe page and filling out the form. 

- User is able to delete a specific recipe after logging in or signing up by clicking "delete Recipe" at the bottom of the recipe page and comfiming on the next page. 

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

This site was tested across various browsers and browser sizes. Multiple times I used [JSHint](https://jshint.com/) to double check my javascript and [W3 validator](https://validator.w3.org/)  to debug and remove extra tags in my code. I used [Responsinator](https://www.responsinator.com) to check the responsiveness of my site in various devices.

Automated testing using Jasmine was not used as there is not Javascript logic in the site. The only JS written excluding what came with the theme came from materialize which was the sidenav for mobile use.

Testing using Unit test was used...

### Deployment

This website was deployed through Heroku directly from the master branch. Using a Procfile and a requirments.txt file Heroku installs the required software in order to run the site. 

In order to run the code locally simply download the files, start up Visual Studio Code or your IDE of choice to check it out. You must have python installed. The difference between the development version and deployment version are little to none. The database is stored on mongodb and is set up through Heroku.

### Things to do in the Future

- More Recipes with better photos.

### Credits

I had trouble finding pictures that matched the recipes so I used the best image from google image search.

### Acknowledgements

- I received inspiration for this project from the 5/5  [example project](https://code-institute-solutions.github.io/StudentExampleProjectGradeFive/)

- The recipes I used are from the wonderful cookbook [The Ultimate Bodybuilding Cookbook](https://www.amazon.com/Ultimate-Bodybuilding-Cookbook-High-Impact-Stronger/dp/162315765X). I highly recommend it.

- Specials Thanks to the student slack channels, my mentor and stackoverflow.

## Mock ups

![Home_Web](https://cook-book-application.herokuapp.com/static/img/mockups/Home_Web.png)

![Home_Phone](https://cook-book-application.herokuapp.com/static/img/mockups/Home_Phone.png)

![Add_Recipe_Phone](https://cook-book-application.herokuapp.com/static/img/mockups/Add_Recipe_Phone.png)

![Add_Recipe_Web](https://cook-book-application.herokuapp.com/static/img/mockups/Add_Recipe_Web.png)

![Data_Page_Phone](https://cook-book-application.herokuapp.com/static/img/mockups/Data_Page_Phone.png)

![Data_Page_Web](https://cook-book-application.herokuapp.com/static/img/mockups/Data_Page_Web.png)

![Login_Web](https://cook-book-application.herokuapp.com/static/img/mockups/Login_Web.png)

![Login_Phone](https://cook-book-application.herokuapp.com/static/img/mockups/Login_Phone.png)

![Recipe_Name_Delete_Phone](https://cook-book-application.herokuapp.com/static/img/mockups/Recipe_Name_Delete_Phone.png)

![Recipe_Name_Delete_Web](https://cook-book-application.herokuapp.com/static/img/mockups/Recipe_Name_Delete_Web.png)

![Recipe_Name_Edit_Phone](https://cook-book-application.herokuapp.com/static/img/mockups/Recipe_Name_Edit_Phone.png)

![Recipe_Name_Edit_Web](https://cook-book-application.herokuapp.com/static/img/mockups/Recipe_Name_Edit_Web.png)

![Recipe_Name_Phone](https://cook-book-application.herokuapp.com/static/img/mockups/Recipe_Name_Phone.png)

![Recipe_Name_Web](https://cook-book-application.herokuapp.com/static/img/mockups/Recipe_Name_Web.png)

![Recipes_Phone](https://cook-book-application.herokuapp.com/static/img/mockups/Recipes_Phone.png)

![Recipes_Web](https://cook-book-application.herokuapp.com/static/img/mockups/Recipes_Web.png)