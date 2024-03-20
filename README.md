# WeatherBot README

## Introduction
WeatherBot is a Python script designed to retrieve and disseminate current weather information for multiple cities using the WeatherAPI and Discord platforms. This README provides an overview of two variations of the script: one that sends textual weather updates and another that sends graphical representations of the weather data.

## Features
- Utilizes the WeatherAPI to retrieve current weather data for specified cities.
- Sends weather updates to a designated Discord channel.
- Provides options for both textual and graphical representations of weather data.

## Requirements
- Python 3.x
- [Requests](https://pypi.org/project/requests/) library (`pip install requests`)
- Discord Bot Token
- WeatherAPI Key
- [Matplotlib](https://pypi.org/project/matplotlib/) library (`pip install matplotlib`)

## Setup Instructions
1. Obtain a WeatherAPI Key by signing up at [WeatherAPI](https://www.weatherapi.com/).
2. Obtain a Discord Bot Token by creating a bot in the Discord Developer Portal.
3. Clone or download the WeatherBot repository to your local machine.
4. Install the required dependencies by running `pip install requests matplotlib`.
5. Open the desired script (`weatherbot_text.py` for textual updates or `weatherbot_graph.py` for graphical updates) in a text editor.
6. Replace `"YOUR-WEATHER-API-KEY"` with your WeatherAPI Key.
7. Replace `"YOUR-DISCORD-BOT-TOKEN"` with your Discord Bot Token.
8. Customize the latitude and longitude of desired cities in the `lat` and `lon` lists.
9. Specify the Discord channel ID (`CHANNEL_ID`) where you want the weather updates to be sent.
10. Save the changes and close the text editor.

## Usage
### Textual Weather Updates
1. Run the `weatherbot_text.py` script using the command `python weatherbot_text.py`.
2. Weather updates for the specified cities will be sent to the designated Discord channel at regular intervals.

### Graphical Weather Updates
1. Run the `weatherbot_graph.py` script using the command `python weatherbot_graph.py`.
2. A bar graph visualizing the temperature and "feels like" temperature for the specified cities will be sent to the designated Discord channel.
![Screenshot](https://github.com/Jadsabbagh/Discord-Weatherbot/blob/main/Screenshot.png)


## Important Notes
- Ensure that your WeatherAPI Key and Discord Bot Token are kept confidential and not shared publicly.
- Customize the scripts further by adjusting update intervals, adding more cities, or modifying the graphical representation as required.
- Exercise caution when running the scripts continuously to avoid exceeding API rate limits or violating Discord's terms of service.

## Contributing
Contributions to WeatherBot are welcome! Feel free to submit bug reports, feature requests, or pull requests through GitHub.

## Acknowledgments
Special thanks to the creators of the WeatherAPI and Discord for providing the tools and platforms necessary for developing WeatherBot.
