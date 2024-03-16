import smtplib
from email.mime.text import MIMEText
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# os.getenv('PATH')
path = ""
recipients_excel = pd.read_excel(path)
subject = "Email Subject"
body = "This is the body of the text message"
recipients = []
for  destino in recipients_excel["Email"]:
    if pd.notna(destino):
        recipients.append(destino)
sender = os.getenv('GMAIL_SENDER')
password = os.getenv('GMAIL_PASSWORD')


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)