import tkinter as tk
from tkinter import Canvas,PhotoImage
import pandas as pd
from random import choice    

BACKGROUND_COLOR = "#B1DDC6"
FONT_COLOR = "#0A4D79"
ENG_COLOR = "#198AD5"
dt_path = r"""./FlashCard_EN_ES/data/words_to_learn.csv"""
dt_path_2 = r"""./FlashCard_EN_ES/data/english_words.csv"""
current_word = {}
data_dict = {}

try:
    data = pd.read_csv(dt_path)
except FileNotFoundError:
    data = pd.read_csv(dt_path_2)
finally:
    data_dict = data.to_dict(orient="records")

def new_word():
    global current_word,delay
    window.after_cancel(id=delay)
    current_word = choice(data_dict)
    canvas.itemconfig(card_title,text=list(data.columns.values)[0],fill=ENG_COLOR)
    canvas.itemconfig(card_word,text=current_word["English"],fill=FONT_COLOR)
    canvas.itemconfig(card_image,image=front_card)
    delay = window.after(3000,func=flip_card)

def knew_word():
    try:
        data_dict.remove(current_word)
        data_knew = pd.DataFrame(data_dict)
        data_knew.to_csv("./FlashCard_EN_ES/data/words_to_lean.csv",index=False)
    except ValueError:
        pass

def flip_card():
    canvas.itemconfig(card_image,image=back_card)
    canvas.itemconfig(card_title,fill="white",text=list(data.columns.values)[1])
    canvas.itemconfig(card_word,fill="white",text=current_word["Spanish"])
# USER INTERFACE - UI
window = tk.Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR,padx=20,pady=20)

delay = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card = PhotoImage(file="./FlashCard_EN_ES/images/card_front.png")
back_card = PhotoImage(file="./FlashCard_EN_ES/images/card_back.png")
card_image = canvas.create_image(400,526/2,image=front_card)
card_title = canvas.create_text(400,150,text="",font=("Arial",40,"italic"),fill=ENG_COLOR)
card_word = canvas.create_text(400,300,text="",font=("Arial",60,"bold"),fill=FONT_COLOR)
canvas.grid(row=0,column=0,columnspan=2,rowspan=2)

good = PhotoImage(file="./FlashCard_EN_ES/images/right.png")
good_button = tk.Button(window,image=good,highlightthickness=0,borderwidth=0,command=knew_word)
good_button.grid(row=2,column=1)
wrong = PhotoImage(file="./FlashCard_EN_ES/images/wrong.png")
wrong_button = tk.Button(window,image=wrong,highlightthickness=0,borderwidth=0,command=new_word)
wrong_button.grid(row=2,column=0)

new_word()

window.mainloop()

