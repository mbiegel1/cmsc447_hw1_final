# Scores is the table name
# scores.db is the database file name

import sqlite3

### ------------------------------------------------------------------
### Insert data method
### Inserts new data in to the table with name, id, and score
### ------------------------------------------------------------------
def insert_data(connection, cursor, name, id, score):
    cursor.execute("INSERT INTO scores VALUES (:name, :id, :score)", {'name': name, 'id': id, 'score': score})
    connection.commit()

    connection.close

### ------------------------------------------------------------------
### Remove data method
### Removes data from table based on user's selected name, id, and score
### ------------------------------------------------------------------
def remove_data(connection, cursor, name, id, score):
    cursor.execute("DELETE FROM scores WHERE name=:name AND id=:id AND score=:score", {'name': name, 'id': id, 'score': score})
    connection.commit()
    #print("Total number of rows deleted: ", conn.total_changes)
    connection.close

### ------------------------------------------------------------------
### Remove all data method
### Removes all data from the data table
### ------------------------------------------------------------------
def remove_all_data(connection, cursor):
    cursor.execute("DELETE FROM scores")
    connection.commit()
    print("Total number of rows deleted: ", connection.total_changes)

    connection.close

### ------------------------------------------------------------------
### Update data method
### Updates username, id, and/or score based on the selected name
### ------------------------------------------------------------------
def update_data(connection, cursor, selected_name, new_name="", new_id=-1, new_score=-1):

    if (new_name != ""):
        print("Updating name...")
        cursor.execute("UPDATE scores SET name=:new_name WHERE name=:selected_name", {'selected_name': selected_name, 'new_name': new_name})
        selected_name = new_name

    if (new_id != -1):
        print("Updating id...")
        cursor.execute("UPDATE scores SET id=:new_id WHERE name=:selected_name", {'selected_name': selected_name, 'new_id': new_id})


    if (new_score != -1):
        print("Updating score...")
        cursor.execute("UPDATE scores SET score=:new_score WHERE name=:selected_name", {'selected_name': selected_name, 'new_score': new_score})

    connection.commit()
    connection.close

### ------------------------------------------------------------------  
### Read data method
### Reads a single piece of data entry specified by user using "username"
### ------------------------------------------------------------------  
def read_data(connection, selected_name):
    table = connection.execute("SELECT * from scores")

    for record in table:
        if (record[0] == selected_name):
            return_string = record[0] + "<br>ID: " + str(record[1]) + "<br>Score: " + str(record[2])
            connection.close
            return return_string

### ------------------------------------------------------------------  
### Read All data method
### Displays all data in the tabel
### ------------------------------------------------------------------  
def read_all_data(connection):
    table = connection.execute("SELECT * from scores")
    printing_data = ""

    for record in table:
        print(record[0], " ID = ",record[1] ,"|  Score = ",record[2])

        # Uses the <br> tag so that when HTML prints it, it prints a newline
        # HTML's \n = <br>
        printing_data += str(record[0]) + "<br>ID = " + str(record[1]) + "<br>Score = " + str(record[2])
        printing_data += "<br><br>"

    connection.close
    return printing_data