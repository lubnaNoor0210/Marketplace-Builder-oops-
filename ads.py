import streamlit as st
import time
from payment import PaymentProcessor

def show_timed_ad(tab_name=""):
    now = time.time()

    if "last_ad_dismissed" not in st.session_state or not isinstance(st.session_state["last_ad_dismissed"], dict):
        st.session_state["last_ad_dismissed"] = {}

    if tab_name not in st.session_state["last_ad_dismissed"]:
        st.session_state["last_ad_dismissed"][tab_name] = 0

    seconds_since_dismiss = now - st.session_state["last_ad_dismissed"][tab_name]

    if seconds_since_dismiss > 10:
        stripe_key = st.secrets["stripe"]["secret_key"]
        processor = PaymentProcessor(stripe_key)
        checkout_url = processor.create_checkout_session(10)  
        st.markdown(f"""
    <div style="background-color:#fff7e6; padding:10px 15px; border:2px solid #ffc107; border-radius:10px; max-width: 100%; margin: 10px auto;">
        <h5 style="margin: 5px 0;">🚨 Ad: Upgrade to Premium</h5>
        <p style="font-size: 14px; margin: 5px 0;">This is a free version. Buy Premium to remove ads permanently.</p>
        <a href='{checkout_url}' target='_blank'>
            <button style="background-color:#28a745; color:white; padding:6px 12px; font-size: 14px; border:none; border-radius:5px;">
                Buy Premium
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

        if st.button("Dismiss Ad", key=f"dismiss_btn_{tab_name}"):
            st.session_state["last_ad_dismissed"][tab_name] = now
