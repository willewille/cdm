from RPi.GPIO import GPIO
from time import sleep

Motor1A = 27
Motor1B = 22
Motor1E = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1A,GPIO.LOW)

GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1A,GPIO.HIGH)
