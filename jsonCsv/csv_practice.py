import csv

csv_columns = ["UID", "first_name", "last_name", "gender", "age"]

# Read file using DictReader()
def read_csv_dict():
    patients = []
    patient_file = open("patient_record.csv", "r")
    patient_record = csv.DictReader(patient_file)
    for item in patient_record:
        patients.append(item)
    return patients

# Read using csv reader
def read_csv():
    with open('patient_record.csv') as csv_file:
        csv_data = csv.reader(csv_file)
        for s in csv_data:
            print(s)

def write_to_csv(uid,fname,lname,age,gender):
    new_patient = {
        "UID" : uid,
        "first_name" : fname,
        "last_name" : lname,
        "gender" : gender,
        "age" : age
    }
    patients = read_csv_dict()
    patients.append(new_patient)
    csv_file = open("patient_record.csv", "w")
    csv_data = csv.DictWriter(csv_file, csv_columns)
    csv_data.writeheader()
    for item in patients:
        csv_data.writerow(item)
    print(f"--Registered Patient ID {uid}--")

print("--CSV patient registration--")
print("--Registered Patients--")
patients=read_csv_dict()
print(patients)
write_to_csv(3,"Mary","Cooper",32,"Female")
write_to_csv(4,"George","Cooper",13,"Male")
print("--Registered Patients--")
read_csv()

