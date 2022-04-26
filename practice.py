import speech_recognition as sr
import streamlit as st
import datetime
import webbrowser
import pyttsx3
import pywhatkit
import time

engine = pyttsx3.init()
r = sr.Recognizer()

st.title("welcome to the AI bot")

device_name = "jarvis"
def talk(text):
    engine.say(text)
    engine.runAndWait()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        talk('listening')
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            talk("sorry could not recognize")
        return voice_data

def respond(voice_data):
    if "hello" in voice_data:
        st.write(f'{device_name}:- hello there')
        talk("hello there")
    if "what is your name" in voice_data:
        st.write(f'{device_name}:- my name is jarvis')
        talk("my name is jarvis")
    if "what time it is" in voice_data:
        st.write(f'{device_name}:- it is ' + str(datetime.datetime.now().hour) + 'oclock')
        talk("it is " + str(datetime.datetime.now().hour) + " o'clock")
    if 'search' in voice_data:
        st.write(f'{device_name}:- what do u want to search for')
        talk('what do u want to search for')
        search = record_audio("what do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
    if "where is" in voice_data:
        st.write(f'{device_name}:- i dont know')
        talk("i dont know")
    if "what is my name" in voice_data:
        st.write(f'{device_name}:- hello sir you are my creator your name is deepak')
        talk("hello sir you are my creator your name is deepak")
    if "play" in voice_data:
        song = voice_data.replace('play','')
        talk("playing")
        pywhatkit.playonyt(song)
        exit()

    
    if "exit" in voice_data:
        st.write('exiting')
        talk('exiting')
        exit()

time.sleep(1)
st.write(f'{device_name}:my name is jarvis how can i help you')
talk("my name is jarvis how can i help u")
while 1:
    voice_data = record_audio()
    print(f'user:- {voice_data}')
    st.write(f'user:- {voice_data}')
    respond(voice_data)
