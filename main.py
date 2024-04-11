import os
import requests

def get_weather(latitude, longitude):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    latitude = float(os.environ.get("LAT", 0.0))
    longitude = float(os.environ.get("LONG", 0.0))
    weather_data = get_weather(latitude, longitude)
    print(weather_data)

#https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=236df28640d8e0bc71a29bd329f6a8d7

