import streamlit as st
from datetime import datetime
import requests
import pytz
from streamlit_autorefresh import st_autorefresh

def live_clock():
    st_autorefresh(interval=60000, key="clock_refresh")

    # Timezone-aware datetime for Pakistan
    pakistan_tz = pytz.timezone('Asia/Karachi')
    now = datetime.now(pakistan_tz)

    time_str = now.strftime("%I:%M %p")
    gregorian_date = now.strftime("%A, %d %B %Y")

    hijri_date = "Hijri date unavailable"
    try:
        response = requests.get(f"https://api.aladhan.com/v1/gToH?date={now.day}-{now.month}-{now.year}")
        if response.status_code == 200:
            data = response.json()["data"]["hijri"]
            hijri_date = f"{data['day']} {data['month']['en']} {data['year']}"
    except:
        pass

    # Custom 3D-style CSS
    st.markdown("""
        <style>
        .clock-card {
            background: linear-gradient(145deg, #f0f0f0, #cacaca);
            border-radius: 20px;
            box-shadow: 8px 8px 15px #bebebe, -8px -8px 15px #ffffff;
            padding: 25px;
            text-align: center;
            font-family: 'Courier New', monospace;
            margin: 20px 0;
        }
        .clock-time {
            font-size: 48px;
            color: #2C5364;
            font-weight: bold;
        }
        .clock-label {
            font-size: 18px;
            color: #444;
            margin-bottom: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Display 3D boxes
    st.markdown(f"""
        <div class="clock-card">
            <div class="clock-label">🕒 Current Time</div>
            <div class="clock-time">{time_str}</div>
        </div>
        <div class="clock-card">
            <div class="clock-label">📅 Gregorian Date</div>
            <div class="clock-time">{gregorian_date}</div>
        </div>
        <div class="clock-card">
            <div class="clock-label">🕌 Hijri Date</div>
            <div class="clock-time">{hijri_date}</div>
        </div>
    """, unsafe_allow_html=True)

    st.button("🔄 Refresh Clock", on_click=st.rerun)
