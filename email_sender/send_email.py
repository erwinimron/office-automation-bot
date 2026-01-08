import smtplib
from email.message import EmailMessage

def send_email():
    msg = EmailMessage()
    msg["Subject"] = "Daily Sales Report"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = "receiver@email.com"
    msg.set_content("Attached is today's sales summary.")

    with open("output/summary.xlsx", "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename="summary.xlsx"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("your_email@gmail.com", "APP_PASSWORD")
        smtp.send_message(msg)

    print("📧 Email sent")

if __name__ == "__main__":
    send_email()
