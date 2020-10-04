import cv2
import requests
import speech_recognition as sr     # import the library
import shlex,subprocess
import os

import playsound
from gtts import gTTS
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# To capture video from webcam. 
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('img', img)
    # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
    while len(faces) != 0 :
        bot_message = ""
        message=""
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

        print("Bot nói : ",end=' ')
        for i in r.json():
            bot_message = i['text']
            print(f"{bot_message}")

        #engine = pyttsx3.init()
        #engine.say(bot_message)
        #engine.runAndWait()
        myobj = gTTS(text=bot_message,lang='vi',slow = False)
        myobj.save("welcome.mp3")
        playsound.playsound('welcome.mp3', True)
        os.remove('welcome.mp3')
        # Playing the converted file
        #subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

        while True:
            r = sr.Recognizer()  # initialize recognizer
            with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
                r.adjust_for_ambient_noise(source) 
                audio = r.listen(source) # listen to the source
            try:
                message = r.recognize_google(audio,language='vi-VN')  # use recognizer to convert our audio into text part.
                print("Bạn nói : {}".format(message))
            except:
                print("Tôi không hiểu bạn nói gì")  # In case of voice not recognized  clearly
            if len(message)==0:
                continue
            print(".....")

            r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

            print("Bot nói : ",end=' ')
            for i in r.json():
                bot_message = i['text']
                print(f"{bot_message}")
            #engine = pyttsx3.init()
            #engine.say(bot_message)
            #engine.runAndWait()
            myobj = gTTS(text=bot_message,lang='vi',slow=False)
            myobj.save("welcome1.mp3")
            playsound.playsound('welcome1.mp3', True)
            os.remove('welcome1.mp3')
            if "Kính chào tạm biệt và mong sớm gặp lại quý khách!" in  bot_message or "Kính chào tạm biệt và chúc quý khách một ngày tốt lành!" in  bot_message :
                break
        _, img = cap.read()
    # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('img', img)
    # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
            # Playing the converted file
            #subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])


            # Draw the rectangle around each face
                
                # DisplayS
        # Release the VideoCapture object
cap.release()