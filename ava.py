from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/t', methods=['GET'])
def print_payload():
    try:
        # Get the payload from the request parameters
        payload = request.args.get('p')

        if payload is not None:
            # Print the payload
            print("Received payload:", payload)
            return jsonify({"message": "Payload received successfully", "payload": payload})
        else:
            return jsonify({"error": "Payload not provided"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, ssl_context=('cert.pem', 'key.pem'))
