import stripe
import streamlit as st

class PaymentProcessor:
    def __init__(self, secret_key):
        stripe.api_key = secret_key

    def create_checkout_session(self, amount_in_dollars):
        try:
            YOUR_NGROK_URL = "https://demo-quran-guide.streamlit.app"
            user = st.session_state.get("user", {})
            id_token = user.get("idToken")
            user_id = user.get("localId")

            if not id_token or not user_id:
                st.error("🔐 You must be logged in to make a payment.")
                return None

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Support Quran Guide App',
                        },
                        'unit_amount': int(amount_in_dollars * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url = f"{YOUR_NGROK_URL}/?status=success&tab=donate&token={id_token}&uid={user_id}",
                cancel_url=f'{YOUR_NGROK_URL}/?status=cancel',
                customer_email="test@example.com",
                billing_address_collection='auto',
                phone_number_collection={'enabled': False},
            )
            return session.url
        except Exception as e:
            print("❌ Stripe Error:", e)
            return None
