import database

dbOperations = database.DBoperations()

while True:
    print("Patient Database")
    print("1.Register new patient")
    print("2.Display all patients")
    print("3.Update Patient Data")    
    print("4.Delete a Patient")
    print("5.Lookup a Patient")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        #Register patient
        uid = input("Enter UID - ")
        firstname = input("Enter first name - ")
        lastname = input("Enter last name - ")
        gender = input("Enter gender - ")
        age = input("Enter age - ")
        dbOperations.add_patient(id = uid, first_name = firstname, last_name = lastname, age = age, gender = gender)        
    
    elif choice==2:
        print('---Registered Patients---')
        dbOperations.display_all()
    
    elif choice==3:
        uid = input("Enter UID of patient to update - ")
        print('Enter new data for {uid} ')
        firstname = input("Enter first name  - ")
        lastname = input("Enter last name - ")
        gender = input("Enter gender - ")
        age = input("Enter age - ")
        dbOperations.update_patient(id = uid, first_name = firstname, last_name = lastname, age = age, gender = gender)        

    elif choice==4:
        uid = input("Enter UID of patient to delete - ")
        dbOperations.delete_patient(f'{uid}')
    
    elif choice==5:
        uid = input("Enter UID of patient to lookup - ")
        dbOperations.search_id(f'{uid}')

    elif choice==6:
        dbOperations.close_connection()
        break

    else:
        print("Wrong Choice")

