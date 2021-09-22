#!/usr/bin/env python
# coding: utf-8

#module to test facial expressions

from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np
import time
label=''
def detect_expressions():
    cv2.destroyAllWindows()
    detection_model_path = 'haarcascade_frontalface_alt.xml' #path for face detection model - harcascade
    emotion_model_path = '_mini_XCEPTION.102-0.66.hdf5' #path for emotion model - xception

    face_detection = cv2.CascadeClassifier(detection_model_path) #calling cascade classifier
    emotion_classifier = load_model(emotion_model_path, compile=False) #loading emotion model
    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised","neutral"] #7 classes of emotions

    cap = cv2.VideoCapture(0) #camera

    endTime = time.time()+5 #current time + 5 seconds

    while time.time()<endTime: #the loop runs for 5 seconds
        frame = cap.read()[1] #capturing the frame
        #frame = cv2.imread('img.jpg') #input is image file
        #reading the frame
        frame = imutils.resize(frame,width=300) #resizing the image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting to image to grayscale
        faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    
        canvas = np.zeros((250, 300, 3), dtype="uint8")
        frameClone = frame.copy()
        if len(faces) > 0:
            faces = sorted(faces, reverse=True,
            key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = faces
                        # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
            # the ROI for classification via the CNN
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
        
        
            predictions = emotion_classifier.predict(roi)[0] #predicting the emotions
            emotion_probability = np.max(predictions) #probability of each emotion class
            global label
            label = EMOTIONS[predictions.argmax()] #the emotion with maximum probability
           # print(preds)
 
            for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, predictions)):
                # construct the label text
                text = "{}: {:.2f}%".format(emotion, prob * 100)

                # draw the label + probability bar on the canvas
               
                w = int(prob * 300)
                #cv2.rectangle(canvas, (7, (i * 35) + 5),
                #(w, (i * 35) + 35), (0, 0, 255), -1)
                #cv2.putText(canvas, text, (10, (i * 35) + 23),
                #cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                #(255, 255, 255), 2)
                cv2.putText(frameClone, label, (fX, fY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                              (0, 0, 255), 2)

        cv2.imshow('your_face', frameClone)
        #cv2.imshow("Probabilities", canvas)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    #while True:
     #   cv2.imshow('your_face',frameClone)
      #  if cv2.waitKey(1) & 0xFF == ord('q'):
       #         break
    listt=[label,frameClone]
    return listt
    

#detect_expressions()

