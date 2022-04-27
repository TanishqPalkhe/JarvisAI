import requests
import pickle

list = []
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = requests.get(url).text
with open("had.txt", 'w') as f:
    f.write(data)
f = open("had.txt")
data = f.readlines()

# pickling
file = "gag.pkl"
total = open(file, 'wb')
pickle.dump(data, total)
total.close()
file = "gag.pkl"
total = open(file, 'rb')
read = pickle.load(total)
print(read)

