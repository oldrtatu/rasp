import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from playsound import playsound
import time
import schedule

db_url = 'https://smartalarmclock-7f74a.firebaseio.com/'


# Fetch the service account key JSON file contents
cred = credentials.Certificate(
    './smartalarmclock-7f74a-firebase-adminsdk-2gitw-e60d381bca.json')


# Initialize the app with a service account, granting admin privileges
app = firebase_admin.initialize_app(cred, {
    'databaseURL': db_url
})


def display_data(text):
    pass


def play_sound(time):
    pass


def print_reminders():
    get_reminders()
    # print(reminders)


def get_reminders():
    userId = 'NZUtAQoQb2XfCU9Y09R7VJluZVy2'

    currentTime = time.time() * 1000

    allReminders = []

    ref = db.reference('reminders')

    all_reminders = ref.get()

    userReminders = all_reminders[userId]

    for key in userReminders:
        if currentTime >= userReminders[key]['alarm']:
            print("alarm set")
            print(time.ctime(userReminders[key]["alarm"] / 1000))
        else:
            print("there is going to be alarm soon")


def print_time():
    print(time.ctime(1608718800000/1000))


schedule.every(5).seconds.do(get_reminders)


while True:
    schedule.run_pending()
    time.sleep(1)
