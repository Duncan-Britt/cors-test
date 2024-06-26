from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

@app.route('/api/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    message = f'Hello, {name}!'
    return jsonify({'message': message})

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    # Process the received data
    processed_data = process_data(data)
    return jsonify({'processed_data': processed_data})

def process_data(data):
    # Apply upper() to all string values in the dictionary
    processed_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            processed_data[key] = value.upper()
        else:
            processed_data[key] = value
    return processed_data

if __name__ == '__main__':
    app.run()
