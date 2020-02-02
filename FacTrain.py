import cv2
import os
import numpy as np

"""
Folder trainingData has subdirectories of people
    each subdir has images of that person
    Subdirs should be named ints (i.e. 1, 2, 3, etc.)
Folder testData has images to test the trained program on

"""

people = ["Unknown Person", "Alyssa", "Jerry"]

def display_face(label, face):
    scalePercent = 30
    width = int(face.shape[1] * scalePercent/100)
    height = int(face.shape[0] * scalePercent/100)
    dim = (width, height)
    cv2.imshow(label, cv2.resize(face, dim))
    cv2.waitKey(50)

def detect_face(img):
    """ Detects face in image, returns face part of the image """
    # convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # load openCV LBP face detector (LBP is faster but slightly less accurate than Haar classifier
    face_cascade = cv2.CascadeClassifier('../Downloads/lbpcascade_frontalface.xml')
    # these settings make it better at detecting faces?
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3);
    # if face not detected, return None
    if (len(faces) == 0):
        return None, None
    # extract the face area of the image
    (x, y, w, h) = faces[0]
    # return the face part of the image
    return gray[y:y+w, x:x+h], faces[0]

def prepare_training_data(data_folder_path):
    """ Reads all training images, detects face and returns list of faces,
        and list of labels for each face """
    # gets the directories (one for each person) in data folder
    dirs = os.listdir(data_folder_path)
    # list for subject faces, and labels for subjects
    faces = []
    labels = []
    # loops through directories and reads images in them
    for dir_name in dirs:
        label = int(dir_name)
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)
        for image_name in subject_images_names:
            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            #print(image_path)
            #display_face("BLADFASDF", image)
            face, rect = detect_face(image)
            if face is not None:
                display_face("Training on image...", face)
                #add face to list of faces
                faces.append(face)
                #add label for this face
                labels.append(label)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces, labels

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
    face, rect = detect_face(img)
    display_face("image", face)
    label, confidence = face_recognizer.predict(face)
    print("label: ", label, confidence)
    label_text = people[label]
    print("label_text: ", label_text)
    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1]-5)
    return img

if __name__ == "__main__":
    print("Preparing data...")
    faces, labels = prepare_training_data("../Downloads/training-data")
    print("Data prepared")
    #print total faces and labels
    print("Total faces: ", len(faces))
    print("Total labels: ", len(labels), labels)

    face_recognizer = cv2.face.createLBPHFaceRecognizer()
    # Other face recognition stuffs
    #face_recognizer = cv2.face.createEigenFaceRecognizer()
    #face_recognizer = cv2.face.createFisherFaceRecognizer()

    face_recognizer.train(faces, np.array(labels))
    print("Creating xml")

    face_recognizer.save("trainedData.xml")
    
        

print("Training finished")

















