import pickle
cars=["audi","suzuki","honda"]
file="cars.pkl"
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()

file="cars.pkl"
fileobj=open(file,'rb')
cars=pickle.load(fileobj)
print(cars)
from pygame import mixer

mixer.init()
mixer.music.load("water3.mp3")
mixer.music.set_volume(100)
mixer.music.play()
