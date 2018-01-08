#! python3
"""Schedules periodic breaks by playing some of your favourite music from youtube"""
import time
from random import randint
import webbrowser

break_music = {'good life g eazy': "https://youtu.be/FG9M0aEpJGE",
                "overcomer" : "https://youtu.be/b8VoUYtx0kw",
               "heroes" : "https://youtu.be/a7SouU3ECpU",
               "don't let me down" : "https://youtu.be/Io0fBr1XBUA",
               "jaguar take slow" : "https://youtu.be/4gGx0rWIGvw",} # Add your favourite songs in this dictionary

def breaktime():
	"""This function chooses a song from the dictionary randomly and opens it on youtube using your default browser"""
	urls = list(break_music.values())
	index = randint(0, len(urls))
	webbrowser.open(urls[index])

sessions = 5

while sessions > 0:
	print("Program Initialized at " + time.ctime())
	print("Set to launch in the next 45mins, sit tight and proceed\n")
	time.sleep(45 * 60) # Call the breaktime function after every 45mins
	breaktime()
	sessions -= 1
