import tkinter

window = tkinter.TK()
window.title("My First GUI Program")

window.minsize(width=588, weight=300)
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bald"))
my_label.pack(expand=True)

import turtle 

tim = turtle.Turtle()
tim.write()