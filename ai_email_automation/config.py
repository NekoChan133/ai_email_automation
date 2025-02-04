import os
from dotenv import load_dotenv

# load environment variables from a .env file if present
load_dotenv()

# openAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

# SMTP configuration (example using Gmail, adjust as needed)
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "example_email@gmail.com")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "password")

# email campaign settings
EMAIL_SUBJECT = "Exclusive Digital Advertising Offer Just for You!"
OFFER_DESCRIPTION = "a 20% discount on our next campaign booking"