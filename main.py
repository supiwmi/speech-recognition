#!/usr/bin/env python3

# import pyttsx3
import pyttsx4

# Importing the speech_recognition library
import speech_recognition as sr

import webbrowser
import datetime

# import pywhatkit
# import os
# import yfinance as yf
# import pyjokes
# import wikipedia


def transform():
    # Create an instance of the Recognizer class
    r = sr.Recognizer()

    # get audio from the microphone
    with sr.Microphone() as source:
        print("Speak:")
        r.pause_threshold = 0.8
        said = r.listen(source)
    try:
        print("You said " + r.recognize_google(said))
        #      print('I am listening')
        q = r.recognize_google(said, language="en")
        return speaking("You said" + q)
    except sr.UnknownValueError:
        print("Sorry, I could not understand")
        return speaking("Sorry, I could not understand")
        # return "I am waiting"
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        speaking("Sorry, I could not understand")
    #      print("Sorry the service is down")
    #      return "I am waiting"
    except ImportError:
        return "I am waiting"


def speaking(message):
    engine = pyttsx4.init()
    engine.say(message)
    engine.runAndWait()


def query_day():
    day = datetime.date.today()
    #    print(day)
    weekday = day.weekday()
    #    print(weekday)
    mapping = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    try:
        speaking(f"Tßoday is {mapping[weekday]}")
    except ImportError:
        pass


# returns the time
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speaking(f"The curent time is {time[1]} o'clock and {time[3:5]} minutes")


# greeting at start up
def whatsup():
    speaking("""Hi, I'm your personal assistant. How may I help you?""")


# the core of our asistant. Takes queries and returns answers
def querying():
    whatsup()
    start = True
    # this creates an infinite loop
    while start:
        q = transform().lower()

        if "start youtube" in q:
            speaking("starting youtube. Please wait a second.")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "start webbrowser" in q:
            speaking("opening browswer")
            webbrowser.open("https://www.google.com")
            continue

        elif "what day is it" in q:
            query_day()
            continue

        elif "what time is it" in q:
            query_time()
            continue

        elif "Goodbye" in q:
            speaking("OK Have a nice day. bye bye")
            break


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    # speaking('Please say something with your microphone')
    # transform()
    # query_day()
    # query_time()
    # whatsup()
    querying()
