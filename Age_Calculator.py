from PIL import Image, ImageTk
import datetime
import tkinter as tk
window = tk.Tk()
window.geometry("400x500")
window.configure(background= "OliveDrab1")
window.title("Age_Calculator")

def calculate_age():
    name_input = str(name_entry.get()).lower()
    year = int(year_entry.get())
    month = int(month_entry.get())
    date = int(date_entry.get())
    you = Person(name_input, datetime.date(year,month,date))
    print(you)
    print(you.age())
    
    text_answer = tk.Text(master=window, height=20, width=30)
    text_answer.grid(column=1, row=6)
    text_answer.insert(tk.END, you.age())
    text_answer.insert(tk.END, you.in_days())
    
    
    
name_label = tk.Label(text="Name",padx=10,pady=6,fg='black',font=('arial', 15,'bold'),bg='OliveDrab1')
name_label.grid(column=0,row=1)                 
                 
    
year_label = tk.Label(text="Year",padx=10,pady=6,fg='black',font=('arial', 15,'bold'),bg='OliveDrab1')
year_label.grid(column=0,row=2)

month_label = tk.Label(text="Month",padx=10,pady=6,fg='black',font=('arial', 15,'bold'),bg='OliveDrab1')
month_label.grid(column=0,row=3)

date_label = tk.Label(text="Date",padx=10,pady=6,fg='black',font=('arial', 15,'bold'),bg='OliveDrab1')
date_label.grid(column=0,row=4)

name_entry = tk.Entry()
name_entry.grid(column=1,row=1,padx=10,pady=10)

year_entry = tk.Entry()
year_entry.grid(column=1,row=2,padx=10,pady=10)

month_entry = tk.Entry()
month_entry.grid(column=1,row=3,padx=10,pady=10)

date_entry = tk.Entry()
date_entry.grid(column=1,row=4,padx=10,pady=10)

calc_button =tk.Button(window,command=calculate_age, text="Calculate Now",padx=10,pady=6,fg='black',font=('arial', 15,'bold'), bg='khaki')
calc_button.grid(column=1,row=5)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __str__(self):
        return " Name: {} | Birthdate: {} ".format(self.name, self.birthdate)

    def age(self):
        now = datetime.date.today()
        age_in_years = now.year - self.birthdate.year
        age_in_days = now - self.birthdate
        return " {} is {} years old       ".format(self.name, age_in_years) #the space allows for the age_in_days to appear on the next line

    def in_days(self):
        now = datetime.date.today()
        age_in_days = now - self.birthdate
        return " ({}) ".format(age_in_days)
    
image = Image.open(r'C:\Users\USER\Desktop\soccer.jpg')
image.thumbnail((250, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1,row=0)
                  
window.mainloop()
