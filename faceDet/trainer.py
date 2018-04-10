import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataSet'

def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    user_ids = []

    for imagePath in imagePaths:
        if imagePath.endswith('.DS_Store'):
            if os.remove(imagePath)  : print "Unable to delete!"
            else                : print "Deleted..."
        else:
            faceImage = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImage, 'uint8')
            user_id = int(os.path.split(imagePath)[-1].split('-')[1])
            faces.append(faceNp)
            user_ids.append(user_id)
            cv2.imshow('training', faceNp)
            cv2.waitKey(10)

    return np.array(user_ids), faces


user_ids, faces = getImagesWithID(path)
recognizer.train(faces, user_ids)
recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()