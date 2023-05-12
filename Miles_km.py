import tkinter as tk
from tkinter import Tk,END

def mile_km():
    ml = float(miles.get())
    kilometers = round(ml*1.60934,3)
    Km["text"] = str(kilometers)

#Create the window interface
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=290,height=70)
window.config(padx=10,pady=10) #add a 10 margin

my_label = tk.Label(text="Miles",font=('Arial',10,'bold'))
my_label.grid(column=3,row=1)
my_label.config(padx=30)
my_label = tk.Label(text="is equal to",font=('Arial',10,'bold'))
my_label.grid(column=1,row=2)
my_label.config(padx=30)
my_label = tk.Label(text="Km",font=('Arial',10,'bold'))
my_label.grid(column=3,row=2)
my_label.config(padx=30)

miles = tk.Entry(width=10)
miles.grid(column=2,row=1)
Km = tk.Label(text="0",font=('Arial',10,'bold'))
Km.grid(column=2,row=2)
Km.config(padx=40)

calculate = tk.Button(text="Calculate",command=mile_km)
calculate.grid(column=2,row=3)

window.mainloop()