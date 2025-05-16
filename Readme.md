Quran Guide is a modular, object-oriented web app built with Streamlit.The app combines prayer tools, journaling, and Islamic utilities with modern login and payment flows.
🕒 Live Clock: Displays real-time Islamic and Gregorian dates with timezone awareness (Asia/Karachi).
Calendar Converter,  Emotional Quran Quote Generator, Hadith Collection, Surah Viewer,  Asma-ul-Husna, journal,login/signup, donate.
Authentication:
✅ Email/Password Login (Firebase)
Signup and login directly within the Streamlit interface.
Users attempting to log in without registering are prompted to sign up first.On successful login, the sidebar shows:

Email, UID, Logout button
Google & Facebook Login:
Users are redirected to their respective login pages via a Netlify-based Firebase UI. made a custom page for login and hosted on netlify and added the domain in seccret.toml
These logins are functional but do not fully redirect back into the Streamlit app (frontend only).

Google OAuth Secrets
Google Client ID and Secret were configured in the Firebase Console (under Authentication > Google).
Google client ID and secret are stored in .streamlit/secrets.toml and used where needed for token verification.

Payments – Stripe Integration
Donate Button (Last Tab)
Opens a Stripe checkout page to simulate a donation.
After payment, users are redirected back to the app — with or without login.
Advertisement Banners
Shown on most feature tabs.
Can be dismissed for ~10–12 seconds.
Includes a “Buy Premium” button linked to Stripe.
💡 Use dummy card number 4242 4242 4242 4242 with any valid future date and CVC for test payments.

