import time
from pygame import mixer
import datetime
def log():
    with open("log.txt",'w') as f:
        f.write(f"time to complete music is {datetime.datetime.now()}\n")
if __name__=="__main__":
    water = time.time()
    music1=time.time()
    music2=time.time()
    watraw=5
    mu1=10
    mu2=20
    while True:
        if time.time()-water>watraw:
            mixer.init()
            mixer.music.load("water3.mp3")
            mixer.music.play()
            water=time.time()
            log()
            if input()=="s":
                mixer.music.stop()
        if time.time()-music1>mu1:
            mixer.init()
            mixer.music.load("eye.mp3.mp3")
            mixer.music.play()
            music1 = time.time()
            log()
            if input()=="s":
                mixer.music.stop()

        if time.time()-music2>mu2:
            mixer.init()
            mixer.music.load("exercise.mp3.mp3")
            mixer.music.play()
            music2 = time.time()
            log()
            if input()=="s":
                mixer.music.stop()






