# Alarm-Clock

This is an advanced digital clock application built using Python's Tkinter for the graphical user interface and Pygame for playing alarm sounds. The application allows users to set multiple alarms, snooze alarms, and provides a user-friendly interface.

Features:
-Digital Clock: Displays the current time in HH:MM:SS format.
-Multiple Alarms: Allows setting multiple alarms with customizable messages.
-Snooze Functionality: Enables snoozing alarms for a specified duration (default is 5 minutes).
-Sound Alerts: Plays a sound when an alarm goes off.
-User-Friendly Interface: Easy-to-use interface with clear labels and buttons.

Attributes:
root: The main Tkinter window.
time_label: Label to display the current time.
alarm_frame: Frame to contain alarm input fields and button.
alarm_time_var, alarm_message_var: Variables to store the alarm time and message.
alarm_time_entry, alarm_message_entry: Entry fields for inputting alarm time and message.
set_alarm_button: Button to set an alarm.
alarm_listbox: Listbox to display set alarms.
snooze_button: Button to snooze the alarm.
alarms: List to store multiple alarms.

Methods:
__init__(self, root): Initializes the UI elements and starts the clock update loop.
update_clock(self): Updates the current time every second and checks for alarms.
set_alarm(self): Adds a new alarm to the list and updates the listbox.
check_alarms(self): Checks if any alarm matches the current time and triggers it.
trigger_alarm(self, message): Plays the alarm sound and displays a message box.
snooze_alarm(self): Snoozes the alarm for 5 minutes and updates the list.
