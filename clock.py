import streamlit as st
from datetime import datetime
import requests

def live_clock():
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%A, %d %B %Y")

    hijri_date = "Fetching..."
    try:
        response = requests.get(f"https://api.aladhan.com/v1/gToH?date={now.day}-{now.month}-{now.year}")
        if response.status_code == 200:
            hijri_date = response.json()["data"]["hijri"]["date"]
    except:
        hijri_date = "Hijri date unavailable"

    st.markdown("""
        <meta http-equiv="refresh" content="60">
        <style>
        .clock-box {
            background: #f9f9f9;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-family: 'Courier New', monospace;
        }
        .clock-time {
            font-size: 40px;
            color: #2C5364;
        }
        .clock-date, .clock-hijri {
            font-size: 20px;
            color: #444;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='clock-box'>
            <div class='clock-time'>{time_str}</div>
            <div class='clock-date'>📅 {date_str}</div>
            <div class='clock-hijri'>🕌 Hijri: {hijri_date}</div>
        </div>
    """, unsafe_allow_html=True)
