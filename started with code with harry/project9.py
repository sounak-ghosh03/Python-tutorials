# A PYTHON PROGRAM CAPABLE OF REMINDING TO DRINK WATER AFTER EVERY HOUR OR TWO
# THE PROGRAM CAN EITHER BEEP OR SEND NOTIFICATION FOR A SPECIFIC OPERATING SYSTEM
# HERE WE ARE WRITING THE CODE FOR WINDOWS OPERATING SYSTEM

from plyer import notification
import pyttsx3
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while True:
    notification.notify(
        title="Reminder",
        message=("Please drink water"),
        timeout=10
    )
    engine.say(" Reminder... Please drink water")
    engine.runAndWait()
    time.sleep(3600)  # Wait for 1 hour (3600 seconds)
