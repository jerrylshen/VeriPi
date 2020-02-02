import cv2
import sys
import FacRec
import readSerial

def captureWebcam(video_capture):

    while True:
        ret, frame = video_capture.read()
     
        # load openCV LBP face detector (LBP is faster but slightly less accurate than Haar classifier
        predicted_img1 = FacRec.predict(frame)
        """
        scalePercent = 50
        width = int(face.shape[1] * scalePercent/100)
        height = int(face.shape[0] * scalePercent/100)
        dim = (width, height)
        """
   #     cv2.imshow("Video", frame)
        cv2.imshow("Video", predicted_img1)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
def startWebcam():
    face_cascade = cv2.CascadeClassifier('../Downloads/lbpcascade_frontalface.xml')
    # these settings make it better at detecting faces?
    
    video_capture = cv2.VideoCapture(0)
    captureWebcam(video_capture)
    video_capture.release()
    cv2.destroyAllWindows()
        
if __name__ == "__main__":
    startWebcam()
    
    #readSerial.startSerial()
    
    
    
    
    