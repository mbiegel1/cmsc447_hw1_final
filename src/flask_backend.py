# Importing Flask, sqlite3, sql python file, and other modules
from multiprocessing import connection
import sqlite3
import sql_data
from flask import Flask, request, render_template
#--------------------------------------------------------------------


# Flask constructor for creating app
app = Flask(__name__)


### ------------------------------------------------------------------
### db_connection()
### Connects to existing database file to be accessed throughout program
### ------------------------------------------------------------------
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("scores.db")
    except sqlite3.error as e:
        print(e)
    return conn


### ------------------------------------------------------------------
### home_screen()
### Displays home screen template with 6 buttons for database fucntionality
### ------------------------------------------------------------------
@app.route('/', methods =["GET", "POST"])
def home_screen():
    return render_template("home_screen.html")


### ------------------------------------------------------------------
### add_user_data()
### Route for the "Add a new user" button
### ------------------------------------------------------------------
@app.route('/add', methods =["GET", "POST"])
def add_user_data():

    # Create connection to database file and make a cursor
    conn = db_connection()
    cursor = conn.cursor()

    # If the front-end sends information,
    if request.method == "POST":

        # Get the username, id, and score from front-end
        user_name = request.form.get("uname")
        user_id = request.form.get("uid")
        user_score = request.form.get("uscore")

        # Validates if the user enters integers for either id or score and if those
        #   entered values are integers
        try:                
            user_id = int(user_id)
            user_score = int(user_score)
        except:
            return "Invalid input for user's id or user's score. Please enter integers."

        # Dunno how to validate if the user enters a name here or keeps it blank
        # Leaving it blank returns NULL into the database, but python does not
        #   see this as being equal to None, so I don't know how to validate for this
        if (user_name == "enter_name_here"):
            return "Please enter a name for the user."
        else:
            # Enter data into the sql database
            sql_data.insert_data(connection=conn, cursor=cursor, name=user_name, id=user_id, score=user_score)
            return "Data added to database!"

    return render_template("add_data.html")


### ------------------------------------------------------------------
### update_user_data()
### Route for the "Update existing user" button
### ------------------------------------------------------------------
@app.route('/update', methods =["GET", "POST"])
def update_user_data():

    # Create connection to database file and make a cursor
    conn = db_connection()
    cursor = conn.cursor()

    # If the front-end sends information,
    if request.method == "POST":

        # Get the selected username, new username, new id, and new score from front-end
        user_name = request.form.get("uname")
        new_name = request.form.get("nname")
        user_id = request.form.get("uid")
        user_score = request.form.get("uscore")

        # Validates if the user enters integers for either id or score and if those
        #   entered values are integers
        try:                
            user_id = int(user_id)
            user_score = int(user_score)
        except:
            return "Invalid input for user's id or user's score. Please enter an integer."

        # Goes into the database to check and see if the user exists
        retrieved_name = sql_data.read_data(connection=conn, selected_name=user_name)

        # If the user doesn't exist, return an error
        if (retrieved_name is None):
            return "ERROR: Can't update a user that's not in list!"
        else:
            # Updates data in the sql database
            sql_data.update_data(connection= conn, cursor=cursor, selected_name=user_name, new_name=new_name, new_id=user_id, new_score=user_score)
            return "Done"

    return render_template("update_data.html")


### ------------------------------------------------------------------
### display_user_data()
### Route for the "Look up existing user" button
### ------------------------------------------------------------------
@app.route('/display', methods =["GET", "POST"])
def display_user_data():

    # Create connection to database file
    conn = db_connection()

    # If the front-end sends information,
    if request.method == "POST":
        
        # Get the username from front-end
        user_name = request.form.get("uname")

        # Goes into the database to check and reads the selected user
        retrieved_name = sql_data.read_data(connection=conn, selected_name=user_name)

        # If the user doesn't exist, return an error
        if (retrieved_name is None):
            retrieved_name = "ERROR: User not in list"
            return retrieved_name
        
        # Return the retrieved name to the front-end
        return retrieved_name

    return render_template("display_data.html")


### ------------------------------------------------------------------
### display_all_data()
### Route for the "Display all data" button
### ------------------------------------------------------------------
@app.route('/display_all', methods =["GET", "POST"])
def display_all_data():

    # Create connection to database file
    conn = db_connection()

    # If the front-end sends information,
    if request.method == "POST":

        # Get all the data from the database and put it in a string, formatted
        all_data = sql_data.read_all_data(connection=conn)

        # Return the string to the front-end
        return all_data

    return render_template("display_all_data.html")


### ------------------------------------------------------------------
### delete_user_data()
### Route for the "Delete existing user" button
### ------------------------------------------------------------------
@app.route('/delete', methods =["GET", "POST"])
def delete_user_data():

    # Create connection to database file and make a cursor
    conn = db_connection()
    cursor = conn.cursor()

    # If the front-end sends information,
    if request.method == "POST":

        # Get the specified username, id, and score from front-end
        user_name = request.form.get("uname")
        user_id = request.form.get("uid")
        user_score = request.form.get("uscore")

        # Validates if the user enters integers for either id or score and if those
        #   entered values are integers
        try:                
            user_id = int(user_id)
            user_score = int(user_score)
        except:
            return "Invalid input for user's id or user's score. Please enter an integer."

        # Goes into the database to check and see if the user exists
        retrieved_name = sql_data.read_data(connection=conn, selected_name=user_name)

        # If the user doesn't exist, return an error
        if (retrieved_name is None):
            return "ERROR: User not in list"
        else:
            # Deletes data in the sql database
            sql_data.remove_data(connection=conn, cursor=cursor, name=user_name, id=user_id, score=user_score)
            completed = str(user_name) + " deleted"
            return completed

    return render_template("delete_data.html")


### ------------------------------------------------------------------
### delete_all_data()
### Route for the "Delete ALL data" button
### ------------------------------------------------------------------
@app.route('/delete_all', methods =["GET", "POST"])
def delete_all_data():

    # Create connection to database file and make a cursor
    conn = db_connection()
    cursor = conn.cursor()

    # If the front-end sends information,
    if request.method == "POST":

        # Send the command to the database to remove all data
        sql_data.remove_all_data(connection=conn, cursor=cursor)
        return "All data deleted"

    return render_template("delete_all_data.html")


### Main - Launchs the flask app
if __name__=='__main__':
    # Runs application in debug mode; for development purposes only
    #app.run(debug=True)

    app.run()
