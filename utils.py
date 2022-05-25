import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def take_pic():


def send_text(msg_text, recipients):
    # Create message
    msg = MIMEText(msg_text)
    msg['From'] = os.environ.get('SMTP_USER')
    msg['To'] = 'Awesomeness'

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operations via server
    server.login(os.environ.get('SMTP_USER'), os.environ.get('SMTP_PASSWORD'))
    server.sendmail(os.environ.get('SMTP_USER'), recipients, msg.as_string())
    server.quit()

