import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import os
from dotenv import load_dotenv
load_dotenv()

OUTLOOK_P = os.getenv('OUTLOOK_P')
OUTLOOK_E = os.getenv('OUTLOOK_E')
SAMPLE_EMAIL = os.getenv('SAMPLE_EMAIL')
OUTLOOK_S = os.getenv('OUTLOOK_S')


# Set up SMTP server and login credentials
smtp_server = OUTLOOK_S
smtp_port = 587
smtp_username = OUTLOOK_E
smtp_password = OUTLOOK_P

# Set up email content
sender_email = OUTLOOK_E
recipient_email = SAMPLE_EMAIL
email_subject = 'Test Email Subject 2'
email_body = 'Hello World!'

# Create a MIMEMultipart message and set headers
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = email_subject

# Add body text to message
body = MIMEText(email_body)
message.attach(body)

# Add attachment to message
attachment_path = '/python/pdf-file/single.pdf'
with open(attachment_path, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='pdf')
    attachment.add_header('Content-Disposition', 'attachment', filename='attachment.pdf')
    message.attach(attachment)

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(message)

print('Email sent successfully.')
