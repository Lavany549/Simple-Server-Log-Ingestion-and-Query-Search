from flask import Flask, request
from flask_restful import Api, Resource
import csv

app = Flask(__name__)
api = Api(app)

class LogReceiver(Resource):
    # Receives data from the client
    def post(self):
        log_data = request.get_json()
        print("Received Log Data:")
        print(log_data)

        # Save log data to a CSV file
        save_bulk_to_csv(log_data)

        return {'status': 'success', 'message': 'Log received and saved to CSV successfully'}, 200

# Filters out each input and writes into logs.csv file
def save_to_csv(log_data):
    # CSV file path (assuming it's in the same folder as log_receiver.py)
    csv_file_path = 'logs.csv'

    # Write log data to CSV file
    with open(csv_file_path, mode='a', newline='') as csv_file:
        fieldnames = ["level", "message", "resourceId", "timestamp", "traceId", "spanId", "commit", "metadata.parentResourceId"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Check if the CSV file is empty and write header only if needed
        if csv_file.tell() == 0:
            writer.writeheader()

        # Write log data to CSV file
        writer.writerow({
            "level": log_data.get("level", ""),
            "message": log_data.get("message", ""),
            "resourceId": log_data.get("resourceId", ""),
            "timestamp": log_data.get("timestamp", ""),
            "traceId": log_data.get("traceId", ""),
            "spanId": log_data.get("spanId", ""),
            "commit": log_data.get("commit", ""),
            "metadata.parentResourceId": log_data.get("metadata", {}).get("parentResourceId", "")
        })

# Saves the bulk data into entries of logs.csv file
def save_bulk_to_csv(log_data_list):
    for log_data in log_data_list:
        save_to_csv(log_data)

api.add_resource(LogReceiver, '/')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
