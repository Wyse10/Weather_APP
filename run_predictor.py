import requests

def get_rain_prediction(city, weather_data):
    system_prompt = "You are a helpful AI assistant that predicts if it will rain."
    query = f"""
    Weather data for {city}:
    - Temperature: {weather_data['temperature']} °C
    - Humidity: {weather_data['humidity']} %
    - Wind Speed: {weather_data['wind_speed']} m/s
    - Condition: {weather_data['condition']}

    Based on this info:
    - Will it rain today in {city}?
    - Answer 'Yes, it will rain' or 'No, it will not rain' with explanation.
    """

    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()  # raise error if request failed
    data = response.json()
    
    # Ollama chat responses are in 'message' or 'messages' depending on version
    return data.get("message", {}).get("content", "")
