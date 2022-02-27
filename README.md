# cmsc447_hw1_final


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
    <br>`\nsql_data.py`: Contains functionality for adding, updating, reading, and deleting data from the SQL database.
    <br>`\nscores.db`: Database file that stores data and is accessed by application during use
    <br>`\ntemplates`: Contains all HTML templates that are used and displayed on each respected page:
        <br>`home_screen.html`: Interface output for the home screen of the application
        <br>`add_data.html`: Interface and page for user to interact with when "Add a new user" button is selected
        <br>`update_data.html`: Interface and page for user to interact with when "Update existing user" button is selected
        <br>`display_data.html`: Interface and page for user to interact with when "Look up existing user" button is selected
        <br>`display_all_data.html`: Interface and page for user to interact with when "Display all users" button is selected
        <br>`delete_data.html`: Interface and page for user to interact with when "Delete existing user" button is selected
        <br>`delete_all_data.html`: Interface and page for user to interact with when "Delete ALL users" button is selected


### Assumptions
This program assumes you are currently in a virtual environment with flask installed
If you need to create a virtual environment, follow these steps at this link: 
    `https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/`

Once you have installed and have activated the virtual environment, install flask with: pip3 install Flask
Then proceed to `Running the application`


### Running the application
Launch the python file to start the sever by entering the following command from within the src/ folder:
    `python3 flask_backend.py`

This will start flask and the application, giving you an address to enter into your browser to view the website

### Using the application
