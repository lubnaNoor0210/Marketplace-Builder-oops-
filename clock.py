import streamlit as st
from datetime import datetime
import requests
import pytz
from streamlit_autorefresh import st_autorefresh

def live_clock():
    # Optional: auto refresh every 60 seconds
    st_autorefresh(interval=60000, key="clock_refresh")

    # Time in Pakistan timezone
    now = datetime.now(pytz.timezone("Asia/Karachi"))
    time_str = now.strftime("%I:%M %p")

    hijri_date = "Hijri date unavailable"
    try:
        response = requests.get(f"https://api.aladhan.com/v1/gToH?date={now.day}-{now.month}-{now.year}")
        if response.status_code == 200:
            data = response.json()["data"]["hijri"]
            hijri_date = f"{data['day']} {data['month']['en']} {data['year']}"
    except Exception as e:
        hijri_date = f"Error: {e}"

    # Just show values, no headers
    st.write(time_str)
    st.write(hijri_date)

    # Optional refresh button
    st.button("🔄 Refresh", on_click=st.rerun)
