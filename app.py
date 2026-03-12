from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["userdb"]
collection = db["users"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/save', methods=['POST'])
def save_user():

    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    user = {
        "name": name,
        "age": int(age)
    }

    collection.insert_one(user)

    return jsonify({"message": "User saved successfully!"})


if __name__ == '__main__':
    app.run(debug=True)