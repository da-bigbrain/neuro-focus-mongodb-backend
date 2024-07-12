
db = db.getSiblingDB("userData");
// db.preference_tb.drop();

db.preference_tb.insertMany([
    {
        "id": 1,
        "cookie": "test_user",
        "name": "ww",
        "type": "wild"
    },
    {
        "id": 5,
        "cookie": "test_user",
        "name": "daniel",
        "type": "domestic"
    },

]);