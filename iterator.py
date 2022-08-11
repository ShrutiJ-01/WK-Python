import json

path = "jsonCsv/patient_record.json"

def get_iterator():
    with open(path) as json_file:
        json_data = json.load(json_file)
        return iter(json_data["patients"])

def print_patients(p_itr):
    while True:
        try:
            print(next(p_itr))
        except StopIteration:
            break

print_patients(get_iterator())