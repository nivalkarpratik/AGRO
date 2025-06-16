from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__,template_folder="Template")

@app.route('/')
def index():
    return render_template('weather.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city-input')
    api_key = 'YOUR_AP32187bdcc880be018c7fc27cadbd1411I_KEY'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(base_url)
    data = response.json()

    weather = {
        'description': data['weather'][0]['description'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
    }

    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
