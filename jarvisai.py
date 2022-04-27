import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from PIL import Image

# open method used to open different extension image file
im = Image.open(r"C:\Users\hp\PycharmProjects\pythonProject\wp1913286.png")

# This method will show image in any image viewer
im.show()
engine=pyttsx3.init('sapi5')#sapi5 is used to take voices from windows
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if 0<hour<12:
        speak("good morning")
    elif 12<=hour<=16:
        speak("good afternoon")
    elif 16<hour<=19:
        speak("good evening")
    else:
        speak("good night")

    speak("hi sir i am jarvis how can i help you")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.energy_threshold=6000
        audio=r.listen(source)
    try:
        print("Recognising....")
        total=r.recognize_google(audio,language="en-in")
        print(f"user said  {total}\n")
    except Exception as e:
        print("say that again please")
        return "None"
    return total

if __name__=="__main__":
    wishMe()
    for i in range (0,20):
        total=takecommand().lower()
        if 'wikipedia' in total:
            speak("searching wikipedia")
            total=total.replace("wikipedia","")
            results=wikipedia.summary(total,sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in total:
            webbrowser.open("youtube.com")
        elif 'open youtube' in total:
            webbrowser.open("google.com")
        elif 'open facebook' in total:
            webbrowser.open("facebook.com")
        elif 'play music' in total:
            music_dir="C:\\thas" # mention the path of the folder where the music files are stored
            songs=os.listdir(music_dir)
            a=random.choice(songs)
            os.startfile(os.path.join(music_dir,a))
        elif 'time' in total:
            rtime=datetime.datetime.now()
            speak(f"the current time is {rtime}")
        elif 'stop' in total:
            exit()
        elif 'who are you'in total:
            speak("i am  jarvis i am a kind of ai that is created for you ")
        elif 'tanishq' in total:
            speak("tanishq is a very handsome boy he  live in india and he loves programming")
        elif 'image' in total:
            pic_dir="C:\\cool" # mention the path of the folder where the images are stored
            kite=os.listdir(pic_dir)
            a = random.choice(kite)
            os.startfile(os.path.join(pic_dir, a))
        elif 'weather' in total:
            speak("weather is too cold ")
        elif 'how are you' in total:
            speak("i am fine sir")
