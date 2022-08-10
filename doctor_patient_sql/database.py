import sqlite3

class DBoperations:

    cursor = None
    connection = None

    def __init__(self):
        self.get_cursor()

    def get_cursor(self):
        # Connect to the database
        self.connection = sqlite3.connect('patients.db')
        #Create a cursor
        self.cursor = self.connection.cursor()

    def display_all(self):
        self.cursor.execute("SELECT * FROM registrations")
        registered_patients = self.cursor.fetchall()

        for patient in registered_patients:
            print(patient)

        self.connection.commit()

    def add_patient(self,first_name,last_name,id,age,gender):
        self.cursor.execute("INSERT INTO registrations VALUES (?,?,?,?,?)",(id,first_name,last_name,age,gender))
        self.connection.commit()
        print(f'---Registered patient id {id}---')
        
    def delete_patient(self,id):
        self.cursor.execute("DELETE from registrations WHERE uid = (?)",(id,))
        self.connection.commit()
        print(f'---Deleted patient id {id}---')


    def update_patient(self,first_name,last_name,age,gender,id):
        self.cursor.execute("""UPDATE registrations SET first_name = ? ,
        last_name = ? ,
        age = ? ,
        gender = ?
        WHERE uid = ?""",(first_name,last_name,age,gender,id))
        self.connection.commit()
        print(f'---Updated patient id {id}---')
    
    def search_id(self,id):
        self.cursor.execute("SELECT * FROM registrations WHERE uid = ?",(id,))
        matches = self.cursor.fetchall()
        for item in matches:
            print(item)
        self.connection.commit()
    
    def close_connection(self):
        self.connection.close()


    

        
        




    







