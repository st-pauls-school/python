import pyrebase
import arrow 

config = {
  "apiKey": "AIzaSyAehYWh_RvsEXQMfpTfent-AXjgXftdLIk",
  "authDomain": "sps-monitor.firebaseapp.com",
  "databaseURL": "https://sps-monitor.firebaseio.com",
  "projectId": "sps-monitor",
  "storageBucket": "sps-monitor.appspot.com",
  "serviceAccount": "sps-monitor-firebase-adminsdk-av3qz-4aba12ef41.json",
  "messagingSenderId": "1020030044260"
}

#    appId: "1:1020030044260:web:410f3642080837ea"



firebase = pyrebase.initialize_app(config)
db = firebase.database()

location = "computer gallery"

new_event = {"utc" : arrow.utcnow().format('YYYY-MM-DD HH:mm:ss'), "mac_address" : "00:11:22:33:44:55", "ssid" : "abcd"}

db.child("events").child(location).push(new_event) 

# taking from the Pyrebase github instructions - https://github.com/thisbejim/Pyrebase 