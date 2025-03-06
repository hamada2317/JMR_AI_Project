from flask import Flask, request, jsonify

app = Flask(__name__)

# Store messages in a list (temporary storage)
messages = []

# Home route
@app.route('/', methods=['GET'])
def home():
    return "JMR Chat Server is running!"

# Route to get all messages
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})

# Route to send a new message
@app.route('/send', methods=['POST'])
def send_message():
    data = request.form.get("message")  # Get message from POST request
    if data:
        messages.append(data)  # Store message in the list
        return jsonify({"status": "Message received", "message": data})
    else:
        return jsonify({"error": "No message provided"}), 400

# Route to get chat info (optional)
@app.route('/chat', methods=['GET'])
def chat():
    return jsonify({"info": "This is JMR Chat Server!"})

# Run the Flask app
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
