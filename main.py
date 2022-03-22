from tkinter import *
import random

t=Tk()
t.title("Select button")
t.geometry("300x350")

def wstaw_przyciski():
    ile_przyciskow = 8
    global przyciski
    przyciski = []
    dobry = random.randint(0,ile_przyciskow-1)
    for i in range (ile_przyciskow):
        if i == dobry:
            przyciski.append(Button(t,text = "button",command=trafiony))
        else:
            przyciski.append(Button(t,text = "button",command=pudlo))
    for i in przyciski:
        i.pack(fill=BOTH,expand=YES)

def trafiony():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "You Won")
    etykieta.pack(fill=BOTH,expand=YES)
    t.after(5000,restart)

def pudlo():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "Wrong Button try again")
    etykieta.pack(fill=BOTH,expand=YES)
    t.after(2000,restart)

def restart():
    etykieta.destroy()
    wstaw_przyciski()

wstaw_przyciski()
t.mainloop()
