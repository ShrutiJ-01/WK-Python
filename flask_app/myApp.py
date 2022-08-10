#Simple API umad eusing flask and sqlite for patient registration

from flask import Flask, request, jsonify,make_response
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return 'Patient Registrations App'

@app.route('/registrations',methods = ["POST"])
def adding_patient():
    print("Inside adding_patient()")
    databaseOperations = database.DBoperations()
    request_data =  request.get_json()
    databaseOperations.add_patient(id = request_data["uid"], first_name = request_data["first_name"], last_name = request_data["last_name"], age = request_data["age"], gender = request_data["gender"])
    operation_status={
      'status' : "Sucess",
      'uid' : request_data["uid"]  
    }
    databaseOperations.close_connection()
    return make_response(jsonify(operation_status),200)

@app.route('/registrations',methods = ["GET"])
def getting_patients():
    print("Inside getting_patients()")
    databaseOperations = database.DBoperations()
    all_patients = databaseOperations.get_all_patients()
    operation_status={
      "patients" : all_patients
    }
    databaseOperations.close_connection()
    return make_response(jsonify(operation_status),200)


if __name__ == '__main__':
    app.run(debug=True)
