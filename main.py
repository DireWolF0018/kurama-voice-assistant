import speech_recognition as sr
import webbrowser
import datetime as dt
import time
import playsound
import os
import random
from gtts import gTTS
import requests
import subprocess

r = sr.Recognizer()


def wishMe():
    hour = dt.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Speak again you piece of shit.')
        except sr.RequestError:
            speak('Sorry, my bad.')
        return voice_data.lower()


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    speak("Tell me how can I help you now?")
    statement = record_audio().lower()
    if "good bye" in statement or "ok bye" in statement or "stop" or "exit" in statement:
        speak('Finally! The nightmare is over.')
        exit()

    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        time.sleep(5)

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now")
        time.sleep(5)

    elif "weather" in statement:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("whats the city name")
        city_name = record_audio()
        complete_url = base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                  str(current_temperature) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
            print(" Temperature in kelvin unit = " +
                  str(current_temperature) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))

        else:
            speak(" City Not Found ")

    elif 'time' in statement:
        strTime = dt.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    elif 'who are you' in statement or 'what can you do' in statement:
        speak('I am Kurama, definitely NOT! your persoanl assistant. Its my unfortunate to help lazy ass people like you with'
              'opening youtube, google chrome and gmail, tell time, predict weather'
              'in different cities, and get top headline news from times of india.'
              'Sadly there is still no cure for your lonliness so I can\'t help you with that. Please do\'nt flirt with me.')

    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("I was built by Satan")

    elif 'news' in statement:
        speak('What are you going to do with news, its not food. Imbecile!')
        news = webbrowser.open_new_tab(
            "https://timesofindia.indiatimes.com/home/headlines")
        time.sleep(6)

    elif 'search' in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)

    elif "log off" in statement or "sign out" in statement:
        speak(
            "Ok , your pc will log off in 10 sec make sure you exit from all applications")
        subprocess.call(["shutdown", "/l"])


time.sleep(3)

speak('Now what')
while 1:
    voice_data = record_audio()
    respond(voice_data)
