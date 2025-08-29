import ollama 

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

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
    )
    return response["message"]["content"]
