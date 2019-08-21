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


firebase = pyrebase.initialize_app(config)
db = firebase.database()

all_macs = db.child("probes").get()
# print(all_macs)

macs = []
pattern = "94:65:2d:"

for user in all_macs.each():
    #print(user.key()) # Morty
    macs.append(user.key())
    if user.key()[:len(pattern)] == pattern:
    	print("{0}: {1}".format(user.key(), user.val()))
    # print(user.val()) #wc  {name": "Mortimer 'Morty' Smith"}

print(len(macs))

macs.sort()

# print(macs)