import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyAqeepHymrN1x9WMnPYMugl2QON4vhezQ4",
    'authDomain': "deskmeter.firebaseapp.com",
    'projectId': "deskmeter",
    'storageBucket': "deskmeter.appspot.com",
    'messagingSenderId': "150976878297",
    'appId': "1:150976878297:web:5c76e73051de3597b410c8",
    'measurementId': "G-6J1LSYSZNH",
    "databaseURL": "https://deskmeter-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
storage = firebase.storage()
db = firebase.database()

# # sign in
# email = input("email : ")
# password = input("password : ")
# try:
#     auth.sign_in_with_email_and_password(email, password)
# except:
#     print("Wrong")

# # sign up
# email = input("email : ")
# password = input("password : ")
# try:
#     auth.create_user_with_email_and_password(email, password)
# except:
#     print("Email already exist")

# database
data = {
    'age': 40,
    'address': 'New york',
    'occupied': True,
    'name': 'mark'
}
# db.child('people').push(data)

# add data
# db.child('people').child('myownid').set(data)

# update
# db.child('people').child('myownid').update({'name': 'jane'})

# get all people
# people = db.child('people').get()
# for person in people.each():
#     x = person.val()
#     print(x['name'])
#     print(person.val())
#     print(person.key())
#     if person.val()['name'] == 'mark':
#         db.child('people').child(person.key()).update({'name': 'jane'})

# delete
# db.child('people').child('person').child('age').remove()

# read
people = db.child('people').order_by_child("name").equal_to("Jane").get()
# greater of equal to 30
people = db.child('people').order_by_child("age").start_at(30).get()
# between 25 and 30
people = db.child('people').order_by_child("age").start_at(25).end_at(30).get()
# people = db.child('people').get()
for person in people.each():
    print(person.val())
