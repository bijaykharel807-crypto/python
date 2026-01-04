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
terminal.execute("Select  name  from student") 
result = terminal.fetchall()
for i in result:
    print(i)



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
terminal.execute("Select * from student  ") 
result = terminal.fetchall()
print(type(result))


terminal.execute("Select * from student  ") 
result = terminal.fetchall()
print(i[0])  # sab id haro aauncha...



terminal.execute("Select * from student limit 2")
result = terminal.fetchall()
print(i)    #only two id,name,address will come



terminal.execute("Select name,id from student 2")
result = terminal.fetchall()
print(i)    #only two id,name will come not address





