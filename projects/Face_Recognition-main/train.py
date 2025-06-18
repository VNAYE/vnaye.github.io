import cv2
import os
import numpy as np
from PIL import Image
import pickle

def get_images_and_labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    Ids = []
    names = {}
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        parts = os.path.split(imagePath)[-1].split("-")
        name = parts[0]
        Id = int(parts[1])
        names[Id] = name
        faces = detector.detectMultiScale(imageNp)
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y+h, x:x+w])
            Ids.append(Id)
    if not os.path.exists('TrainingImageLabel'):
        os.makedirs('TrainingImageLabel')
    with open('TrainingImageLabel/names.pkl', 'wb') as f:
        pickle.dump(names, f)
    return faceSamples, Ids

def train_model():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, Ids = get_images_and_labels('TrainingImage')
    recognizer.train(faces, np.array(Ids))
    recognizer.save('TrainingImageLabel/trainner.yml')

