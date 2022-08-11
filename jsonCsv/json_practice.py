import json

patient_file = open("patient_record.json", "r")
patient_record = json.load(patient_file)

def add_patient(uid,first_name,last_name,age,gender):
    new_patient = {
        "uid" : uid,
        "first_name" : first_name,
        "last_name" : last_name,
        "age" : age,
        "gender" : gender
    }
    patient_record["patients"].append(new_patient)
    with open("patient_record.json", "w") as updated_patient_file:
        json.dump(patient_record, updated_patient_file, indent=8)
        print(f"--Added UID {uid}--")
        updated_patient_file.close()

def display_data():
    print("--Patient Records--")
    for patient in patient_record["patients"]:
        print(patient)

def update_patient_name(uid, updated_name):
    for patient in patient_record["patients"]:
        if patient["uid"] == uid:
            patient["first_name"] = updated_name
            with open("patient_record.json", "w") as updated_patient_file:
                json.dump(patient_record, updated_patient_file, indent=8)
                print(f"--Updated UID {uid}--")
                updated_patient_file.close()
        else:
            print("--Record not found--")

print("--JSON patient registration--")
display_data()
add_patient(3,"Mary","Cooper",32,"Female")
add_patient(4,"George","Cooper",13,"Male")
display_data()
update_patient_name(4,"Georgie")
display_data()