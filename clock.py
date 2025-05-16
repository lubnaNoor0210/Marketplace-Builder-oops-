import streamlit as st
from datetime import datetime
import requests

def live_clock():
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")  # Hour:Minute AM/PM
    gregorian_date = now.strftime("%A, %d %B %Y")

    # Fetch Hijri date using Aladhan API
    hijri_date = "Fetching Hijri date..."
    try:
        response = requests.get(f"https://api.aladhan.com/v1/gToH?date={now.day}-{now.month}-{now.year}")
        if response.status_code == 200:
            hijri_date = response.json()["data"]["hijri"]["date"]
        else:
            hijri_date = "Hijri date unavailable"
    except:
        hijri_date = "Hijri date unavailable"

    # Auto-refresh every 60 seconds
    st.markdown("<meta http-equiv='refresh' content='60'>", unsafe_allow_html=True)

    # Styled output
    st.markdown(f"""
        <div style='
            background-color: #ffffff;
            border: 2px solid #C9EBCB;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            font-family: Courier, monospace;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);'>

            <div style='font-size: 38px; color: #2C5364;'>🕒 {time_str}</div>
            <div style='font-size: 20px; margin-top: 10px;'>📅 {gregorian_date}</div>
            <div style='font-size: 18px; margin-top: 5px;'>🕌 Hijri: {hijri_date}</div>
        </div>
    """, unsafe_allow_html=True)
