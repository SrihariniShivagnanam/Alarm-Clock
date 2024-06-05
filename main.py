import tkinter as tk
from tkinter import messagebox
import time
import threading
import pygame
from datetime import datetime, timedelta

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Digital Clock with Alarm")
        self.root.geometry("500x400")

        self.time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
        self.time_label.pack(anchor='center', pady=20)

        self.alarm_frame = tk.Frame(root)
        self.alarm_frame.pack(anchor='center')

        self.alarm_time_var = tk.StringVar()
        self.alarm_message_var = tk.StringVar()

        self.alarm_time_entry = tk.Entry(self.alarm_frame, textvariable=self.alarm_time_var, font=('terminal', 20, 'bold'))
        self.alarm_time_entry.pack(side='left')

        self.alarm_message_entry = tk.Entry(self.alarm_frame, textvariable=self.alarm_message_var, font=('terminal', 20, 'bold'))
        self.alarm_message_entry.pack(side='left')

        self.set_alarm_button = tk.Button(self.alarm_frame, text="Set Alarm", command=self.set_alarm, font=('terminal', 20, 'bold'))
        self.set_alarm_button.pack(side='left')

        self.alarm_listbox = tk.Listbox(root, font=('calibri', 20))
        self.alarm_listbox.pack(anchor='center', pady=10)

        self.snooze_button = tk.Button(root, text="Snooze", command=self.snooze_alarm, font=('terminal', 20, 'bold'), state='disabled')
        self.snooze_button.pack(anchor='center', pady=10)

        self.alarms = []

        pygame.mixer.init()

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.check_alarms()
        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        alarm_time = self.alarm_time_var.get()
        alarm_message = self.alarm_message_var.get()
        try:
            datetime.strptime(alarm_time, '%H:%M:%S')
            self.alarms.append((alarm_time, alarm_message))
            self.alarm_listbox.insert(tk.END, f"{alarm_time} - {alarm_message}")
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format")

    def check_alarms(self):
        current_time = time.strftime('%H:%M:%S')
        for alarm_time, alarm_message in self.alarms:
            if current_time == alarm_time:
                self.trigger_alarm(alarm_message)
                self.alarms.remove((alarm_time, alarm_message))
                self.alarm_listbox.delete(0, tk.END)
                for alarm in self.alarms:
                    self.alarm_listbox.insert(tk.END, f"{alarm[0]} - {alarm[1]}")
                break

    def trigger_alarm(self, message):
        self.snooze_button.config(state='normal')
        pygame.mixer.music.load("alarm_sound.mp3")
        pygame.mixer.music.play()
        messagebox.showwarning("Alarm", message)

    def snooze_alarm(self):
        pygame.mixer.music.stop()
        self.snooze_button.config(state='disabled')
        snooze_time = (datetime.now() + timedelta(minutes=5)).strftime('%H:%M:%S')
        self.alarms.append((snooze_time, "Snoozed Alarm"))
        self.alarm_listbox.insert(tk.END, f"{snooze_time} - Snoozed Alarm")

if __name__ == "__main__":
    root = tk.Tk()
    clock = Clock(root)
    root.mainloop()
