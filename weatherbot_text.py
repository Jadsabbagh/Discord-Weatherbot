import requests
import json

from weatherapi import WeatherPoint as wp

key = "YOUR-WEATHER-API-KEY"

#you can customize the latitude and longtitude of your desired cities
lat = [31.963158, 40.7128, 51.5072]
lon = [35.930359,  74.0060,  0.1276] 

point = wp(lat[0], lon[0])
point.set_key(key)

point2 = wp(lat[1],lon[1])
point2.set_key(key)

point3 = wp(lat[2],lon[2])
point3.set_key(key)



points = [point, point2, point3]
temps = []
conditions = []
feels_likes = []
Cities = ["Amman", "New York", "London"]

#getting data
for p in points:
    p.get_current_weather()
    temps.append(p.temp_c)
    conditions.append(p.condition)
    feels_likes.append(p.feelslike_c)

#creating the message
message = ""
for city, temp, condition in zip(Cities, temps, conditions):
    message += f"{city}: {temp}C, {condition}. "


TOKEN = 'YOUR-DISCORD-BOT-TOKEN'
CHANNEL_ID = 'CHANNEL-ID'



#endpoint
url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

# JSON payload for  message
payload = {
    'content': message
}


headers = {
    'Authorization': f'Bot {TOKEN}',
    'Content-Type': 'application/json'
}



while True:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # check if message was sent
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print(f'Failed to send message. Status code: {response.status_code}')
    break
