import tkinter as tk
from tkinter import Tk,Canvas,PhotoImage,messagebox
from random import randint,choice,shuffle
import pyperclip
import json 

FONT_NAME = "Rockwell"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','_']

    temporal_letters = [choice(letters) for letter in range(1,randint(8,10)+1)] 
    temporal_numbers = [choice(numbers) for number in range(1,randint(2,4)+1)] 
    temporal_symbols = [choice(symbols) for symbol in range(1,randint(2,4)+1)] 

    password = temporal_letters + temporal_numbers + temporal_symbols
    shuffle(password)

    password = ''.join(password)

    pass_name.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
pass_path = r"""./pass_manager/passwords.json"""
def save_pass():
    new_data = {website_name.get():{"email":email_name.get(),"password":pass_name.get()}}
    if website_name.get()=="" or pass_name.get()=="":
        messagebox.showwarning(title="Missing info",
        message=f"Website or Password are empty, please fill that fields.")
    else:
        try:
            with open(pass_path,'r') as f:
                #json.dump(new_data, f,indent=4) #write on json data 
                #data = json.load(f) #Read json data
                #reading old data
                data = json.load(f)
        except FileNotFoundError:
             with open(pass_path,'w') as f: 
                 json.dump(new_data,f,indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open(pass_path,'w') as f:
                #saving updated data
                json.dump(data,f,indent=4) #update json data
        finally:
            website_name.delete(0,'end')
            pass_name.delete(0,'end')
# ---------------------------- SEARCH DATA ---------------------------- #
def search_data():
    website_info = website_name.get()
    try:
        with open(pass_path,"r") as f:
            searched_data = json.load(f)
        messagebox.showinfo(title=website_info,
                message=f"Email: {searched_data[website_info]['email']}\nPassword: {searched_data[website_info]['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="File empty",message="You need to add info")
    except KeyError as key_error:
        messagebox.showerror(title="Key Error",message=f"The key {key_error} haven't found in the file")
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50,bg="white")

canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
padlock = PhotoImage(file="./pass_manager/logo.png")
canvas.create_image(100,100,image=padlock)
canvas.grid(row=0,column=1)

website = tk.Label(text="Website:",font=(FONT_NAME,12),bg="white")
website.grid(row=1,column=0)
email = tk.Label(text="Email/Username:",font=(FONT_NAME,12),bg="white")
email.grid(row=2,column=0)
password = tk.Label(text="Password:",font=(FONT_NAME,12),bg="white")
password.grid(row=3,column=0)
website_name = tk.Entry(width=30)
website_name.grid(row=1,column=1)
website_name.focus()
email_name = tk.Entry(width=53)
email_name.grid(row=2,column=1,columnspan=2)
email_name.focus()
email_name.insert(0,"prueba@gmail.com")
pass_name = tk.Entry(width=31)
pass_name.grid(row=3,column=1)
generate_pass = tk.Button(text="Generate Password",font=(FONT_NAME,8),width=18,command=random_generator)
generate_pass.grid(row=3,column=2)
add_pass = tk.Button(text="ADD",width=53,font=(FONT_NAME,8),command=save_pass)
add_pass.grid(row=4,column=1,columnspan=2)
search = tk.Button(text="Search",font=(FONT_NAME,8),width=15,command=search_data)
search.grid(row=1,column=2)

window.mainloop()