import speech_recognition as sr
import pyaudio
import pyttsx3
import wikipedia
from gtts import gTTS
from PyDictionary import PyDictionary
import playsound
import datetime
import os
from translation import baidu, google, youdao, iciba

def speak(text):
    engine = pyttsx3.init()
    dictionary = PyDictionary()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def speak_indian(text):
    tts = gTTS(text=text, lang='en-in')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

listener = sr.Recognizer()
word='alexa'
with sr.Microphone() as source:
    print("listening...")
    voice = listener.listen(source)
    cmd = listener.recognize_google(voice)
    cmd=cmd.lower()
print(cmd)
if word in cmd:
    cmd=cmd.replace('alexa','')
    if 'time' in cmd:
        timenow=datetime.datetime.now()
        cmd=timenow.strftime("%I:%M %p")
        speak(cmd)
        speak_indian(cmd)
    else:
        speak(cmd)
        speak_indian(cmd)

else:
    pass
