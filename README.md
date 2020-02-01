# AISecurityCamera - HackUCI 2020 Jan 30 - Feb 2 Project 

## Inspiration


## What it does
The blah is a security camera that authenticates the user mainly through facial recognition. The blah is designed to be placed on the door, where it can detect the movement of the door. The user has a limited time window to verify their identity. In the small chance where the camera doesn't work, the user can verify through a passcode. Also, the passcode can be used by people that the blah hasn't trained the AI on yet.

## How we built it
The Arduino Uno, as slave, has the following modules: accelerometer, capacitive input, and LED light
The Raspberry Pi 4, as master, is used to conduct the facial recognition aspect while also being connected to the Internet, where it can send SMS messages to the emergency contact.

The Uno and Pi are connected and communcate through serial. The Uno is powered by the Pi, and the Pi is powered externally.


## APIs Used
OpenCV
Twilio


## Challenges we ran into
Getting OpenCV to work. [add more details]
Assembling everything [add more details]



## Accomplishments that we're proud of
It works [add more details]

## What we learned
OpenCV, Uno, Pi [add more details]

## What's next for Blah
...

# Built With
Arduino Uno rev3, acceleromter, 8 key capacitive, Grove shield, LED Light
Raspberry Pi 4, USB cables, monitor (development/debugging)
Arduino IDE: C/C++
Rasbian OS: Python
Twilio
