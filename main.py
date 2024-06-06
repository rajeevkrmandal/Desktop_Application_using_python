import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Taking voice from my system
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[16].id)
engine.setProperty('rate', 150)
def speak(text):
    """This Function takes text and return speech
      Args:
           text(_type_): string
       """
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """This fucntion will recognize voice and return text"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio=r.listen(source)

        try:
            print("Recognising")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said:{query}\n")
        except Exception as e:
            print("Say that again please")
            return "none"

        return query
text = takeCommand()
speak(text)