import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import re
import os
import json
import random
from urllib.request import urlopen
import time
from datetime import datetime
from voice_type import *
from playsound import playsound
import random
import omdb
import wolframalpha

vt = voice_type()
v = 0
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[v].id)
omdb.set_default("apikey", '''enter apikey here''')

cwd = os.getcwd()

def talk(text):

    engine.say(text)
    engine.runAndWait()


def take_command():

    playsound(cwd + "\\assets\\test.mp3")
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

    except Exception as e:

        print("Unable to Recognize your voice.")
        talk("Unable to Recognize your voice.")

    if "lucas" in command:
        command = command.replace("lucas", "")
    return command


def wishMe():
    hour = int(datetime.now().hour)
    
    
    
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir !")
        print("Good Morning Sir !")
    elif hour >= 12 and hour < 18:
        talk("Good Afternoon Sir !")
        print("Good Afternoon Sir !")

    else:
        talk("Good Evening Sir !")
        print("Good Evening Sir !")

    assname = "LUCAS "
    version = "1 point O"
    print("I am your Assistant " + assname + "1.0")
    talk("I am your Assistant " + assname + version)
    print("How may I help you")
    talk("How may I help you")
    


def run_lucas(v = v):

    wishMe()
    while True:
        command = take_command()
        if command != "none":
            print(command)
        if "none" == command:
            continue
        elif "game" in command:
            webbrowser.open("https://supermarioemulator.com/supermario.php")
            n = input()
        elif "play" in command:
            song = command.replace("play", "")
            talk("playing " + song)
            pywhatkit.playonyt(song)
            time.sleep(10)

        elif "powerpoint" in command:
            talk("Opening Powerpoint")
            appli = r"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
            os.startfile(appli)
            engine.runAndWait()
            time.sleep(10)
        elif "notepad" in command:
            talk("Opening Notepad")
            appli = r"C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(appli)
        elif "paint" in command:
            talk("Opening paint")
            appli = r"C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(appli)
            time.sleep(5)
        # elif 'directions' in command:

        elif "open" in command:
            reg_ex = re.search("open (.+)", command)

            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = "https://www." + domain
                webbrowser.open(url)
                talk("The website you have requested has been opened for you Sir.")
                time.sleep(3)

        elif "message" in command:
            print("Enter the recipient contact number")
            talk("Enter the recipient contact number")
            no = input()
            print("What should I send")
            talk("What should I send")
            command = take_command()
            print(command)
            pywhatkit.sendwhatmsg(
                no, command, datetime.now().hour, datetime.now().minute + 1, 5
            )

        elif "close" in command and "window" in command:
            vt.close()
        # elif 'wait' in command:
        #     talk("How long should I wait")

        elif "news" in command:
            try:
                jsonObj = urlopen(
                   #apikey 
                )
                data = json.load(jsonObj)
                i = 1

                talk("here are some top news for you")

                for item in data["articles"]:
                    print(str(i), ".", item["title"], "\n")
                    print("\t", item["description"], "\n")
                    talk(item["title"])
                    i += 1
                    if i > 10:
                        break
            except Exception as e:
                pass

        elif "weather" in command:

            # Google Open weather website
            # to get API of Open weather
            jsonObj = urlopen(
               # apikey
            )
            x = json.load(jsonObj)

            # try:
            for items in x["data"]:
                current_temperature = items["temp"]
                current_pressure = items["pres"]
                current_humidiy = items["rh"]
                z = items["weather"]
                weather_description = z["description"]
                talk("weather in chennai:")
                print(
                    " Temperature (in Celcius unit) = "
                    + str(current_temperature)
                    + "\n atmospheric pressure (in mb) ="
                    + str(current_pressure)
                    + "\n humidity (in percentage) = "
                    + str(current_humidiy)
                    + "\n description = "
                    + str(weather_description)
                )
                talk(" Temperature ," + str(current_temperature))
                talk("atmospheric pressure ," + str(current_pressure))
                talk("humidity ," + str(current_humidiy))
                talk(str(weather_description))
            # except Exception as e:
            #     talk(" City Not Found ")

        elif "time" in command:
            timen = datetime.now().strftime("%I:%M %p")
            talk("Current time is " + timen)

        elif "where is" in command:
            command = command.replace("where is", "")
            location = command
            talk("Showing")
            talk(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "activate voice keyboard" in command:
            print("Voice Keyboard activated")
            talk("Voice Keyboard activated")
            while True:
                command = take_command()
                if "deactivate" in command:
                    print("Voice keyboard deactivated")
                    talk("Voice keyboard deactivated")
                    break
                elif "save" in command:
                    vt.save()
                elif "copy" in command:
                    vt.copy()
                elif "paste" in command:
                    vt.paste()
                elif "backspace" in command:
                    vt.backspace()
                elif "enter" in command:
                    vt.enter()
                else:
                    vt.keywrite(command)
        elif "hello" in command:
            talk("Hello, How are you doing")
        elif (
            "great" in command
            or "fine" in command
            or "wonderful" in command
            or "thanks" in command
            or "thank you" in command
        ):
            talk("Happy to be at your service")
        elif "who created you" in command:
            talk(
                "I am created by the Big 3, namely Mister Joshua, Mister Geoffick and Mister Thompson"
            )

        elif "who are you man" in command or "what is your name" in command:
            talk("I am LUCAS, How are you man?")

        elif "how are you" in command:
            talk("I am wonderful, hope you are too")
        elif "minimise" in command or "minimize" in command:
            vt.mini()
            talk("window minimized")
        elif "maximize" in command or "maximize" in command:
            vt.maxi()
            talk("window maximized")
        elif "joke" in command:
            talk(pyjokes.get_joke())

        elif (
            ("terminate" in command)
            or ("exit" in command)
            or ("bye" in command)
            or ("that's it" in command)
        ):
            talk("Goodbye")
            return 0
        elif "change your voice" in command:
            if v == 0:
                v = 1
            else:
                v = 0
            engine.setProperty("voice", voices[v].id)
            talk("I have changed my voice")
        elif "toss" in command:
            playsound(cwd + "\\assets\\toss.mp3")
            flip = random.randint(0, 1)
            if flip == 0:
                print("Heads")
                talk("You recieved Heads")
            else:
                print("Tails")
                talk("You recieved Tails")
        elif "roll" in command:
            playsound(cwd + "\\assets\\Dice.mp3")
            flip = random.randint(1, 6)
            if flip == 1:
                print("You rolled 1")
                talk("You rolled 1")
            elif flip == 2:
                print("You rolled 2")
                talk("You rolled 2")
            elif flip == 3:
                print("You rolled 3")
                talk("You rolled 3")
            elif flip == 4:
                print("You rolled 4")
                talk("You rolled 4")
            elif flip == 5:
                print("You rolled 5")
                talk("You rolled 5")
            else:
                print("You rolled 6")
                talk("You rolled 6")
        elif "calculate" in command:

            app_id = "8H9R7Q-H38YE4648H"
            client = wolframalpha.Client(app_id)
            indx = command.lower().split().index("calculate")
            command = command.split()[indx + 1 :]
            res = client.query(" ".join(command))
            answer = next(res.results).text
            print("The answer is " + answer)
            talk("The answer is " + answer)
        elif "review" in command:
            talk("What movie or series would you like to hear about")
            t = take_command()
            print(t)
            data = omdb.get(title=t, fullplot=True, tomatoes=True)
            print(data["ratings"])
            for items in data["ratings"]:
                print(items["source"], ":", items["value"])
                talk(items["source"])
                talk(items["value"])
            talk("Would you like to get more details")
            command = take_command()
            if "yes" in command or "sure" in command:
                print(data["plot"])
                talk(data["plot"])
            else:
                talk("alright")
        elif "who" in command or "what" in command:

            try:
                app_id = "8H9R7Q-H38YE4648H"

                # Instance of wolf ram alpha
                # client class
                client = wolframalpha.Client(app_id)

                # Stores the response from
                # wolf ram alpha
                res = client.query(command)

                # Includes only text from the response
                answer = next(res.results).text

                print(answer)
                talk(answer)
            except Exception as e:
                info = wikipedia.summary(command, sentences=2)
                print(info)
                talk(info)

        else:
            try:
                info = wikipedia.summary(command, sentences=2)
                print(info)
                talk(info)
            except Exception as e:
                webbrowser.open(command)

run_lucas(v)

        





