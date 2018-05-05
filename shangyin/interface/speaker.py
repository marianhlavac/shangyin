import RPi.GPIO as GPIO

SPKR_PIN = 12

def init():
    GPIO.setup(SPKR_PIN, GPIO.OUT)

def beep(time, tone):
    pwm = GPIO.PWM(SPKR_PIN, time)
    pwm.start(50)
    time.sleep(time)
    pwm.stop()