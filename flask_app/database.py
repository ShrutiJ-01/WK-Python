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

    def get_all_patients(self):
        patient_list=[]
        self.cursor.execute("SELECT * FROM registrations")
        fetched_results = self.cursor.fetchall()
        self.connection.commit()
        for patient in fetched_results:
            patient_obj = {
                "uid" : patient[0],
                "first_name" : patient[1],
                "last_name" : patient[2],
                "age" : patient[3],
                "gender" : patient[4]
            }
            patient_list.append(patient_obj)

        return patient_list
        

    def add_patient(self,first_name,last_name,id,age,gender):
        self.cursor.execute("INSERT INTO registrations VALUES (?,?,?,?,?)",(id,first_name,last_name,age,gender))
        self.connection.commit()
        print(f'---Registered patient id {id}---')
    
    def close_connection(self):
        self.connection.close()


    

        
        




    







