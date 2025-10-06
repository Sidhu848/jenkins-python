import requests

def get_weather(city):
    # Geocoding: get latitude & longitude
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_response = requests.get(geo_url)
    
    if geo_response.status_code != 200 or not geo_response.json().get("results"):
        print("City not found.")
        return

    location = geo_response.json()["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]

    # Get current weather
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    weather_response = requests.get(weather_url)
    if weather_response.status_code == 200:
        weather = weather_response.json()["current_weather"]
        temp = weather["temperature"]
        wind = weather["windspeed"]
        print(f"Current weather in {city}: {temp}°C, Wind: {wind} km/h")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather("Hyderabad")
