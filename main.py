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

def wish_me():
    hour= (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir. How are you doing")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir. How are you doing")
    else:
        speak("Good Morning Sir. How are you doing")
    speak("I am Jarvis. Tell me sir How can i help you")

if __name__ == "__main__":
    wish_me()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
          speak("Searching Wikipedia")
          query = query.replace('wikipedia', " ")
          print(query)
          results = wikipedia.summary(query, sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)

        elif "youtube" in query:
          speak("Opening YouTube")
          webbrowser.open("youtube.com")
          
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        
        
        elif "goobye" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("Okay Sir I am always there for you.bye bye")
            exit()
               
        
    