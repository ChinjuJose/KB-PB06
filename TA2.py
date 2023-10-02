from tkinter import *
import random

root = Tk()
root.title("Test")
root.geometry("400x400")

def changeColor():
    colors = ["black","red","blue","gold","pink","lavender","purple","cyan","tomato","green"]
    r = random.randint(0,9)
    root.configure(background=colors[r])
    

btn = Button(root,text="Click and Change",command=changeColor)
btn.pack()

root.mainloop()

