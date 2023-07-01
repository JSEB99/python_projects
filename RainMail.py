import requests
import smtplib

my_email = "YOUREMAIL"
password = "YOUREMAILAPPPASS"
api_key = "YOURAPIKEY" #Onecall 3.0

parameters = {
    'lat':45.463620,
    'lon':9.188120,
    'appid':api_key,
    'exclude':'current,minutely,daily'
}

url = "https://api.openweathermap.org/data/3.0/onecall"
umbrellastr = '☔'
umbrella = umbrellastr.encode('ascii', 'ignore').decode('ascii')
response = requests.get(url=url,params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
weather_hourly = data['hourly']
count = 0
next_12h = [weather_hourly[hour]['weather'][0]['id'] for hour in range(len(weather_hourly)) if hour<12]
print(next_12h)
for id in next_12h:
    if id<700:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() #Encrypted the message
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='EMAILTOSEND',
                msg=f"Subject:IT's going to rain!\n\n'Remember to bring your Umbrella'")
        break
