# CMSC 447 Homework 1 Submission
# Mark Biegel
# Professor Allgood
# Monday/Wednesday 5:30-6:45 Section
# Contact: mbiegel1@umbc.edu
###

## Objective
This application follows a CRUD (Create, Read, Update, Delete) process for database management.
Flask is used as a back-end to communicate with HTML on the front-end. An SQL database is used
to hold the data in the program via SQLite3. Faetures such as adding a new user, updating an existing user,
looking up a user or displaying all users, and deleteing a user or all users are functions of 
this CRUD application.


### Design
The design uses HTML. The output is basic and slightly cumbersome; however, the core functionality
is preserved and it enough to get the job done. Front-end could be updated using JavaScript and React;
however, my knowledge of either is very limited and my attempt at it proved that at the moment, I am
unable to use either for a front-end. Thus, I had to resort just to pure HTML.


### Files
There are three main files and a folder:
    <br>`flask_backend.py`: Contains the back-end to communicate between HTML and the SQL database
    <br>`sql_data.py`: Contains functionality for adding, updating, reading, and deleting data from the SQL database.
    <br>`scores.db`: Database file that stores data and is accessed by application during use
    <br>
    <br>`templates/`: Contains all HTML templates that are used and displayed on each respected page:
        <br>`home_screen.html`: Interface output for the home screen of the application
        <br>`add_data.html`: Interface and page for user to interact with when "Add a new user" button is selected
        <br>`update_data.html`: Interface and page for user to interact with when "Update existing user" button is selected
        <br>`display_data.html`: Interface and page for user to interact with when "Look up existing user" button is selected
        <br>`display_all_data.html`: Interface and page for user to interact with when "Display all users" button is selected
        <br>`delete_data.html`: Interface and page for user to interact with when "Delete existing user" button is selected
        <br>`delete_all_data.html`: Interface and page for user to interact with when "Delete ALL users" button is selected


### Assumptions
A `requirements.txt` is provided and is run by the `crud_app.sh` executable. A virtual environment is not needed, but recommended.
Now, you can clone the repo into a directory. Then proceed to the `Running the application` section in this `README.md`.


### Running the application
After cloning the repo, navigate to the folder; you should see a file called `crud_app.sh`. 
Enter the following command to run the application: `./crud_app.sh`

This will install the necessary dependencies to run the application. Then, navigate to the `src/` folder and run the following command:
<br>`python3 flask_backend.py`
This will start flask and the application, giving you an address to enter into your browser to view the website.
The address should be: `http://127.0.0.1:5000/`; however, given the unpredicatbility of computers, it may be different
for some odd reason, so check the output, specifically where it says `"Running on...."` to see the address. Open that link.

*NOTE: If the `crud_app.sh` does not work, and you are unable to launch the application, try running `./crud_app_backup.sh`.
This executable will create an environment, install Flask and necessary dependencies, and run the application. This executable
has only been tested on Linux systems*

Then, proceed to the `Using the application` section in this `README.md`.


### Using the application
To navigate the page, click the buttons, and when you're finished with that function, use the browser's
back-button to go back to the homepage. 

*NOTE* The text fields in this program are CASE SENSITIVE; data entered into the table must be entered in the same case 
sensitivity throughout the application.

On the homepage, there will be 6 buttons stacked in a column, describing their functionality.
    <br>`Add a new user`: Brings to a page to enter new username, id, and score. "Add Data" button will add data into SQL table
    <br>`Updating existing user`: Brings to a page to select the user to update and then gives boxes to input new usename, id, and score.
        "Update" button will send new data into SQL table
    <br>`Look up existing user`: Brings to a page requesting user's name, then displays data if user exists in database
    <br>`Display all data`: Brings to a page for the user to select a "Display" button and display all data in the database
    <br>`Delete existing user`: Brings to a page to enter new username, id, and score. "Delete" button will delete data from SQL table
    <br>`Delete ALL data`: Brings to a page verifying that the user wants to delete all data from the data base. 

*NOTE* If you want to stop the program, use `Ctrl+C` to end the application and not `Ctrl+Z`. `Ctrl+Z` seems to not allow the program to 
run correctly if you were to relaunch the server and run the application again. If you do hit `Ctrl+Z` to stop the program, the solution 
that works for me is to close the terminal and relaunch a new one, navigate to the folder, and run the executable again.
