import requests
import smtplib
from datetime import datetime as dt
import time

MY_LAT = 5.538590 # Your latitude
MY_LONG = -73.366379 # Your longitude
MY_LAT_UP = MY_LAT + 5
MY_LAT_DOWN = MY_LAT - 5
MY_LONG_UP = MY_LONG + 5
MY_LONG_DOWN = MY_LONG - 5
MAIL = "MAIL FROM SEND THE INFO (GMAIL IN THIS CASE)"
DES_MAIL = "MAIL TO SEND THE INFO"
PASS = "PUT AN APP PASSWORD HERE"
def is_iss_overhead():
#If the ISS is close to my current position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT_DOWN<=iss_latitude<=MY_LAT_UP) and (MY_LONG_DOWN<=iss_longitude<=MY_LONG_UP):
        return True
#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
# and it is currently dark
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.now()
    hour = time_now.hour
    if hour>=sunset or hour<=sunrise:
        return True

# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #Encrypted the message
            connection.login(user=MAIL,password=PASS)
            connection.sendmail(
                from_addr=MAIL,
                to_addrs=DES_MAIL,
                msg=f"Subject:Look UP!\n\nThe ISS is Over your head")
# BONUS: run the code every 60 seconds.



