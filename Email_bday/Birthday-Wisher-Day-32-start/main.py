import smtplib
from datetime import datetime as dt
import pandas as pd
from random import choice

data_path = r"""./Email_bday/Birthday-Wisher-Day-32-start/quotes.txt"""
with open(data_path,"r") as quotes:
    file = quotes.read().splitlines()

data_bdays = r"""./Email_bday/Birthday-Wisher-Day-32-start/bday.csv"""
bday = pd.read_csv(data_bdays)

my_email = "yourgmail@gmail.com"
password = "PUT AN APP PASSWORD FOR GMAIL"

today = (dt.now().month,dt.now().day)
bday_dict = {(data_row.month,data_row.day):data_row for (index,data_row) in bday.iterrows()}

letter_path = r"""./Email_bday/Birthday-Wisher-Day-32-start/letter.txt"""

for data in bday_dict:
    if data==today:
        bday_person = bday_dict[today]
        with open(letter_path) as letter:
                edit_letter = letter.read()
        edit_letter = edit_letter.replace("[NAME]",bday_person["name"])
        letter_edited = edit_letter.replace("[QUOTE]",choice(file))
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #Encrypted the message
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_edited}")


