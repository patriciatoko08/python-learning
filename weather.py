import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=45.846&longitude=9.007&current_weather=true&timezone=Europe/Zurich"
response = requests.get(url)
data = response.json()

weather = data["current_weather"]
temperature = weather["temperature"]
wind = weather["windspeed"]

print(f"Current temperature: {temperature}°C")
print(f"Current wind speed: {wind} km/h")