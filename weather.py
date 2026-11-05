import requests

city = input("City: ")

try:
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo = requests.get(geo_url, params={"name": city, "count": 1}, timeout=10).json()

    if "results" not in geo:
        print("City not found.")
    else:
        place = geo["results"][0]
        lat = place["latitude"]
        lon = place["longitude"]

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true",
            "timezone": "auto"
        }
        weather = requests.get(url, params=params, timeout=10).json()["current_weather"]
        print(f"Weather in {place['name']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")

except requests.exceptions.RequestException:
    print("Could not connect. Check your internet and try again.")
