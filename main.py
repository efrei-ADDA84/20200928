import os
import requests

def get_weather(latitude, longitude):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    latitude = float(input("Entrez la latitude du lieu : "))
    longitude = float(input("Entrez la longitude du lieu : "))
    weather_data = get_weather(latitude, longitude)
    print(weather_data)

#https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=aaca89a14b3698bbd46dd966b2fa436d
