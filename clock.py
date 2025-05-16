# app.py
import streamlit as st
from datetime import datetime
import requests

def live_clock():
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    gregorian_date = now.strftime("%A, %d %B %Y")

    hijri_date = "Hijri date unavailable"
    try:
        url = f"https://api.aladhan.com/v1/gToH?date={now.day}-{now.month}-{now.year}"
        res = requests.get(url)
        if res.status_code == 200:
            hijri = res.json()["data"]["hijri"]
            hijri_day = hijri["day"]
            hijri_month = hijri["month"]["en"]
            hijri_year = hijri["year"]
            hijri_weekday = hijri["weekday"]["en"]
            hijri_date = f"{hijri_weekday}, {hijri_day} {hijri_month} {hijri_year}"
    except:
        pass

    # Auto-refresh workaround using Streamlit rerun button (manual)
    st.info("This page refreshes manually. To see current time, click the 'Refresh Clock' button below.")

    # Display results
    st.subheader("🕒 Current Time")
    st.write(time_str)

    st.subheader("📅 Gregorian Date")
    st.write(gregorian_date)

    st.subheader("🕌 Hijri Date")
    st.write(hijri_date)

    # Manual refresh button
    if st.button("🔄 Refresh Clock"):
        st.rerun()
