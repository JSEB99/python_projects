import requests
from twilio.rest import Client

account_sid = "ACCOUNTID"
auth_token = "YOUR TWILIO AUTH TOKEN :)"

api_key = "YOUR ONECALL 3.0 API KEY :)" #Onecall 3.0

parameters = {
    'lat':45.463620,
    'lon':9.188120,
    'appid':api_key,
    'exclude':'current,minutely,daily'
}

url = "https://api.openweathermap.org/data/3.0/onecall"

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
        client = Client(account_sid,auth_token) 
        message = client.messages.create(
            body="It's going to rain today, remember to bring an umbrella ☔",
            from_="YOUR TWILIO TRIAL NUMBER with country code",
            to="YOUR NUMBER"
            )
        print(message.status)
        break
