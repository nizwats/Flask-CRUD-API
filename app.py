import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
App setup

app = Flask(name)
Use Heroku PostgreSQL or fallback to SQLite for local dev

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///users.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Initialize the database

db = SQLAlchemy(app)
Home route for test

@app.route("/")
def home():
return "Flask CRUD API is running!"
Database model

class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(80), nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)

def to_dict(self):
    return {"id": self.id, "name": self.name, "email": self.email}

Create User

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
Get All Users

@app.route("/users", methods=["GET"])
def get_users():
users = User.query.all()
return jsonify([user.to_dict() for user in users])
Update User

@app.route("/users/int:user_id", methods=["PUT"])
def update_user(user_id):
user = User.query.get(user_id)
if not user:
return jsonify({"error": "User not found"}), 404
data = request.get_json()
user.name = data.get("name", user.name)
user.email = data.get("email", user.email)
db.session.commit()
return jsonify(user.to_dict())
Delete User

@app.route("/users/int:user_id", methods=["DELETE"])
def delete_user(user_id):
user = User.query.get(user_id)
if not user:
return jsonify({"error": "User not found"}), 404
db.session.delete(user)
db.session.commit()
return jsonify({"message": "User deleted"})

if name == "main":
app.run(debug=True)
