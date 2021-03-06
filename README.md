# VeriPi, the AI Security Camera - HackUCI 2020 Project  
### (1/30-2/2)

## Inspiration
Security is vital to a safe and functional society. After hearing about the recent burglaries around Irvine, we wanted to find a way to help people know exactly what happens in their homes, so they can immediately contact the authories when trouble strikes. We found that the best way to address this issue would be to create a functional real-time security system that alerts you when an intruder has entered so that you can respond accordingly.  

## What it does
VeriPi is an IoT security camera that authenticates the user mainly through facial recognition, given that the AI is given a training dataset of images. It's designed to be placed on the door, where it can detect when people come and go, but can be placed on other potential entry points throughout a home. Each user has a limited time window to verify their identity. If they fail to do so within a set timeframe, the Raspberry Pi sends a message to the user stating that there is an intruder present. In the rare case when the camera doesn't work, the user can verify their identity through a passcode. Additionally, this passcode can be shared with people that VeriPi's AI has not been trained to recognize yet. Additionally, VeriPi's website (https://hackuci2020-266911.firebaseapp.com/) enables users to upload their own pictures to contribute towards the training set of the facial recognition algorithm.

## How we built it
The Arduino Uno, as the slave, has the following modules: accelerometer, capacitive input, and LED light.
The Raspberry Pi 4, as the master, is used to train the AI and conduct the facial recognition aspect, while also being connected to the Internet, where it can send SMS messages to the emergency contact.    

The Uno and Pi are both connected and communicate via serial. This relationship allows the Uno to be powered by the Pi which is, in turn, powered externally by a battery or outlet.

Our website was created using Javascript, HTML, and CSS. It also leveraged the tools from Cloudinary to allow connection between users from anywhere in the world and their VeriPi.

## APIs Used
OpenCV - uses machine learning to recognize faces and determine whether or not a user is authorized to enter.  

Twilio - texts the user if an unauthorized user has been detected.  

Cloudinary - allows the user to upload photos through our website, which can be directly accessed by the Raspberry Pi.


## Challenges we ran into

Assembling the hardware was somewhat challenging. It's more that there are a lot of modules and wires to manage and try to organize.

Since it was our first time using OpenCV, we ran into some challenges when trying to get the features to work together. It was difficult to figure out which tools were best suited to handle the face detection and machine learning for our situation.  Providing good training data so that OpenCV could recognize individual faces was something that was accomplished with a lot of trial and error.  We also tried a few different facial recognition algorithms before finding one that worked consistently.

On the front-end side, it was difficult to find which API use to upload the images online. While we initially pursued Google's Photos and Drive APIs, we soon found that the severe lack of thoroughness and clearness in documentation worsened by the tight security of the APIs made them too difficult to navigate, particularly given our time constraint. Additionally, the entire team had little to no prior web development experience, so we already had to read plenty of other documentation and learn new syntax. This struggle pushed us to explore various APIs, eventually settling with the Cloudinary API which was both well-documented and broadly supported.

## Accomplishments that we're proud of

In the end, we successfully wrote a program that uses facial recognition and machine learning with a tangible application in the real world. In doing so, we have gained an awareness of the potential impact of our work as creative developers, integrating a multitude of concepts and tools into seamless processes that can be put to good use.  

We successfully trained OpenCV's facial recognition algorithm to recognize a few particular faces.  Our program uses the results of the facial recognition to send information to the Raspberry Pi, which then sends text message alerts through Twilio based on who it detects.

## What we learned

For OpenCV, we learned how to use its diverse tools to detect faces and create accurate models. To ensure the accuracy of our model, we utilized a large dataset of images to both train and test our end-product.  

In the front-end, we learned how to implement an image drag-and-drop feature using Javascript, HTML, and CSS. To do this, we learned about event listeners and handlers to upload the images with their respective name. We also decided to create objects to store the names of the people and their respective images. Additionally, we learned how to use an API to upload images online. From there, we could use a python script that downloads the images for OpenCV to use.  

We ultimately learned how to use a variety of new tools that have a wide range of applications. Through these experiences, we have grown to better understand how those working together to create a product should be aware of their impact on the work of others so that a cohesive product can be put together in the end.  

## What's next for VariPi  
After the initial base project, we would like to add the following features:  
1. We could make the text message include the image of the intruder if it recognizes that it is an unauthorized user.  
2. Additionally, we could add another camera in the front of the door that continuously records and tracks faces, and if the door is opened and the indoor camera is unable to recognize the face, the front camera would look through the previous footage to find the face of the intruder.  
3. In the setup, you can choose whether or not to automatically call 911 if you do not respond within a certain amount of time to the automated message.  
4. The website will have more features such as being able to remove previously uploaded photos from the training set and viewing all photos separated by person from the training set online.

# Built With  
Arduino Uno rev3, accelerometer, 8 key capacitive, Grove shield, LED Light, and buzzer  

Raspberry Pi 4, USB cables, monitor (development/debugging)  

Arduino IDE: C/C++  

Raspbian OS: Python, Twilio, OpenCV  
Website: HTML, CSS, Javascript, Cloudinary, Firebase

# Other Notes  
The sendSMS python file isn't here. It's the standard Twilio starter code with the API keys and such
