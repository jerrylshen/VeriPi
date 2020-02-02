import math
import sendSMS
import serial
import WebCam

while True :
    linein = ser.readline()
    ser.write("test")

#https://www.dummies.com/computers/raspberry-pi/raspberry-pi-projects-for-dummies-cheat-sheet/
def startSerial():
    try:
      ser = serial.Serial('/dev/ttyACM0',115200, timeout=2)
      #its /dev/ttyACM0
    except:
      ser = serial.Serial('/dev/ttyACM1',115200, timeout=2)
"""
identity = ""

def getLabelText(label_text):
    identity = label_text
"""

def getUno(identity):
    try:
      ser = serial.Serial('/dev/ttyACM0',115200, timeout=2)
      #its /dev/ttyACM0
    except:
      ser = serial.Serial('/dev/ttyACM1',115200, timeout=2)
    ser.flushInput()
    print("hello")
    while True:
        lineIn = ser.readline()
        lineIn = str(lineIn)[2:]
        print(lineIn)
        if lineIn == "ALARM":
            #turn on facial recognition
            if identity == "Unknown Person":
                print("Unk")
                ser.write("NoFace")
                
            #if facial recognition == True:
            else:
                ser.write("YesFace")

        if lineIn == "TEXT":
          #send text via twilio
            sendSMS.send_alert()
            break
        
        if lineIn == "ENTRY":
          #send text via twilio
            sendSMS.send_entry()
            break
        #if no response, means passcode is right
