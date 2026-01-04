import mysql.connector

db = mysql.connector.connect(
    host="localhost", username="root", database="Nepaldata"
)
terminal = db.cursor()
# terminal.execute("Create Database Nepaldata")
terminal.execute("Show tables")
data = terminal.fetchall()
print(data)
# terminal.execute("Create table history (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(60), address VARCHAR(12))")

#TODO,Drop, database
db = mysql.connector.connect(
    host="localhost", username="root"
)
terminal = db.cursor()

# terminal.execute("Drop database Parent")