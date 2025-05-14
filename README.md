# Flask CRUD API

A RESTful API built with Flask and SQLAlchemy to perform Create, Read, Update, and Delete (CRUD) operations on user data. The application uses PostgreSQL for persistent storage and is deployed on Heroku.

## Features

- Create new users
- Retrieve all users
- Update existing users
- Delete users
- JSON-based input and output

## Tech Stack

- Python 3.12
- Flask
- SQLAlchemy
- PostgreSQL
- Heroku (Deployment)

## Project Structure

flask_crud_api/
├── app.py # Main application file
├── requirements.txt # Python dependencies
├── Procfile # Heroku deployment instruction
├── .gitignore # Files excluded from Git tracking
└── README.md # Project documentation


## Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/nizwats/Flask-CRUD-API.git
cd Flask-CRUD-API


2. Create and Activate a Virtual Environment

python3 -m venv venv
source venv/bin/activate


3. Install Dependencies

pip install -r requirements.txt


4. Run the Flask App Locally

python app.py

5. The application will run at: http://127.0.0.1:5000/

API Endpoints
Method	Endpoint	Description
POST	/users	Create a new user
GET	/users	Retrieve all users
PUT	/users/<id>	Update a user
DELETE	/users/<id>	Delete a user
Example Requests


6. Use curl or Postman to interact with the API.

Create a User (POST):
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john@example.com"}'


Get All Users (GET):
curl http://127.0.0.1:5000/users


Update a User (PUT):
curl -X PUT http://127.0.0.1:5000/users/1 \
-H "Content-Type: application/json" \
-d '{"name": "Updated Name", "email": "updated@example.com"}'


Delete a User (DELETE):
curl -X DELETE http://127.0.0.1:5000/users/1


7. Deployment
The app is deployed on Heroku and uses a Heroku Postgres add-on.

8. Live API URL:
https://nizwa-crud-api-05975b68cbc4.herokuapp.com/
