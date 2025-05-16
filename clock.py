import streamlit as st
from datetime import datetime
import requests
import pytz
from streamlit_autorefresh import st_autorefresh

def live_clock():
    st_autorefresh(interval=60000, key="clock_refresh")

    # Get time in Pakistan timezone
    now = datetime.now(pytz.timezone("Asia/Karachi"))
    time_str = now.strftime("%I:%M %p")

    # Get Hijri date
    hijri_date = "Hijri date unavailable"
    try:
        response = requests.get(f"https://api.aladhan.com/v1/gToH?date={now.day}-{now.month}-{now.year}")
        if response.status_code == 200:
            data = response.json()["data"]["hijri"]
            hijri_date = f"{data['day']} {data['month']['en']} {data['year']}"
    except:
        pass

    # Inject 3D-style CSS
    st.markdown("""
        <style>
        .card3d {
            background: #e0e0e0;
            border-radius: 20px;
            box-shadow: 8px 8px 15px #bebebe, -8px -8px 15px #ffffff;
            padding: 30px;
            text-align: center;
            font-family: 'Courier New', monospace;
            margin-top: 30px;
        }
        .clock-text {
            font-size: 42px;
            color: #2C5364;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # Display Time and Hijri Date in 3D cards
    st.markdown(f"""
        <div class="card3d">
            <div class="clock-text">{time_str}</div>
        </div>
        <div class="card3d">
            <div class="clock-text">{hijri_date}</div>
        </div>
    """, unsafe_allow_html=True)

    # Manual refresh
    if st.button("🔄 Refresh"):
        st.rerun()
