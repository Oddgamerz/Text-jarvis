import datetime
import webbrowser
import wikipedia
import os
import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

chrome_path = "C:\\Users\\Rajesh Kumar\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning sir,")
    elif hour >= 12 and hour < 18:
        print("Good afternoon sir,")
    else:
        print("Good evening sir,")

def takeCommand():
    print("How may i help you")
    query = str(input(''))
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if 'wikipedia' in query:
         try:
             print("Searching wikipedia...")
             query = query.replace("wikipedia", '')
             results = wikipedia.summary(query, sentences=2)
             print("According to wikipedia...")
             print(results)
             speak(results)

         except Exception as e:
             print("Sorry i couldn't do that")

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is",time)

        elif 'open amazon' in query:
            try:
                print("Opening Amazon")
                webbrowser.get('chrome').open_new_tab("amazon.in")

            except Exception as e:
                print("Sorry i couldn't open Amazon")

        elif 'open youtube' in query:
            try:
                print("Opening youtube")
                webbrowser.get('chrome').open_new_tab("youtube.com")

            except Exception as e:
                print("Sorry i couldn't open YouTube")

        elif 'open code' in query:
            try:
                code_path = "C:\\Users\\Rajesh Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)
            except Exception as e:
                print("Sorry, I couldn't open visual studio code")

        elif 'hello' or 'hi' in query:
            a = ["hello","hello sir","hi","yo"]
            print(random.choice(a))

        elif 'stop' in query:
            break

        elif 'toss' in query:
            toss = ("Heads","Tails")
            print(random.choice(toss))
           
