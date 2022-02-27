#from msilib.schema import tables
import sqlite3

### Scores is the table name
### Creates a .db file with the following name if the file doesn't exist
### Otherwise, it just connects to the file
# conn = sqlite3.connect('scores.db')

# c = conn.cursor()

### -------------------------
### Insert data method
### -------------------------
def insert_data(connection, cursor, name, id, score):
    cursor.execute("INSERT INTO scores VALUES (:name, :id, :score)", {'name': name, 'id': id, 'score': score})
    connection.commit()

    connection.close

### -------------------------
### Remove data method
### -------------------------
def remove_data(connection, cursor, name, id, score):
    cursor.execute("DELETE FROM scores WHERE name=:name AND id=:id AND score=:score", {'name': name, 'id': id, 'score': score})
    connection.commit()
    #print("Total number of rows deleted: ", conn.total_changes)
    connection.close

### -------------------------
### Remove all data method
### -------------------------
def remove_all_data(connection, cursor):
    cursor.execute("DELETE FROM scores")
    connection.commit()
    print("Total number of rows deleted: ", connection.total_changes)

    connection.close

### -------------------------
### Update data method
### -------------------------
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

### -------------------------
### Read data method
### -------------------------
def read_data(connection, selected_name):
    table = connection.execute("SELECT * from scores")

    for record in table:
        if (record[0] == selected_name):
            return_string = record[0] + "<br>ID: " + str(record[1]) + "<br>Score: " + str(record[2])
            connection.close
            return return_string

### -------------------------
### Read All data method
### -------------------------
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










# def create_table():

#     ### This creates a table
#     ### If it already exists, it will throw an error
#     c.execute("""CREATE TABLE scores (
#             name text,
#             id integer,
#             score integer
#         )""")



### Inserts data
#c.execute("INSERT INTO scores VALUES ('Steve Smith', 211, 80)")
#c.execute("INSERT INTO scores VALUES ('Jian Wong', 122, 92)")

### Deletes all instances with the given condition
#c.execute("DELETE FROM scores WHERE name='Steve Smith'")

### The first and second line are needed for the second line to work
#c.execute("SELECT * FROM scores WHERE name='Steve Smith'")
#print(c.fetchone())

### Other ways to get data like from the line above
#print(c.fetchmany())
#print(c.fetchall())


