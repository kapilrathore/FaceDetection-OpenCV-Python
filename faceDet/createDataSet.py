import cv2
import os
import numpy as np
from PIL import Image

faceDetect = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

data_path = '../images'

def savefaces():

    user_data = []
    
    for path in os.listdir(data_path):

        pathName = path
        user_path = os.path.join(data_path, path)

        if user_path.endswith('.DS_Store'):
            if os.remove(user_path)  : print "Unable to delete!"
            else                : print "Deleted..."
        else:

            user_id = int(os.path.split(user_path)[1].split('-')[0])
            user_name = os.path.split(user_path)[1].split('-')[1]
            user_data.append([user_id, user_name])

            image_samples = 0
            
            for image_path in os.listdir(user_path):
                image_path = os.path.join(user_path, image_path)
        
                if image_path.endswith('.DS_Store'):
                    if os.remove(image_path)    : print "Unable to delete!"
                    else                        : print "Deleted..."
                else:
                    img = cv2.imread(image_path)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        image_samples += 1
                        cv2.imwrite('./dataSet/User-{}-{}.jpg'.format(user_id, image_samples), gray[y:y+h, x:x+w])

    write_to_file(user_data)

def write_to_file(user_details):
    text_file = open('user_data.txt', 'w')
    for user in user_details:
        text_file.write("{},{}\n".format(user[0], user[1]))
    text_file.close()

savefaces()