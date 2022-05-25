import pychromecast
import logging
import os
import sys
import RPi.GPIO as GPIO
import time
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Chromecast Variables
chromecast_name = os.getenv("CHROMECAST_NAME")
mp3 = os.getenv("MP3_URL")

# Setting up pin for button
pin = os.getenv("BUTTON_PIN")
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

logging.info("Starting up chromecasts")
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[chromecast_name])
cast = chromecasts[0]
cast.wait()

def play_mp3(mp3_url):
    print(mp3_url)
    cast.wait()
    mc = cast.media_controller
    mc.play_media(mp3_url, 'audio/mp3')
    mc.block_until_active()

def main():
    while True:
        input_state = GPIO.input(21)
        if input_state == False:
            play_mp3(mp3)
            logging.info("Button Pressed")
            time.sleep(0.5)
    browser.stop_discovery()

if __name__ == "__main__":
    main()

