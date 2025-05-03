from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = Frame(master=root, height=250, width=360, bg="#d0efff")

lbl1 = Label(frame, text="Enter Your Name", bg="#3895D3", fg='green', width=15)
lbl2 = Label(frame, text="Enter Birth Date", bg="#3895D3", fg='purple', width=15)
lbl3 = Label(frame, text="Enter Birth Month", bg="#3895D3", fg='blue', width=15)
lbl4 = Label(frame, text="Enter Birth Year", bg="#3895D3", fg='black', width=15)

name_entry = Entry(frame)
date_entry = Entry(frame)
month_entry = Entry(frame)
year_entry = Entry(frame)

def calculate_age():
    name = name_entry.get()
    birth_date = int(date_entry.get())
    birth_month = int(month_entry.get())
    birth_year = int(year_entry.get())

    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_date))

    message = f"Hello {name}\n Your Age: {age} years"
    textbox.insert(END, message)

textbox = Text(bg="green", fg="black")

btn = Button(text="Calculate Age", command=calculate_age, bg="purple")

frame.place(x=20, y=10)
lbl1.place(x=20, y=20)
name_entry.place(x=160, y=20)
lbl2.place(x=20, y=60)
date_entry.place(x=160, y=60)
lbl3.place(x=20, y=100)
month_entry.place(x=160, y=100)
lbl4.place(x=20, y=140)
year_entry.place(x=160, y=140)
btn.place(x=130, y=180)
textbox.place(x=20, y=220)

root.mainloop()
