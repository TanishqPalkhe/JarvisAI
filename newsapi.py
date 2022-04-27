import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)
if __name__=='__main__':
    speak("hello Tanishq Palkhe")
    speak("welcome to the news reports")
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=00d4b952242d4f038f67d9f9a5267a3c"
    data=requests.get(url).text
    data1=json.loads(data)
    total=data1["articles"]
    for article in total:
        speak(article["title"])
        speak(article["description"])
        speak("moving on to the next news")



    

