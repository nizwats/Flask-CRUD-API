Flask CRUD API

A lightweight RESTful API built using Flask that performs basic Create, Read, Update, and Delete (CRUD) operations on a simple data model.

🚀 Features

Create new items

Read (single or all) items

Update existing items

Delete items

JSON-based communication

🧱 Tech Stack

Python 3.12

Flask

📂 Project Structure

flask_crud_api/
├── app.py               # Main Flask app
├── requirements.txt     # Dependencies
├── .gitignore           # Ignored files
└── README.md            # Project documentation

🔧 Setup Instructions

1. Clone the Repository

git clone https://github.com/nizwats/Flask-CRUD-API.git
cd Flask-CRUD-API

2. Create and Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Flask App

python app.py

Flask will start running on http://127.0.0.1:5000/

🧪 Example API Requests

You can use curl or Postman to test the endpoints.

Create an Item (POST)

curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"name": "Example"}'

Get All Items (GET)

curl http://127.0.0.1:5000/items

Get Single Item (GET)

curl http://127.0.0.1:5000/items/1

Update an Item (PUT)

curl -X PUT http://127.0.0.1:5000/items/1 -H "Content-Type: application/json" -d '{"name": "Updated Name"}'

Delete an Item (DELETE)

curl -X DELETE http://127.0.0.1:5000/items/1

