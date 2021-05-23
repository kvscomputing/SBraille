import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) #set up GPIO

BR = 22
MR = 27
TR = 17
BL = 23
ML = 24
TL = 25
GPIO.setup(TL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ML, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TR, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MR, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BR, GPIO.OUT, initial=GPIO.LOW) #set all pins on Raspberry Pi to no vibration
