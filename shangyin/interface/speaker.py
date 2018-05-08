import RPi.GPIO as GPIO
import time

SPKR_PIN = 12

def init():
    GPIO.setup(SPKR_PIN, GPIO.OUT)

def beep(duration, tone):
    pwm = GPIO.PWM(SPKR_PIN, tone)
    pwm.start(40)
    time.sleep(duration)
    pwm.stop()