# AISecurityCamera - HackUCI 2020 Jan 30 - Feb 2 Project 

## Inspiration
Security is vital to have a safe and functional society. After hearing about the recent burglaries around Irvine, we wanted to find a way to help people know exactly when it happens so they can contact the authories quickly. We found that the best way to address this issue would be to create a functional real-time security system that alerts you when an intruder has entered so that you can respond accordingly.

## What it does
The blah is a security camera that authenticates the user mainly through facial recognition. The blah is designed to be placed on the door, where it can detect the movement of the door. The user has a limited time window to verify their identity. In the small chance where the camera doesn't work, the user can verify through a passcode. Also, the passcode can be used by people that the blah hasn't trained the AI on yet. If the user does not verify themselves within the timeframe, the Raspberry Pi sends messages the user stating that there is an intruder present.

## How we built it
The Arduino Uno, as slave, has the following modules: accelerometer, capacitive input, and LED light
The Raspberry Pi 4, as master, is used to conduct the facial recognition aspect while also being connected to the Internet, where it can send SMS messages to the emergency contact.

The Uno and Pi are connected and communcate through serial. The Uno is powered by the Pi, and the Pi is powered externally.


## APIs Used
OpenCV - uses machine learning to recognizes faces and determine whether the user is authorized
Twilio - texts the user if it determines that an unauthorized user has entered.


## Challenges we ran into
Getting OpenCV to work. [add more details]
Assembling everything [add more details]

Since it was the first time we had used OpenCV and the Google Photos API, we ran into some challenges when trying to get the features to work together. In terms of OpenCV, it was difficult to figure out which tools were best suited to handle the face detection and machine learning for our situation.


## Accomplishments that we're proud of
It works [add more details]

We were able to successfully write a program that uses facial recognition and machine learning that has a tangible application in the real-world.  We learned how to use the APIs OpenCV and Google Photos for both the software to work, and to have a user interface that is easy to use.

## What we learned
OpenCV, Uno, Pi [add more details]

For OpenCV, we learned how to use the diverse tools offered by OpenCV to detect faces and create accurate models. To do this, we also learned how to train models based on images and check how accurate the model is by using the test set. 

## What's next for Blah
After the current base project, we would like to add the following features:
1. We could make the text message include the image of the intruder if it recognizes that it is an unauthorized user. 
2. Additionally, we could add another camera in the front of the door that continuously records and tracks faces, and if the door is opened and the indoor camera is unable to recognize the face, the front camera would look through the previous footage to find the face of the intruder.
3. In the setup, you can choose whether or not to automatically call 911 if you do not respond within a certain amount of time to the automated message.

# Built With
Arduino Uno rev3, acceleromter, 8 key capacitive, Grove shield, LED Light
Raspberry Pi 4, USB cables, monitor (development/debugging)
Arduino IDE: C/C++
Raspbian OS: Python
Twilio
