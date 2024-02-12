# COSC-1100-07
# Eamonn Patterson
# Case study/Exam
#description make a converter from a grade to a point grade
##############################

from tkinter import *
import math


def clear_func():
    entry_1.delete(0, END)
    display.config(text='', background='light gray')


def calculate_func():
    entry = entry_1.get()
    if entry.isnumeric():
        get_point()
    else:
        error()


def get_point():
    entry = entry_1.get()
    if entry.isnumeric():
        if int(entry) > 89:
            display.config(text=5.0, background='light green')
        elif 84 < int(entry) < 90:
            display.config(text=4.5, background='light green')
        elif 79 < int(entry) < 85:
            display.config(text=4.0, background='light green')
        elif 74 < int(entry) < 80:
            display.config(text=3.5, background='light green')
        elif 69 < int(entry) < 75:
            display.config(text=3.0, background='light green')
        elif 64 < int(entry) < 70:
            display.config(text=2.5, background='light green')
        elif 59 < int(entry) < 65:
            display.config(text=2.0, background='light green')
        elif 54 < int(entry) < 60:
            display.config(text=1.5, background='light green')
        elif 49 < int(entry) < 55:
            display.config(text=1.0, background='light green')
        elif int(entry) < 49:
            display.config(text=0.0, background='red')
    else:
        error()


def error():
    display.config(text='ERROR please enter a valid grade')


window = Tk()
window.geometry('300x200')
window.title('Case study/Exam')


entry_1 = Entry(width=5)
entry_1.grid(row=2, column=2)

entry_label = Label(text='Enter Grade Here')
entry_label.grid(row=1, column=2, pady=10)

calculate = Button(text='Calculate', activebackground='light grey', bd=4, command=lambda: calculate_func())
calculate.grid(row=3, column=2, pady=10)

clear = Button(text='Clear', activebackground='light grey', bd=4, command=lambda: clear_func())
clear.grid(row=3, column=3, pady=10, padx=20)

display = Label(text='')
display.grid(row=2, column=3, padx=20)

display_label = Label(text='Point Value')
display_label.grid(row=1, column=3, padx=20)

window.mainloop()