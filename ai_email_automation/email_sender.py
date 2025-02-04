import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, EMAIL_SUBJECT, OFFER_DESCRIPTION
from ai_generator import generate_email_content


def send_email(recipient_email: str, recipient_name: str):
    """
    Generates a personalized email using AI and sends it via SMTP.
    """
    # generate email body using AI
    email_body = generate_email_content(recipient_name, OFFER_DESCRIPTION)

    # create the MIME message, utilizing the email model in python
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    msg["Subject"] = EMAIL_SUBJECT

    # attach the email body as plain text to the email body
    msg.attach(MIMEText(email_body, "plain"))

    try:
        # connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")