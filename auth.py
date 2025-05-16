import streamlit as st
import pyrebase

class AuthManager:
    def __init__(self):
        self.firebaseConfig = {
            "apiKey": "AIzaSyCMprrKEi64KhuApnhze7ZpdAKP7DmYJxc",
            "authDomain": "quran-guide-9b941.firebaseapp.com",
            "databaseURL": "",
            "projectId": "quran-guide-9b941",
            "storageBucket": "quran-guide-9b941.appspot.com",
            "messagingSenderId": "725958461341",
            "appId": "1:725958461341:web:c396f99963b498a06c9174"
        }
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.auth = self.firebase.auth()
        self.oauth_login_url = "https://preeminent-marigold-b1bae0.netlify.app?next=https://demo-quran-guide.streamlit.app"

    def login(self):
        st.subheader("🔐 Email Login")

        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        st.markdown("Or login using your Google or Facebook account:")
        st.markdown(
            f"""
            <div style='text-align:center'>
                <a href="{self.oauth_login_url}" target="_self">
                    <img src='https://img.shields.io/badge/Login%20with-Google-red?logo=google' />
                </a>&nbsp;&nbsp;
                <a href="{self.oauth_login_url}" target="_self">
                    <img src='https://img.shields.io/badge/Login%20with-Facebook-blue?logo=facebook' />
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("Login"):
            try:
                user = self.auth.sign_in_with_email_and_password(email, password)
                st.session_state["user"] = {
                    "email": user["email"],
                    "localId": user["localId"]
                }
                st.success("✅ Logged in successfully!")
                st.rerun()
            except:
                st.error("❌ Invalid email or password.")

    def signup(self):
        st.subheader("🆕 Email Signup")

        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")

        if st.button("Create Account"):
            try:
                self.auth.create_user_with_email_and_password(email, password)
                st.success("✅ Account created! You can now log in.")
            except:
                st.error("❌ Failed to create account. Try a stronger password.")

    def reset_password(self):
        st.subheader("🔁 Reset Password")

        email = st.text_input("Enter your email", key="reset_email")
        if st.button("Send Reset Link"):
            try:
                self.auth.send_password_reset_email(email)
                st.success(f"📩 Reset email sent to {email}.")
            except:
                st.error("❌ Failed to send reset email.")

    def render_auth_tab(self):
        st.title("🛂 Account Access")
        tabs = st.tabs(["Login", "Sign Up", "Reset Password"])

        with tabs[0]:
            self.login()
        with tabs[1]:
            self.signup()
        with tabs[2]:
            self.reset_password()
