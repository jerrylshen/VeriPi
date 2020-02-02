import cv2
import os
import numpy as np
import FacTrain
import readSerial

"""
Folder trainingData has subdirectories of people
    each subdir has images of that person
    Subdirs should be named ints (i.e. 1, 2, 3, etc.)
Folder testData has images to test the trained program on

"""

people = ["Unknown Person", "Alyssa", "Jerry"]

print("Start predicting")

face_recognizer = cv2.face.createLBPHFaceRecognizer()
face_recognizer.load("trainedData.xml")

def display_face(scale, label, face):
    scalePercent = scale
    width = int(face.shape[1] * scalePercent/100)
    height = int(face.shape[0] * scalePercent/100)
    dim = (width, height)
    cv2.imshow(label, cv2.resize(face, dim))
    #cv2.waitKey(0)
    
def detect_faceRec(img):
    """ Detects face in image, returns face part of the image """
    # convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # load openCV LBP face detector (LBP is faster but slightly less accurate than Haar classifier
    face_cascade = cv2.CascadeClassifier('../Downloads/lbpcascade_frontalface.xml')
    # these settings make it better at detecting faces?
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(100, 100));
    # if face not detected, return None
    if (len(faces) == 0):
        return None, None
    # extract the face area of the image
    (x, y, w, h) = faces[0]
    # return the face part of the image
    return gray[y:y+w, x:x+h], faces[0]

def draw_rectangle(img, rect):
    """ Draws rectangle on image according to given (x, y) coordinates
        and given width and height """
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
def draw_text(img, text, x, y):
    """ Draws text on given image starting from passed (x, y) coordinates """
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

def predict(test_img):
    img = test_img.copy()
    face, rect = detect_faceRec(img)
    
    try:
        display_face(100, "image", face)
        label, confidence = face_recognizer.predict(face)
        if confidence > 70:
            label = 0
        #print("label: ", label, confidence)
        label_text = FacTrain.people[label]
        #print("label_text: ", label_text)
        draw_rectangle(img, rect)
        draw_text(img, label_text, rect[0], rect[1]-5)
        print("asdfasF")
        readSerial.getUno(label_text)
        return img
    except:
        return img

if __name__ == "__main__":
    print("Predicting images...")

    #load test images
    test_img1 = cv2.imread("../Downloads/test_data/alyssa1.jpg")
    test_img2 = cv2.imread("../Downloads/test_data/jerry1.jpg")
    test_img3 = cv2.imread("../Downloads/test_data/girl1.jpg")

    #perform a prediction
    predicted_img1 = predict(test_img1)
    predicted_img2 = predict(test_img2)
    predicted_img3 = predict(test_img3)
    print("Prediction complete")

    #display both images
    display_face(30, people[1], predicted_img1)
    display_face(30, people[1], predicted_img2)
    display_face(100, people[0], predicted_img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
print("Images predicted")











