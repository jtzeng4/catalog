To use the program, there are two different files: database_setup.py and project.py. You must first initialize database_setup.py to create the database file. project.py has the functions to create and edit the website application.

After initializing the database with database_setup.py, run project.py to start the website.

The templates folder contains all of the html templates for each function.

*showLogin: shows the login state.
*fbconnect: connect through Facebook.
*gconnect: connect through Google+.
*createUser: creates a new user once connected through Facebook or Google+.
*getUserInfo: obtains the new user's information.
*getUserID: assigns an ID to the new user.

*showCategories: lists the categories in the database.
*categoriesJSON: lists the categories in the database in JSON format.
*newCategory: creates a new category to the database.
*editCategory: edits an existing category in the database.
*deleteCategory: deletes an existing category in the database.

*showItems: lists the items in a specific category
*itemsJSON: lists the items in a specific category in JSON format.
*newCategoryItem: creates a new item in a specific category.
*editCategoryItem: edits an existing item in a specific category.
*deleteCategoryItem: deletes an existing item in a specific category.

*fbdisconnect: disconnects from Facebook.
*gdisconnect: disconnects from Google+
*disconnect: disconnects from every connection.