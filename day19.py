
import mysql.connector

db = mysql.connector.connect(
    host="localhost", username="root", database="broadway_dec_3"
)
terminal = db.cursor()



terminal.execute("insert INTO student (name, address) VALUES ('Suman', 'Dang')"),
('Suman', 'Dang'),
('Ramesh', 'Kathmandu'),
('Rita', 'Pokhara'),
('Amit', 'Butwal'),
('Sita', 'Dang'),
('Bikash', 'Kathmandu'),
('Suman', 'Dang'),
('Ramesh', 'Kathmandu'),
('Anita', 'Lalitpur'),
('Kiran', 'Butwal'),
('Sita', 'Dang'),
('Bikash', 'Kathmandu'),
('Anita', 'Lalitpur'),
('Prakash', 'Biratnagar'),
('Rita', 'Pokhara'),
('Kiran', 'Butwal'),
('Suman', 'Dang'),
('Ramesh', 'Kathmandu'),
('Sita', 'Dang')

db.commit()

# CRUD
 # Reading data from database
terminal.execute("Select  name, address from student where address = 'Kathmandu'") 
result = terminal.fetchall()
for i in result:
    print(i)

# UPDATE `Student` SET `address` = 'Ghorahi' WHERE `Student`.`id` = 18


# Updating data in database
terminal.execute("Update Student set address = 'nepal', name='bj' where id=18")
db.commit()
