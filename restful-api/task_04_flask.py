from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# /data endpoint: list of usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

# /status endpoint
@app.route("/status")
def status():
    return "OK"

# /users/<username> endpoint
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# /add_user endpoint for POST requests
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if JSON is valid
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check for username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

# Run the app
if __name__ == "__main__":
    app.run(port=5000)
