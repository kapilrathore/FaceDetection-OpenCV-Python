import cv2
import numpy as np


def make_predictions(userID):
    faceDetect = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainingData.yml')

    user_id = 0

    img = cv2.imread('./images/check.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        
        cv2.rectangle(img ,(x,y), (x+w, y+h), (0,255,0), 2)
        user_id, conf = recognizer.predict(gray[y:y+h, x:x+w])
        print(user_id, conf)
        cv2.putText(img, get_username_for_id(user_id), (x+w, y+h), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
        if user_id == userID:
            blur = cv2.blur(img[y:y+h, x:x+w],(25,25))
            img[y:y+h, x:x+w] = blur

    cv2.imshow('Face', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_username_for_id(user_id):
    text_file = open("user_data.txt", "r")
    for line in text_file.readlines():
        user_details = line.split(',')
        if user_id == int(user_details[0]):
            text_file.close()
            return user_details[1]
    text_file.close()
    return "User not found."

userId = raw_input('Enter your user ID : ')
make_predictions(int(userId))