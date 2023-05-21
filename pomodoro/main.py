from tkinter import Tk,Canvas,PhotoImage
import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Bebas Neue"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    text["text"] = "Timer"
    text["fg"] = GREEN
    canvas.itemconfig(timer_text,text="00:00")  
    checkmark["text"] = ""
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        text["text"] = "Break"
        text["fg"] = RED
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        text["text"] = "Break"
        text["fg"] = PINK
    else:
        count_down(WORK_MIN*60)
        text["text"] = "Work"
        text["fg"] = GREEN 
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins = math.floor(count/60)
    secs = count%60
    if mins < 10:
        mins = f"0{mins}"
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text,text=f"{mins}:{secs}")    
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark["text"] = marks

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,background=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="./pomodoro/tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,140,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

text = tk.Label(text="Timer",bg=YELLOW,font=(FONT_NAME,40,"bold"),foreground=GREEN)
text.grid(row=1,column=2)

start = tk.Button(text="Start",font=(FONT_NAME,10,"normal"),highlightthickness=0,command=start_timer)
start.grid(row=3,column=1)
reset = tk.Button(text="Reset",font=(FONT_NAME,10,"normal"),highlightthickness=0,command=reset_timer)
reset.grid(row=3,column=3)

checkmark = tk.Label(bg=YELLOW,fg=GREEN,font=(40))
checkmark.grid(row=4,column=2)

window.mainloop()
