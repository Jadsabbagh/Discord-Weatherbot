# WeatherBot README

## Introduction
WeatherBot is a simple Python script designed to retrieve and disseminate current weather information for multiple cities using the WeatherAPI and Discord platforms. This README provides a brief overview of the script's functionality, setup instructions, and usage guidelines.

## Features
- Utilizes the WeatherAPI to retrieve current weather data for specified cities.
- Sends weather updates to a designated Discord channel at regular intervals.
- Customizable to include additional cities or adjust update frequency as needed.

## Requirements
- Python 3.x
- [Requests](https://pypi.org/project/requests/) library (`pip install requests`)
- Discord Bot Token
- WeatherAPI Key

## Setup Instructions
1. Obtain a WeatherAPI Key by signing up at [WeatherAPI](https://www.weatherapi.com/).
2. Obtain a Discord Bot Token by creating a bot in the Discord Developer Portal.
3. Clone or download the WeatherBot repository to your local machine.
4. Install the required dependencies by running `pip install requests`.
5. Open the `weatherbot.py` script in a text editor.
6. Replace `"YOUR-WEATHER-API-KEY"` with your WeatherAPI Key.
7. Replace `"YOUR-DISCORD-BOT-TOKEN"` with your Discord Bot Token.
8. Optionally, customize the latitude and longitude of desired cities in the `lat` and `lon` lists.
9. Specify the Discord channel ID (`CHANNEL_ID`) where you want the weather updates to be sent.
10. Save the changes and close the text editor.

## Usage
1. Run the `weatherbot.py` script using the command `python weatherbot.py`.
2. Weather updates for the specified cities will be sent to the designated Discord channel at regular intervals.
3. Monitor the console for status messages indicating successful message delivery or any potential errors.

## Important Notes
- Ensure that your WeatherAPI Key and Discord Bot Token are kept confidential and not shared publicly.
- Customize the script further by adjusting update intervals or adding more cities as required.
- Exercise caution when running the script continuously to avoid exceeding API rate limits or violating Discord's terms of service.

## Contributing
Contributions to Discord WeatherBot are welcome! Feel free to submit bug reports, feature requests, or pull requests through GitHub.

## Acknowledgments
Special thanks to the creators of the WeatherAPI and Discord for providing the tools and platforms necessary for developing WeatherBot.
