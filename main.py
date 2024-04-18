import os
import requests

def get_weather(latitude, longitude, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    latitude = os.getenv("LAT")
    longitude = os.getenv("LONG")
    api_key = os.getenv("API_KEY")

    if latitude is None or longitude is None or api_key is None:
        raise ValueError("Veuillez configurer la latitude, la longitude et la clé API")
    
    weather_data = get_weather(latitude, longitude, api_key)
    print(weather_data)
