import streamlit as st
import json
from ads import show_timed_ad
import firebase_admin
from Hadith import HadithCollection
from firebase_admin import credentials, auth
from payment import PaymentProcessor
import requests
from datetime import datetime
from calender_converter import CalendarConverter
from emotional_quote import QuranQuoteGenerator
from prayer_tracker import PrayerJournal
from auth import AuthManager
st.set_page_config(page_title="Quran Guide", layout="wide")

if not firebase_admin._apps:
    firebase_config = json.loads(st.secrets["firebase"])
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

query_params = st.query_params
if query_params.get("status") == "success":
    st.success("✅ Payment Successful! Thank you for your support.")
elif query_params.get("status") == "cancel":
    st.warning("❌ Payment was cancelled.")

firebase_token = query_params.get("token")

if firebase_token and "user" not in st.session_state:
    try:
        decoded_token = auth.verify_id_token(firebase_token)
        email = decoded_token.get("email", "")

        try:
            auth.get_user_by_email(email)  
        except firebase_admin.auth.UserNotFoundError:
            st.warning("🚫 This account is not registered. Please sign up first.")
            st.stop()

        st.session_state["user"] = {
            "email": email,
            "name": decoded_token.get("name", ""),
            "localId": decoded_token.get("uid", "")
        }
        st.success(f"✅ Logged in as {email}")

    except Exception as e:
        st.error("❌ Invalid or expired login token.")
if "redirect_tab" in st.session_state:
    st.markdown(f"<script>window.location.hash = '🔐 Login';</script>", unsafe_allow_html=True)
    del st.session_state["redirect_tab"]

