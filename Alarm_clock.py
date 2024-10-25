1. Imports:
from tkinter import *
import datetime
import simpleaudio as sa
import threading
2. set alarm function:
def set_alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm_triggered = False
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time and not alarm_triggered:
            alarm_message()
            alarm_triggered = True
        elif current_time != set_alarm_time:
            alarm_triggered = False
3. Alarm Message:
def alarm_message():
    print("Time to Wake up")
    wave_obj = sa.WaveObject.from_wave_file("sound.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
4. User Interface (Tkinter GUI):
root = Tk()
root.geometry("400x200")
root.title("Alarm Clock")
Tk Window: Creates the main window for the alarm clock interface.
Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()
5. Time Selection with Option Menus
frame = Frame(root)
frame.pack()
hour = StringVar(root)
hours = [str(i).zfill(2) for i in range(25)]
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)
6. Set Alarm Button
Button(root, text="Set Alarm", font=("Helvetica", 15), command=set_alarm_thread).pack(pady=20)
