import speech_recognition as sr
import webbrowser
import datetime as dt
import time
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            kurama_speak(ask)
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            kurama_speak('Speak again you piece of shit.')
        except sr.RequestError:
            kurama_speak('Sorry, my bad.')
        return voice_data


def kurama_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        kurama_speak('My name is Kurama.')
    if 'time' in voice_data:
        kurama_speak(dt.datetime.now().strftime("%H:%M"))
    if 'search' in voice_data:
        search = record_audio('What do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        kurama_speak('Here is what i found: ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        kurama_speak('Here is the location i found: ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
kurama_speak('Now what')
while 1:
    voice_data = record_audio()
    respond(voice_data)
