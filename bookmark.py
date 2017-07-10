import tkinter as tk
import webbrowser
import time
window = tk.Tk()
window.geometry("500x300")
window.configure(background= "DeepSkyBlue4")
window.title("Bookmark")

#enter your desired URLs here like so
URL1 = "https://youtu.be/YDSwwEeF_K8" #mateusz motivation
URL2 = "https://youtu.be/b8VoUYtx0kw" #overcomer
URL3 = "https://youtu.be/4gGx0rWIGvw" #take slow jaguar
URL4 = "https://youtu.be/XWqFFlwC_yI" #twende sudi
URL5 = "http://cleverprogrammer.teachable.com/courses/130834/lectures/2036958" #cleverprogrammer
URL6 = "https://fmovies.is/" #fmovies
def linkgo(event):
     webbrowser.open_new_tab(URL1)
   
def linkgo2(event):
    webbrowser.open_new_tab(URL3)

def linkgo3(event):
    webbrowser.open_new_tab(URL4)

def linkgo5(event):
    webbrowser.open_new_tab(URL5)
    
def linkgo6(event):
    webbrowser.open_new_tab(URL6)
    
def mybreak(event):                #item number 4
    print(" this program began at " + time.ctime())
    i = 0
    while i <= 5:
        time.sleep(60 * 5)
        webbrowser.open(URL2)
        i += 1

#you can modify the the text variable to name the buttons as you wish
button =tk.Button(window, text="MATEUZSM MOTIVATION",padx=10,pady=6,fg='black',font=('arial', 15,'bold'), bg='gold')
button.grid(column=0,row=0)

button2 =tk.Button(window, text="LISTEN TO MUSIC",padx=10,pady=6,fg='black',font=('arial', 15,'bold'), bg='gold')
button2.grid(column=1,row=1)

button3 =tk.Button(window, text="LISTEN TO MUSIC 2",padx=10,pady=6,fg='black',font=('arial', 15,'bold'), bg='gold')
button3.grid(column=0,row=2)

button4 =tk.Button(window, text="SCHEDULE A BREAK",padx=10,pady=6,fg='black',font=('arial', 15,'bold'), bg='gold')
button4.grid(column=1,row=3)

button5 =tk.Button(window, text="CLEVER PROGRAMMER",padx=10,pady=6,fg='black',font=('arial', 15,'bold'), bg='gold')
button5.grid(column=0,row=5)

button6 =tk.Button(window, text="WATCH A MOVIE ",padx=10,pady=6,fg='black',font=('arial', 15,'bold'), bg='gold')
button6.grid(column=1,row=3)

button.bind("<Button-1>", linkgo)
button2.bind("<Button-1>", linkgo2)
button3.bind("<Button-1>", linkgo3)
button4.bind("<Button-1>", mybreak)
button5.bind("<Button-1>", linkgo5)
button6.bind("<Button-1>", linkgo6)

window.mainloop()
