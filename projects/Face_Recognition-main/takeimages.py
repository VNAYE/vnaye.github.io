import cv2
import os
import streamlit as st

def capture_images(name, num_images=70):
    if not os.path.exists('TrainingImage'):
        os.makedirs('TrainingImage')

    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    sampleNum = 0

    stframe = st.empty()

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            sampleNum += 1
            cv2.imwrite(f"TrainingImage/{name}-{sampleNum}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        # Convert the image to RGB format for Streamlit
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        stframe.image(img_rgb, channels="RGB")

        if sampleNum >= num_images:
            break

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

