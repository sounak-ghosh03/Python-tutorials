# JARVIS DESKTOP ASSISTANT AI

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    # Without this command, speech will not be audible to us.
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour > 0 and hour <= 12):
        speak("Good Morning Sir!")
    elif (hour > 12 and hour <= 17):
        speak("Good Afternoon Sir!")
    elif (hour > 17 and hour <= 19):
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("I am Jarvis, how can i help you?")


def takeCommand():
    # It takes input from microphone of the user and returns the string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice or if the voice cannot be recognised
        print("I'm sorry Sir, could you please repeat it?...\n")
        speak("I'm sorry Sir, could you please repeat it?...")
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results, "\n")
            speak(results)

        elif 'open youtube' in query:
            speak("Sure Sir, Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Sure Sir, Opening google")
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            speak("Sure Sir, Opening spotify")
            os.system('start spotify')

        elif 'open instagram' in query:
            speak("Sure Sir, Opening Instagram")
            # os.system('start instagram//:')
            os.system("start https://www.instagram.com")

        elif 'open whatsapp' in query:
            speak("Sure Sir, Opening WhatsApp")
            os.system("start whatsapp://")

        elif 'open camera' in query:
            speak("Sure Sir, Opening Camera")
            os.system("start microsoft.windows.camera:")

        elif 'open linkedin' in query:
            speak("Sure Sir, Opening Linkedin")
            os.system('start linkedin://')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f" Sir, now the time is {strTime}")

        elif 'open code' in query:
            speak("Sure sir, Opening Visual studio code")
            codePath = "C:\\Users\\souna\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'quit' in query:
            print("Quitting!\n")
            speak("Sure sir, quitting!")
            exit()
