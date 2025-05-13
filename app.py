from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
# Use PostgreSQL if DATABASE_URL exists (e.g., on Heroku), otherwise default to local SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///instance/users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM instance
db = SQLAlchemy(app)

# Define the User database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(80), nullable=False)  # User name
    email = db.Column(db.String(120), unique=True, nullable=False)  # User email, must be unique

    # Convert object data to a dictionary
    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

# Home route for sanity check
@app.route("/")
def home():
    return "Flask CRUD API is running!"

# Create a new user (POST)
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email required"}), 400

    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# Retrieve all users (GET)
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Update a user by ID (PUT)
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()

    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)

    db.session.commit()
    return jsonify(user.to_dict())

# Delete a user by ID (DELETE)
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})

# Run the app locally
if __name__ == "__main__":
    app.run(debug=True)

