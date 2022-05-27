import os
import smtplib
import io
import logging
import cv2
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from picamera2 import Picamera2
from PIL import Image

logger = logging.getLogger()

def take_pic():
    picam2 = Picamera2()
    config = picam2.still_configuration()
    picam2.configure(config)
    picam2.start()
    np_image = picam2.capture_array()
    is_success, im_buf_arr = cv2.imencode(".png", np_image)
    picam2.stop()
    return im_buf_arr.tobytes()

def send_text(msg_text, img_data, recipients):
    # Create message
    msg = MIMEMultipart()
    text = MIMEText(msg_text)
    msg.attach(text)
    image = MIMEImage(img_data, name="porch_photo.jpg")
    msg.attach(image)
    msg['From'] = os.environ.get('SMTP_USER')
    msg['To'] = 'Awesomeness'
    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operations via server
    server.login(os.environ.get('SMTP_USER'), os.environ.get('SMTP_PASSWORD'))
    server.sendmail(os.environ.get('SMTP_USER'), recipients.split(','), msg.as_string())
    server.quit()

def main():
    recipients = "3852196527@mailmymobile.net"
    png = take_pic()
    send_text("test", png, recipients)

if __name__ == "__main__":
    main()

