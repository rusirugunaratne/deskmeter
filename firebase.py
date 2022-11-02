import pyrebase


class Firebase:
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

    def firebase_update_time(self, worked_time, date):
        f = open('user.txt', 'r')
        email = f.read().split(' ')[2]
        worked_time_ref = self.db.child('people').child(email).child('worked_time')
        worked_time_collection = worked_time_ref.get()
        date_exists = False
        if worked_time_collection is not None:
            for value in worked_time_collection.each():
                if value.key() == date:
                    date_exists = True
                    existing_date_value = value.val()
                    new_date_value = existing_date_value + worked_time
                    print(f"new date value: {new_date_value}")
                    self.db.child('people').child(email).child('worked_time').update({date: new_date_value})
        if not date_exists:
            print('DATE NOT EXISTS')
            data = {date: worked_time}
            self.db.child('people').child(email).child('worked_time').update(data)


    def login_user(self, email, password):
        people = self.db.child('people').get()
        self.person_exists = False
        if people is not None:
            for person in people.each():
                if person.key() == email and person.val()['password'] == password:
                    first_name = person.val()['first_name']
                    last_name = person.val()['last_name']
                    f = open('user.txt', 'w')
                    f.write(f'{first_name} {last_name} {email}')
                    self.person_exists = True
        if self.person_exists:
            return True
        else:
            print('No user found')
            raise Exception('No such user')

    def add_user(self, first_name, last_name, email, username, password):
        people = self.db.child('people').get()
        self.person_exists = False
        if people is not None:
            for person in people.each():
                if person.key() == email:
                    self.person_exists = True
                    raise Exception('User Exists')
                    print('error')
                else:
                    print('success')
        if not self.person_exists:
            data = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'password': password
            }

            self.db.child('people').child(email).set(data)
            f = open('user.txt', 'w')
            f.write(f'{first_name} {last_name} {email}')
            return True

    def get_progress(self):
        dates = []
        values = []
        f = open('user.txt', 'r')
        email = f.read().split(' ')[2]
        worked_time_ref = self.db.child('people').child(email).child('worked_time')
        worked_time_collection = worked_time_ref.get()
        date_exists = False
        if worked_time_collection is not None:
            for value in worked_time_collection.each():
                dates.append(value.key())
            dates = sorted(dates)
            for date in dates:
                for value in worked_time_collection.each():
                    if value.key() == date:
                        values.append(value.val())

        return [dates, values]