import pexpect
import RPi.GPIO as GPIO
from pathlib import Path
import time
s = input() #input text

proc = pexpect.spawn('sh braillewrite.sh') #run Linux script
proc.expect('')
proc.sendline(s) #send inputted text

proc.expect('finished') #confirm script is finished

txt = Path('brailleOutputs.txt').read_text() #read output from script
txt = txt[:-1] #cut off last character of txt

brailleToBinary = { #dictionary to convert braille ASCII to binary strings
    ' ': '000000',
    '⠮': '011011',
    '⠐': '000100',
    '⠼': '010111',
    '⠫': '111001',
    '⠩': '110001',
    '⠯': '111011',
    '⠄': '000010',
    '⠷': '101111',
    '⠾': '011111',
    '⠡': '100001',
    '⠬': '010011',
    '⠠': '000001',
    '⠤': '000011',
    '⠨': '010001',
    '⠌': '010010',
    '⠴': '000111',
    '⠂': '001000',
    '⠆': '001010',
    '⠒': '001100',
    '⠲': '001101',
    '⠢': '001001',
    '⠖': '001110',
    '⠶': '001111',
    '⠦': '001011',
    '⠔': '000110',
    '⠱': '100101',
    '⠰': '000101',
    '⠣': '101001',
    '⠿': '111111',
    '⠜': '010110',
    '⠹': '110101',
    '⠈': '010000',
    '⠁': '100000',
    '⠃': '101000',
    '⠉': '110000',
    '⠙': '110100',
    '⠑': '100100',
    '⠋': '111000',
    '⠛': '111100',
    '⠓': '101100',
    '⠊': '011000',
    '⠚': '011100',
    '⠅': '100010',
    '⠇': '101010',
    '⠍': '110010',
    '⠝': '110110',
    '⠕': '100110',
    '⠏': '111010',
    '⠟': '111110',
    '⠗': '101110',
    '⠎': '011010',
    '⠞': '011110',
    '⠥': '100011',
    '⠧': '101011',
    '⠺': '011101',
    '⠭': '110011',
    '⠽': '110111',
    '⠵': '100111',
    '⠪': '011001',
    '⠳': '101101',
    '⠻': '111101',
    '⠘': '010100',
    '⠸': '010101',
    }

for i in txt:
    print(brailleToBinary[i] + " ") #print Braille text in binary form to the console

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) #set up GPIO pins

BR = 22
MR = 27
TR = 17
BL = 23
ML = 24
TL = 25 #define correct pins on Raspberry Pi
vTime = 4.5
sTime = 3.5 #define vibration time and delay time for each letter
GPIO.setup(TL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ML, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BL, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TR, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MR, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BR, GPIO.OUT, initial=GPIO.LOW) #link GPIO program to Raspberry Pi

def BinaryToOutput(s): 
    for i in range(6): #make correct pins vibrate
        if i==0:
            if s[i] == '0':
                GPIO.output(TL, GPIO.LOW)
            else:
                GPIO.output(TL, GPIO.HIGH)
        if i==1:
            if s[i] == '0':
                GPIO.output(TR, GPIO.LOW)
            else:
                GPIO.output(TR, GPIO.HIGH)
        if i==2:
            if s[i] == '0':
                GPIO.output(ML, GPIO.LOW)
            else:
                GPIO.output(ML, GPIO.HIGH)
        if i==3:
            if s[i] == '0':
                GPIO.output(MR, GPIO.LOW)
            else:
                GPIO.output(MR, GPIO.HIGH)
        if i==4:
            if s[i] == '0':
                GPIO.output(BL, GPIO.LOW)
            else:
                GPIO.output(BL, GPIO.HIGH)
        if i==5:
            if s[i] == '0':
                GPIO.output(BR, GPIO.LOW)
            else:
                GPIO.output(BR, GPIO.HIGH)

    time.sleep(vTime) #vibrate for set time
    GPIO.output(TL, GPIO.LOW)
    GPIO.output(ML, GPIO.LOW)
    GPIO.output(BL, GPIO.LOW)
    GPIO.output(TR, GPIO.LOW)
    GPIO.output(MR, GPIO.LOW)
    GPIO.output(BR, GPIO.LOW) #set all pins back down
    time.sleep(sTime) #delay for set time before next letter

for i in txt:
    BinaryToOutput(brailleToBinary[i]) #Vibrate the correct pins for each character
