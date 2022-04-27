import os
from tkinter import*
from PIL import Image,ImageTk
tan=Tk()
# this is the place where gui code is written
tan.geometry("670x780")
tan.minsize(560,80)
tan.maxsize(2000,600)
danny=Label(text="hi this is python gui")
danny.pack()
# for png image
# photo=PhotoImage(file="pop.png")
# raj=Label(image=photo)
# raj.pack()
# for jpg image or other
image=Image.open("5.jpg")
photo=ImageTk.PhotoImage(image)
raj=Label(image=photo)
raj.pack()
tan.mainloop()
def c(exe):
    for i in range (1,4):
        with open(f"hidude/{i}.{exe}",'w') as f:
            f.write("hi")
            # os.remove(f"pythonGUI/gui{i}")
c("txt")

