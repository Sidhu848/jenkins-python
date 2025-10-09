from flask import Flask, jsonify
import requests


app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_response = requests.get(geo_url)
    
    if geo_response.status_code != 200 or not geo_response.json().get("results"):
        return jsonify({"error": "City not found"}), 404

    location = geo_response.json()["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    weather_response = requests.get(weather_url)
    if weather_response.status_code == 200:
        weather = weather_response.json()["current_weather"]
        return jsonify({
            "city": city,
            "temperature": weather["temperature"],
            "wind_speed": weather["windspeed"]
        })
    else:
        return jsonify({"error": "Weather data not available"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
