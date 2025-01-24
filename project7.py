# TEXT TO SPEECH CONVERTER USING PYTHON

import pyttsx3
engine = pyttsx3.init()
names=["StupidProgramm1","AayushGarg15", "Yuniek"]
for name in names:
    engine.say(name)
engine.runAndWait()  