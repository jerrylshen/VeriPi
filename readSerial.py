import math
import sendSMS
import serial


#https://www.dummies.com/computers/raspberry-pi/raspberry-pi-projects-for-dummies-cheat-sheet/
try:
  ser = serial.Serial('/dev/ttyACM0',115200, timeout=2)
  #its /dev/ttyACM0
except:
  ser = serial.Serial('/dev/ttyACM1',115200, timeout=2)

ser.flushInput()
while True:
    lineIn = ser.readline()
    
    if lineIn == "ALARM":
      #turn on facial recognition
      
      #if facial recognition == True:
        ser.write("Y")
      #else
        ser.write("N")
    if lineIn == "TEXT":
      #send text via twilio
     
    #if no response, means passcode is right
    
      
    
    

    """"
#for loop because i wasn't sure about the speed, delete if not wanted
count = 1
long, lad = 0, 0
temp = 0
print("start")
while True:
    
    back = ser.readline() #the important line
    back = (str(back)[2:])
    print(back[0:6])
    #print (back[0:6])
    if back[0:6] =

"""
