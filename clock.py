import streamlit as st
from datetime import datetime
import requests
from streamlit_autorefresh import st_autorefresh

def live_clock():
    # Refresh the tab every 60 seconds
    st_autorefresh(interval=60000, key="clock_refresh")

    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    gregorian_date = now.strftime("%A, %d %B %Y")

    hijri_date = "Hijri date unavailable"
    try:
        response = requests.get(f"https://api.aladhan.com/v1/gToH?date={now.day}-{now.month}-{now.year}")
        if response.status_code == 200:
            data = response.json()["data"]["hijri"]
            hijri_date = f"{data['weekday']['en']}, {data['day']} {data['month']['en']} {data['year']}"
    except:
        pass

    st.subheader("🕒 Time")
    st.write(time_str)

    st.subheader("📅 Gregorian Date")
    st.write(gregorian_date)

    st.subheader("🕌 Hijri Date")
    st.write(hijri_date)

    if st.button("🔄 Refresh Clock"):
        st.rerun()
