from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import pyrebase

config = {
    "apiKey": "AIzaSyAYmY8jhzekHRySq-rDGJeaDtqC7QP6t9M",
    "authDomain": "gym-journal-5b64d.firebaseapp.com",
    "databaseURL": "https://gym-journal-5b64d.firebaseio.com",
    "projectId": "gym-journal-5b64d",
    "storageBucket": "",
    "messagingSenderId": "978352276575"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("nishant15066@iiitd.ac.in", "Sanskriti0304")



def test(request):
    # db = firebase.database()
    # lana = {"name": "Lana Kane", "agency": "Figgis Agency"}
    # db.child("agents").child("Lana").set(lana, user['idToken'])
    # all_agents = db.child("agents").get(user['idToken']).val() #You can get all of the values of an object
    # lana_data = db.child("agents").child("Lana").get(user['idToken']).val() #all_agents = db.child("agents").get(user['idToken']).val()
    # db.child("agents").child("Lana").update({"name": "Lana Anthony Kane"}, user['idToken']) #Updates can be made with the update() method.
    # db.child("agents").remove(user['idToken']) #The remove() method removes objects from the database.
    # db.child("agents").child("Lana").remove(user['idToken']) #Or a specific value from an object
    # dic = {'message_sent': False, 'error': False, }
    # if request.method != 'POST':
    #     return render(request, 'index.html', dic)
    #
    # name = request.POST['name']
    # email = request.POST['email']
    # message = request.POST['message']
    # write_to_database(name, email, message)

    return render(request, 'journal/createEntry.html')

# def write_to_database( name, email, message ):
    # db = firebase.database()
    # entry = {"name": name, "email": email, "message": message }
    # db.child("customer").child("customer 1").set(entry, user['idToken'])
    # all_agents = db.child("agents").get(user['idToken']).val() #You can get all of the values of an object
    # lana_data = db.child("agents").child("Lana").get(user['idToken']).val() #all_agents = db.child("agents").get(user['idToken']).val()
    # db.child("agents").child("Lana").update({"name": "Lana Anthony Kane"}, user['idToken']) #Updates can be made with the update() method.
    # db.child("agents").remove(user['idToken']) #The remove() method removes objects from the database.
    # db.child("agents").child("Lana").remove(user['idToken']) #Or a specific value from an object