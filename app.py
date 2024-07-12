from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv 
import os 

load_dotenv() 

app = Flask(__name__)

client = MongoClient(host='mongodb',
                        port=27017, 
                        username=os.getenv("MONGO_USERNAME"), 
                        password=os.getenv("MONGO_PASSWORD"),
                    authSource="admin")
db = client["userData"]

@app.route('/')
def ping_server():
    return "API connection working."

@app.route('/publishUserPreferenceToTable', methods = ["POST"]) #for now must include cookie and preference label
def publish_user_preference():
    data = request.get_json()
    if not data or "cookie" not in data:
        return jsonify({"error": "Invalid data or no cookie associated with this user."}), 400
    result = db.preference_tb.insert_one({
        "cookie" : data["cookie"],
        "preference" : data["preference"]
    })
    return jsonify({"message": "User preference published successfully.", "inserted_id": str(result.inserted_id)}), 201

@app.route('/getAllPreferences', methods = ["GET"])
def get_stored_preferences():
    _userPreferenceData = db.preference_tb.find()
    userPreferenceData = [{"id": data["id"], "name": data["name"], "type": data["type"]} for data in _userPreferenceData]
    return jsonify({"preferences": userPreferenceData})

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

# #sample data:     {
#         "id": 5,
#         "cookie": "test_user",
#         "type": "domestic"
#     }