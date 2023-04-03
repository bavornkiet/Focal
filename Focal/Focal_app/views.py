from django.shortcuts import render
import pyrebase
import os

config = {
  "apiKey": "AIzaSyDdFmv64kAMrmhPcL9mpzlg91r8HlmSnGc",
  "authDomain": "focal-ebc94.firebaseapp.com",
  "databaseURL": "https://focal-ebc94-default-rtdb.firebaseio.com",
  "projectId": "focal-ebc94",
  "storageBucket": "focal-ebc94.appspot.com",
  "messagingSenderId": "1021011042147",
  "appId": "1:1021011042147:web:3c808011babd0967b43d56",
  "measurementId": "G-04DTRWS0SD"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

storage = firebase.storage()
storage.child(PATH/DIRECTORY_ON_CLOUD).put(PATH_TO_LOCAL_IMAGE)

# Example (same directory, same file name)
storage.child("images/example.jpg").put("example.jpg")

# Example (different directory, different file name)
storage.child("images/renamed_img.jpg").put("media/original_img.jpg")

def view_name(request):
    return render(request, 'template_name.html', {})
