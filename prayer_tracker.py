import streamlit as st
from datetime import datetime
import pyrebase

class PrayerJournal:
    def __init__(self):
        firebase_config = {
            "apiKey": "AIzaSyCMprrKEi64KhuApnhze7ZpdAKP7DmYJxc",
    "authDomain": "quran-guide-9b941.firebaseapp.com",
    "databaseURL": "https://quran-guide-9b941-default-rtdb.firebaseio.com",  # <-- VERY IMPORTANT
    "projectId": "quran-guide-9b941",
    "storageBucket": "quran-guide-9b941.appspot.com",
    "messagingSenderId": "725958461341",
    "appId": "1:725958461341:web:c396f99963b498a06c9174"
        }
        self.firebase = pyrebase.initialize_app(firebase_config)
        self.db = self.firebase.database()

    def save_entry(self, user_id, date, prayers, dhikr):
        entry = {
            "day": datetime.now().strftime("%A"),
            "prayers": prayers,
            "dhikr": dhikr
        }
        self.db.child("journals").child(user_id).child(date).set(entry)

    def get_entry(self, user_id, date):
        entry = self.db.child("journals").child(user_id).child(date).get()
        return entry.val() if entry.val() else {"prayers": {}, "dhikr": ""}

    def get_last_entries(self, user_id, count=5):
        data = self.db.child("journals").child(user_id).get().val() or {}
        last_keys = sorted(data.keys(), reverse=True)[:count]
        return {k: data[k] for k in last_keys}
