import math
import sendSMS
import serial
#https://www.dummies.com/computers/raspberry-pi/raspberry-pi-projects-for-dummies-cheat-sheet/
try:
  ser = serial.Serial('/dev/ttyACM0',115200, timeout=2)
  #its /dev/ttyACM0
except :
  ser = serial.Serial('/dev/ttyACM1',115200, timeout=2)

def conv_coords (degMin): 
    min_num = 0.0; 
    decDeg = 0.0; 
    #get the minutes, fmod() requires double 
    min_num = math.fmod(float(degMin), 100.0); 
    #rebuild coordinates in decimal degrees 
    degMin = int ( degMin / 100 );
    decDeg = degMin + ( min_num / 60 ); 
    return decDeg; 


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
