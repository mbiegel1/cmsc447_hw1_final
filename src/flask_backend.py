# importing Flask and other modules
from multiprocessing import connection
import sqlite3
import sql_data
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("scores.db")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/', methods =["GET", "POST"])
def home_screen():
    return render_template("home_screen.html")



@app.route('/add', methods =["GET", "POST"])
def add_user_data():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
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
            sql_data.insert_data(connection=conn, cursor=cursor, name=user_name, id=user_id, score=user_score)
            return "Data added to database!"

    return render_template("add_data.html")



@app.route('/update', methods =["GET", "POST"])
def update_user_data():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        user_name = request.form.get("uname")
        new_name = request.form.get("nname")
        user_id = request.form.get("uid")
        user_score = request.form.get("uscore")

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
        #elif ():

        else:
            sql_data.update_data(connection= conn, cursor=cursor, selected_name=user_name, new_name=new_name, new_id=user_id, new_score=user_score)
            return "Done"


    return render_template("update_data.html")



# A decorator used to tell the application
# which URL is associated function
@app.route('/display', methods =["GET", "POST"])
def display_user_data():
    conn = db_connection()

    if request.method == "POST":
        # getting input with name = fname in HTML form
        user_name = request.form.get("uname")

        retrieved_name = sql_data.read_data(connection=conn, selected_name=user_name)

        if (retrieved_name is None):
            retrieved_name = "ERROR: User not in list"
            return retrieved_name

        return retrieved_name
    return render_template("display_data.html")



@app.route('/display_all', methods =["GET", "POST"])
def display_all_data():
    conn = db_connection()

    if request.method == "POST":
        all_data = sql_data.read_all_data(connection=conn)

        return all_data
    return render_template("display_all_data.html")



@app.route('/delete', methods =["GET", "POST"])
def delete_user_data():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        # getting input with name = fname in HTML form
        user_name = request.form.get("uname")
        user_id = request.form.get("uid")
        user_score = request.form.get("uscore")

        try:                
            user_id = int(user_id)
            user_score = int(user_score)
        except:
            return "Invalid input for user's id or user's score. Please enter an integer."


        retrieved_name = sql_data.read_data(connection=conn, selected_name=user_name)

        if (retrieved_name is None):
            retrieved_name = "ERROR: User not in list"
            return retrieved_name
        else:
            sql_data.remove_data(connection=conn, cursor=cursor, name=user_name, id=user_id, score=user_score)
            completed = str(user_name) + " deleted"
            return completed

    return render_template("delete_data.html")


@app.route('/delete_all', methods =["GET", "POST"])
def delete_all_data():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        sql_data.remove_all_data(connection=conn, cursor=cursor)
        return "All data deleted"

    return render_template("delete_all_data.html")


if __name__=='__main__':
    app.run(debug=True)
