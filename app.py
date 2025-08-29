from flask import Flask, render_template, request
from weather_api import get_weather
from run_predictor import get_rain_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST'])
def predict():
    city = request.form['city']
    weather_data = get_weather(city)

    if "error" in weather_data:
        return render_template(
            "result.html",
            city=city,
            weather=None,  # Make sure weather is always defined
            error=weather_data["error"]
        )

    prediction = get_rain_prediction(city, weather_data)
    return render_template(
        "result.html",
        city=city,
        weather=weather_data,
        prediction=prediction,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")