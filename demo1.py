from firebase import firebase
firebase = firebase.FirebaseApplication('https://attendance-eaebe.firebaseio.com/')
result = firebase.put('/test val','value',600)
print (result)