auth_manager = AuthManager()
st.markdown(
    """
     <style>
        .stApp{
            background: linear-gradient(to bottom, #F1F1F1, #D97A48); 
            height: 100vh;
            margin: 0;
            padding: 0;}
            .center {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .quote-box {
            background-color: #F1F1F1;  
            border: 6px solid  #D56B6B;
            padding: 15px;
            border-radius: 5px;
            color: #000000;
            font-size: 22px; 
        }
        .prayer-box {
            background-color: #F1F1F1;
            border: 6px solid #D56B6B;
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
            font-size: 18px;
        }
         .convertor-box {
            background-color: #F1F1F1;
            border: 6px solid  #D56B6B;
            padding: 15px;
            border-radius: 5px;
            color: #000000;
            font-size: 22px; 
        }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_data
def fetch_surah_list():
    response = requests.get("https://api.alquran.cloud/v1/surah")
    if response.status_code == 200:
        data = response.json()["data"]
        return {f"{surah['englishName']} ({surah['number']})": surah["number"] for surah in data}
    return {}

def fetch_prayer_times(city):
    response = requests.get(f'http://api.aladhan.com/v1/timingsByCity?city={city}&country=&method=1&school=1')
    if response.status_code == 200:
        return response.json()['data']['timings']
    return None

def format_time(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M")
    return time_obj.strftime("%I:%M %p")

st.markdown("<div class='center'><h1>🕌 Quran-Guide</h1></div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    tab_labels= ["☪️Salah Time🕜","📖 Quote Generator", "📅 Calendar Converter", "📔 Journal", "Asma-Ul-Husna🌟", "Surah Translation", "Hadees","🔐 Login / Signup", "Donate"]
    tab_blocks = st.tabs(tab_labels)

with tab_blocks[0]:
    st.subheader("Today's Prayer Times")
    show_timed_ad("Salah Time")
    city = st.text_input('Enter your city:', 'Makkah')
    if st.button('Get Prayer Times'):
        prayer_times = fetch_prayer_times(city)
        if prayer_times:
            for prayer, time in prayer_times.items():
                formatted_time = format_time(time)
                st.markdown(f'<div class="prayer-box">{prayer}: {formatted_time}</div>', unsafe_allow_html=True)
        else:
            st.error('Failed to fetch prayer times. Please try again.')

with tab_blocks[1]:
    st.subheader("Find a Quran Quote Based on Your Emotions")
    show_timed_ad("Quote Generator")
    emotion = st.selectbox("Select your emotion:", ("Sad", "Anxious", "Grateful", "Hopeful", "Fearful", "Angry", "Guilty", "Impatient", "Insecure", "Lazy", "Happy"))
    if st.button("Get Quote"):
        quote = QuranQuoteGenerator(emotion).fetch_quote()
        if quote:
            st.markdown(f'<div class="quote-box">{quote}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error-box">Sorry, unable to fetch the quote. Please try again.</div>', unsafe_allow_html=True)

with tab_blocks[2]:
    st.subheader("Convert Dates Between Gregorian and Hijri")
    show_timed_ad("Calendar Converter")
    date = st.text_input("Enter date (DD-MM-YYYY):")
    direction = st.radio("Convert to:", ("Hijri", "Gregorian"))
    if st.button("Convert Date"):
        to_hijri = True if direction == "Hijri" else False
        converted = CalendarConverter(date, to_hijri).convert()
        st.markdown(f'<div class= "convertor-box">{converted}</div>', unsafe_allow_html=True)

journal = PrayerJournal()

with tab_blocks[3]:
    st.subheader("📝 Your Daily Journal")
    show_timed_ad("Journal")
    today = datetime.now().strftime("%Y-%m-%d")
    day_name = datetime.now().strftime("%A")
    st.markdown(f"📅 Today: **{today}** ({day_name})")
    prayers = {
        "Tahajjud": st.checkbox("Tahajjud"),
        "Fajr": st.checkbox("Fajr"),
        "Dhuhr": st.checkbox("Dhuhr"),
        "Asr": st.checkbox("Asr"),
        "Maghrib": st.checkbox("Maghrib"),
        "Isha": st.checkbox("Isha"),
    }
    dhikr = st.text_area("Your reflections:")
    if st.button("💾 Save Today's Journal"):
        if "user" not in st.session_state:
            st.warning("🔐 Please login to save your journal.")
            st.session_state["redirect_tab"] = 6
            st.rerun()
        user_id = st.session_state["user"]["localId"]
        journal.save_entry(user_id, today, prayers, dhikr)
        st.success("✅ Journal entry saved!")
        last_5 = journal.get_last_entries(user_id)
        st.markdown("### 📖 Your Last 5 Entries")
        for date, data in last_5.items():
            st.markdown(f"**{date} ({data['day']})**")
            st.markdown(f"Prayers: {', '.join([p for p, done in data['prayers'].items() if done])}")
            st.markdown(f"Dhikr: {data['dhikr']}")
        if len(last_5) >= 5:
            st.warning("🔒 You've reached 5 free entries.")
            st.markdown("[🔓 Unlock Full Journal Access ($5)](/payment)", unsafe_allow_html=True)

with tab_blocks[4]:
    st.subheader("🕋 99 Names of Allah (Asma ul Husna)")
    show_timed_ad("Asma-Ul-Husna")
    response = requests.get("https://api.aladhan.com/v1/asmaAlHusna")
    if response.status_code == 200:
        names = response.json()["data"]
        for i in range(0, len(names), 3):
            row = st.columns(3)[::-1]
            for j in range(3):
                if i + j < len(names):
                    name = names[i + j]
                    with row[j]:
                        st.markdown(f"### {name['name']}")
                        st.markdown(f"*{name['en']['meaning']}*")
                        st.markdown("---")
    else:
        st.error("Failed to fetch 99 Names of Allah. Please check the API.")

with tab_blocks[5]:
    st.subheader("🔍 View a Quran Verse")
    show_timed_ad("Surah Translation")
    surah_dict = fetch_surah_list()
    surah_name = st.selectbox("Select Surah:", list(surah_dict.keys()))
    surah_number = surah_dict[surah_name]
    verse_number = st.number_input("Enter Verse number:", min_value=1, step=1)
    if st.button("Get Verse"):
        arabic_url = f"https://api.alquran.cloud/v1/ayah/{surah_number}:{verse_number}/ar"
        english_url = f"https://api.alquran.cloud/v1/ayah/{surah_number}:{verse_number}/en.asad"
        try:
            arabic_res = requests.get(arabic_url).json()
            english_res = requests.get(english_url).json()
            arabic = arabic_res["data"]["text"]
            english = english_res["data"]["text"]
            st.markdown(f"**🕋 Arabic:** {arabic}")
            st.markdown(f"**🌍 Translation:** {english}")
        except:
            st.error("❌ Invalid Surah or Verse. Please try again.")

with tab_blocks[6]:
    st.subheader("📜 Hadith Collection")
    show_timed_ad("Hadees")

    collection = HadithCollection()

    book_labels = {
        "Sahih Bukhari": "sahih_bukhari",
        "Sahih Muslim": "sahih_muslim",
        "Jami at Tirmidhi": "Jami at Tirmidhi"  
    }

    book_name = st.selectbox("Select Hadith Book", list(book_labels.keys()))
    book_key = book_labels[book_name]

    hadiths = collection.get_hadiths_by_book(book_key)
    hadith_numbers = [h["number"] for h in hadiths]

    selected_number = st.selectbox("Select Hadith Number", hadith_numbers)

    if st.button("📥 Get Hadith"):
        hadith = collection.get_hadith_by_number(book_key, selected_number)

        if hadith:
            st.markdown(f"### 📘 {book_name} - {hadith['number']}")
            st.markdown(f"📜 {hadith['text']}")
        else:
            st.error("❌ Hadith not found.")

    
with tab_blocks[7]: 
     auth_manager.render_auth_tab()


with tab_blocks[8]:
     st.subheader("💝 Support Our Quran Guide App")

     amount = st.slider("Select donation amount ($)", 1, 100, 10)

     if st.button("Donate Now"):
        processor = PaymentProcessor("sk_test_51ROtsrCNTjOCPhsX7h4gGlbrFN8JNM9fPtaX2wjOAeQCvB57huhaOk8jnhMnpioqD3VmOEDctxhGFCEWTvJfYpA400zPESVNp4")
        checkout_url = processor.create_checkout_session(amount)

        if checkout_url:
            st.markdown(f"[👉 Click here to complete payment]({checkout_url})", unsafe_allow_html=True)
        else:
            st.error("❌ Failed to create Stripe Checkout session. Check terminal for error.")

 


st.sidebar.title("👤 Account")
if "user" in st.session_state:
    user = st.session_state["user"]
    st.sidebar.success(f"✅ Logged in as {user['email']}")
    st.sidebar.markdown(f"**User ID:** {user['localId']}")
    if st.sidebar.button("Logout"):
        del st.session_state["user"]
        st.rerun()