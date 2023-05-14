from distutils.cmd import Command
from re import search
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import pyttsx3
import pywhatkit
from gtts import gTTS
from time import ctime
r = sr.Recognizer()

def record_audio(ask=False):
  with sr.Microphone() as source:
    if ask:
        miram_speak(ask)
    audio =r.listen(source)
    voice_data= ""
    try:
        voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
        miram_speak("sorry, I did not get that")
    except sr.RequestError:
        miram_speak("sorry , my speech service is down")
    return voice_data

def miram_speak(audio_string):
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        miram_speak('My name is Miram')
    if 'what is the date and time' in voice_data:
        miram_speak(ctime())
    if 'search' in voice_data:
        search=record_audio('what do you want to search for?')
        url='http://google.com/search?q='+search
        webbrowser.get().open(url)
        miram_speak('here is what I found for ' +search)
    if 'find location' in voice_data:
        location=record_audio('what location you want?')
        url = 'https://www.google.nl/maps/place/' +location +"/&amp;"
        webbrowser.get().open(url)
        miram_speak('here is the location of'+location)
    if 'play' in voice_data:
        song=record_audio('what do you want to play?')
        pywhatkit.playonyt(song)

    if 'exit' in voice_data:
        exit()
time.sleep(1)
miram_speak("HEY user")
miram_speak("how can i help you?")     
while 1:
    voice_data=record_audio()
    respond(voice_data)
