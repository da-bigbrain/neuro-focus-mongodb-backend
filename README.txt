to run: create a .env file with 
MONGO_USERNAME = "your_username"
MONGO_PASSWORD = "your_password"

run the command
sudo docker-compose build
sudo docker-compose up

to see entries: 
enter docker image with docker exec -it "ID"

when in root, type
mongosh
use admin
db.auth("myUserAdmin", passwordPrompt()) // or cleartext password
use userData
db.userPreference.find()
