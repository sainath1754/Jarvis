import speech_recognition as sr
import pyttsx3
import webbrowser as web
import datetime
import wikipedia
import pywhatkit
import os
from geopy.distance import great_circle
from geopy.geocoders import nominatim
import geocoder
import requests


def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0<=hour<12:
        print("Good Morning")
        speak("Good Morning")
    elif 12<=hour<18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    print("hi,how can i help you?............")
    speak("hi,how can i help you?............")


def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing ...")
        speak("recognizing ...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said : {query}")
        return query
    except Exception as e:
        print(f'error : {e}')
        return 'error'


def open_website(url):
    speak(f"opening {url}")
    web.open(url)








def stop_prog():
    print("you have exited successfully...")
    speak("you have exited successfully...")
    exit()


def main():
    print("hi, i am your voice assistant")
    speak("hi, i am your voice assistant")
    wish_me()
    while True:
        query = take_command().lower()

        if "open youtube" in query:
            open_website("https://www.youtube.com")

        elif "play".lower() in query:
            query = query.replace("search youtube"," ")
            speak("searching in youtube for"+query)
            print("searching in youtube for" + query)
            pywhatkit.playonyt(query)

        elif ("open insta" in query) or ("open instagram" in query):
            open_website("https://www.instagram.com")

        elif "open whatsapp" in query:
            open_website("https://web.whatsapp.com/")

        elif ("tell about" in query) or ("search about" in query):
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(f"According to wikipedia,{results}")
            speak(results)


        elif ("stop" in query) or ("end" in query) or ("exit" in query) or ("finish" in query):
            stop_prog()



if __name__=="__main__":
    main()

