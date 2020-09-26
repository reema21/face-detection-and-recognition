from firebase import firebase
import time
import datetime
import urllib.request
import urllib.error
import json
whattime = datetime.datetime.now()
firebase = firebase.FirebaseApplication('https://attendance-eaebe.firebaseio.com/',None)
result = firebase.put('/user',str(whattime),'testing')
