import pyttsx3          #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia                 #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit      # pip install pywhatkit


engine = pyttsx3.init('sapi5')        #Sapi5 is microsoft speech API

voices = engine.getProperty('voices')  # getting details of current voice

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # Without this command, speech will not be audible to us..
    engine.runAndWait()


def greet_introduce():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <= 12:
        speak("Good Morning!")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your assistant Pheonix, Please tell me how may I help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        speak("Pardon Please")
        return "None"  # None string will be returned
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    greet_introduce()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            speak("Searching youtube...")
            query = query.replace("play music", "")
            speak(query)
            pywhatkit.playonyt(query)
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open vscode' in query:
            codePath = "C: \\Users\\vinay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
                
        elif 'quit' in query: 
            exit()
