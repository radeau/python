import os
import glob
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

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
email_subject = 'Test Email Subject'
email_body = 'Hello World!'

# Set up folder path
folder_path = '/python/pdf-files'

# Iterate over files in folder
for file_path in glob.glob(os.path.join(folder_path, '*')):
    if os.path.isfile(file_path):
        # Create a MIMEMultipart message and set headers
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = email_subject

        # Add body text to message
        body = MIMEText(email_body)
        message.attach(body)

        # Add attachment to message
        with open(file_path, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='pdf')
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
            message.attach(attachment)

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(message)

        print(f'Email sent successfully for file: {file_path}')

print('All emails sent successfully.')
