import tkinter as tk
from tkinter import Button, Text, Label, END

time_counting = 0.00
sts_running = False


def reset():
    global sts_running, time_counting
    sts_running = False
    inputtext.delete(1.0, END)
    time_counting = 0.00


def start(event):
    global sts_running, time_counting
    sts_running = True
    if sts_running:
        if time_counting >= 10:
            sts_running = False


def timer():
    global time_counting, sts_running
    if sts_running:
        time_counting += 1
        if time_counting >= 10:
            inputtext.delete(1.0, END)
        elif 3.5 <= time_counting < 7.5:
            inputtext.config(fg='red')
        elif time_counting >= 7.5:
            inputtext.config(fg='pink')
        elif time_counting < 3.5:
            inputtext.config(fg='black')
    screen.after(1000, timer)


def reset_timer(event):
    global time_counting
    time_counting *= 0


# GUI
screen = tk.Tk()
screen.geometry('800x600')
timer()
frame = tk.Frame(screen)
screen_label = Label(frame, text='Start Typing', font=('Arial', 18), padx=20, pady=20)
screen_label.pack()
inputtext = Text(frame, width=50, height=10, font=('Arial', 14), padx=20, pady=20)
inputtext.bind('<KeyPress>', reset_timer)
inputtext.bind('<KeyRelease>', start)
inputtext.pack()

reset_button = Button(frame, text='Reset', command=reset)
reset_button.pack()
frame.pack(expand=True)
screen.mainloop()
