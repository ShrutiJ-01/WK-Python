import json

path = "jsonCsv/patient_record.json"
def patient_generator():
    json_file = open(path)
    json_data = json.load(json_file)
    for patient in json_data["patients"]:
        yield patient

for i in patient_generator():
    print(i)