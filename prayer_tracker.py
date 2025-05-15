from datetime import datetime
import streamlit as st
import firebase_admin
from firebase_admin import db

class PrayerJournal:
    def __init__(self):
        self.base_ref = db.reference("journals")

    def save_entry(self, user_id, date, prayers, dhikr):
        entry = {
            "day": datetime.now().strftime("%A"),
            "prayers": prayers,
            "dhikr": dhikr
        }
        self.base_ref.child(user_id).child(date).set(entry)

    def get_entry(self, user_id, date):
        entry = self.base_ref.child(user_id).child(date).get()
        return entry if entry else {"prayers": {}, "dhikr": ""}

    def get_last_entries(self, user_id, count=5):
        data = self.base_ref.child(user_id).get() or {}
        last_keys = sorted(data.keys(), reverse=True)[:count]
        return {k: data[k] for k in last_keys}
