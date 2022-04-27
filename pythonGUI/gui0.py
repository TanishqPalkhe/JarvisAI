from tkinter import*
root=Tk()
root.geometry("400x200")
root.title("TANISHQ GUI")
# Important Pack options
# anchor = nw this is for direction
# side = top, bottom, left, right
# fill
# padx
# pady
raj=Label(text='''Abdul Rashid Salim Salman Khan is an Indian 
\nfilm actor, producer, occasional playback singer and television personality. In a film career spanning 
\nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film 
\nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian 
\ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian 
\ncinema. According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was''',bg="pink",fg="black",font="comicsansms 9 bold", borderwidth=3, relief=GROOVE)
# raj.pack(side=LEFT)
# raj.pack(side=LEFT,anchor="sw",fill=X)
raj.pack(side=BOTTOM,fill=X,padx=45,pady=78)
root.mainloop()