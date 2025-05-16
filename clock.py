import streamlit as st
from datetime import datetime

def live_clock():
    now = datetime.now()
    time_str = now.strftime("%I:%M:%S %p")
    date_str = now.strftime("%A, %d %B %Y")

    st.markdown("""
        <meta http-equiv="refresh" content="10">
        <style>
        .clock-box {
            background: linear-gradient(145deg, #f5f0da, #e8dfc4);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 6px 6px 12px #bfb8a8, -6px -6px 12px #ffffff;
            text-align: center;
            font-family: 'Courier New', monospace;
        }
        .clock-time {
            font-size: 48px;
            color: #2C5364;
        }
        .clock-date {
            font-size: 24px;
            color: #203A43;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class='clock-box'>
            <div class='clock-time'>{time_str}</div>
            <div class='clock-date'>{date_str}</div>
        </div>
    """, unsafe_allow_html=True)
