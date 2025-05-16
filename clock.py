import streamlit as st
from datetime import datetime
import requests
import pytz
from streamlit_autorefresh import st_autorefresh

def live_clock():
    st_autorefresh(interval=60000, key="clock_refresh")

    now = datetime.now(pytz.timezone("Asia/Karachi"))
    time_str = now.strftime("%I:%M %p")

    hijri_date = "Hijri date unavailable"
    try:
        response = requests.get(f"https://api.aladhan.com/v1/gToH?date={now.day}-{now.month}-{now.year}")
        if response.status_code == 200:
            data = response.json()["data"]["hijri"]
            hijri_date = f"{data['day']} {data['month']['en']} {data['year']}"
    except:
        pass

    st.markdown("""
        <style>
        .holographic-title {
            font-size: 32px;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 30px;
            font-weight: bold;
            background: linear-gradient(90deg, #ff9a9e, #fad0c4, #fad0c4, #fbc2eb, #a18cd1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
            font-family: 'Trebuchet MS', sans-serif;
        }
        .card3d {
            background: #e0e0e0;
            border-radius: 20px;
            box-shadow: 8px 8px 15px #bebebe, -8px -8px 15px #ffffff;
            padding: 25px;
            text-align: center;
            font-family: 'Courier New', monospace;
            margin: 20px auto;
            max-width: 300px;
        }
        .clock-text {
            font-size: 36px;
            color: #2C5364;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="holographic-title">
            ✨ Welcome to the App – May your spiritual journey be filled with light ✨
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="card3d">
            <div class="clock-text">{time_str}</div>
        </div>
        <div class="card3d">
            <div class="clock-text">{hijri_date}</div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Refresh"):
        st.rerun()
