import os
import smtplib
from email.mime.text import MIMEText

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email():
    msg = MIMEText("Hello, this email is sent from Office Automation Bot 🚀")
    msg["Subject"] = "Automation Test Email"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_SENDER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    send_email()
