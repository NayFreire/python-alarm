import tkinter as tk
from tkinter import messagebox
import time
import threading
import pygame

# Initializing the audio lib
pygame.mixer.init()

# Playing the alarm sound
def play_alarm():
    pygame.mixer.music.load('alarm_project/connor.mp3')
    pygame.mixer.music.play()

# Running a separate thread to verify the time
def verify_time(time_alarm):
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == time_alarm:
            play_alarm()
            message_return = messagebox.askquestion('Alarm', 'Your time is up')
            while message_return != 'yes':
                play_alarm()
                message_return = messagebox.askquestion('Alarm', 'Your time is up')
            break
        time.sleep(1)

# Start alarm
def start_alarm():
    hour = hour_input.get()
    minute = minute_input.get()

    if hour.isdigit() and minute.isdigit():
        hour_alarm = f"{hour.zfill(2)}:{minute.zfill(2)}"
        threading.Thread(target=verify_time, args=(hour_alarm,)).start()
        messagebox.showinfo('Alarm', f'Alarm will ring at {hour_alarm}')
        app.destroy()
    else:
        messagebox.showerror('Error', 'Please, input a valid time')


app = tk.Tk()
app.title('Alarm')

tk.Label(app, text='Hora (HH)').grid(row=0, column=0)
hour_input = tk.Entry(app)
hour_input.grid(row=0, column=1)

tk.Label(app, text='Minuto (MM)').grid(row=1, column=0)
minute_input = tk.Entry(app)
minute_input.grid(row=1, column=1)

start_button = tk.Button(app, text='Start Alarm', command=start_alarm)
start_button.grid(row=2, columnspan=2)

app.mainloop()