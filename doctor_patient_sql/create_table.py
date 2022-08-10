import sqlite3
# Connect to the database
connection = sqlite3.connect('patients.db')
#Create a cursor
cursor = connection.cursor()
#Create a Table
cursor.execute("""CREATE TABLE registrations (
    uid integer,
    first_name text,
    last_name text,
    age integer,
    gender text
)""")

cursor.execute("""INSERT INTO registrations VALUES (
    345612,
    'John',
    'Doe',
    20,
    'female'
)""")

many_patients = [
    (345617,'Mark','Doe',20,'Male'),
    (465738,'Bob','Ross',45,'Male'),
    (981123,'Trevor','Jules',30,'Trans-Male')
]
cursor.executemany("INSERT INTO registrations VALUES (?,?,?,?,?)",many_patients)