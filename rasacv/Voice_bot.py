## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
import speech_recognition as sr     # import the library
import shlex,subprocess
import os

import playsound
from gtts import gTTS
# sender = input("What is your name?\n")

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
# Playing the converted file
#subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])

while True:
    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Bạn nói đi tôi đang nghe nè :")
        audio = r.record(source, duration=5) # listen to the source
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
    # Playing the converted file
    #subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
