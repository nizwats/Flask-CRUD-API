from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# App setup
app = Flask(__name__)

# Use PostgreSQL on Heroku, else SQLite locally
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Root route for deployment check
@app.route("/")
def home():
    return "Flask CRUD API is running!"

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

# Create user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email required"}), 400
    try:
        user = User(name=data["name"], email=data["email"])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    db.session.commit()
    return jsonify(user.to_dict())

# Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})

