import webbrowser
import time
from random import randint

break_music = {'good life g eazy': "https://youtu.be/FG9M0aEpJGE",
                "overcomer" : "https://youtu.be/b8VoUYtx0kw",
               "heroes" : "https://youtu.be/a7SouU3ECpU",
               "don't let me down" : "https://youtu.be/Io0fBr1XBUA",
               "jaguar take slow" : "https://youtu.be/4gGx0rWIGvw",}

#Add a song to your playlist here below , (name of song, youtube url)

#break_music.setdefault( )

#preferred time is 45mins
def breaktime():
	urls = list(break_music.values())
	index = randint(0, len(urls))
	webbrowser.open(urls[index])


sessions = 5
while sessions > 0:
	print("Program Initialized at " + time.ctime())
	print("Set to launch in the next 45mins, sit tight and proceed\n")
	time.sleep(45 * 60)
	breaktime()
	sessions -= 1
