from time import sleep
from tkinter import *
tk=Tk()
win=Canvas(tk, width=50, height=200)
win.pack()

def light1(colour):
    win.create_oval(5,5,50,50, fill=colour)
    tk.update()

def light2(colour):
    win.create_oval(5,55,50,100, fill=colour)
    tk.update()

def light3(colour):
    win.create_oval(5,105,50,150, fill=colour)
    tk.update()
    

light1("black")
light2("black")
light3("black")

while True:
    # write your traffic light code here
    # remember each line in the loop should start with 4 spaces
    # if you want to add a time delay, use sleep(2), where 2 is the number of seconds
    # the colours you can chose from are "green", "amber" and "red"
    light1("red")
    sleep(2)
    light1("black")
    sleep(2)
