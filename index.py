from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def handle_request():
    # Assuming the incoming request data is in JSON format
    received_data = request.json

    if not received_data:
        return jsonify({"error": "Invalid JSON data"}), 400

    # Process the data as needed
    # For this example, we'll simply log the received data
    print("Received JSON data:", received_data)

    # Prepare a response
    response = {"message": "JSON data received successfully"}

    return jsonify(response)

if __name__ == '__main__':
    # Replace '0.0.0.0' with your desired IP address and '3000' with your desired port number
    app.run(host='0.0.0.0', port=3000)
