import requests
import json
import matplotlib.pyplot as plt
import numpy as np

from weatherapi import WeatherPoint as wp

# replace the API key with your WeatherAPI key
key = "YOUR_WEATHER_API_KEY"

#the latitude and longitude of your desired cities
lat = [31.963158, 40.7128, 51.5072]
lon = [35.930359,  74.0060,  0.1276] 

points = [wp(lat[i], lon[i]) for i in range(len(lat))]
for point in points:
    point.set_key(key)

#organize data
temps = []
feels_likes = []
Cities = ["Amman", "New York", "London"]

# get weather data for each city
for p in points:
    p.get_current_weather()
    temps.append(p.temp_c)
    feels_likes.append(p.feelslike_c)

# Plotting the bar graph
x = np.arange(len(Cities))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, temps, width, label='Temperature (°C)')
rects2 = ax.bar(x + width/2, feels_likes, width, label='Feels Like (°C)')

ax.set_xlabel('Cities')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Weather Data')
ax.set_xticks(x)
ax.set_xticklabels(Cities)
ax.legend()

# Save the plot as an image
plt.savefig('weather_data.png')

# Close the plot to avoid displaying it
plt.close()

# Replace these placeholders with your Discord bot token and channel ID
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
CHANNEL_ID = 'YOUR_DISCORD_CHANNEL_ID'

# Endpoint for uploading images to Discord
upload_url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

# Headers for the request
headers = {
    'Authorization': f'Bot {TOKEN}'
}

# Payload containing the image data
files = {
    'file': open('weather_data.png', 'rb')
}

# Send the image to Discord
response = requests.post(upload_url, headers=headers, files=files)

# Check if the image was sent successfully
if response.status_code == 200:
    print('Image sent successfully!')
else:
    print(f'Failed to send image. Status code: {response.status_code}')
