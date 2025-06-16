from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__, template_folder="Template", static_folder="Static")


def index():
    return render_template('index.html', link='http://127.0.0.1:5001/')


# Define crop details
crop_details_data = {
    "Wheat": "Wheat is a cereal grain that is a staple food in many countries.",
    "Rice": "Rice is the seed of the grass species Oryza sativa.",
    # Add more crop details as needed
}

def get_current_season():
    now = datetime.now()
    month = now.month

    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    else:
        return "Winter"

def recommend_crops_seasonal(ph, n, p, k, current_season):
    crop_conditions = {
        "Wheat": {"Spring": (5.5, 7.5, 60, 120, 30, 60, 60, 120)},
        "Rice": {"Atumn": (5, 7, 80, 120, 40, 60, 80, 120)},
        "Corn": {"Summer": (5.8, 7, 120, 180, 60, 90, 120, 180), "Autumn": (5.8, 7.5, 80, 120, 40, 60, 80, 120)},
        "Soybeans": {"Summer": (6, 7.5, 80, 120, 40, 60, 80, 120)},
        "Tomatoes": {"Summer": (6, 7, 120, 180, 60, 90, 120, 180)},
        "Potatoes": {"Winter": (4.8, 6.5, 120, 180, 60, 90, 120, 180)},
        "Barley": {"Spring": (6, 7.5, 60, 120, 30, 60, 60, 120)},
        "Cotton": {"Summer": (5.5, 7, 120, 180, 60, 90, 120, 180)},
        "Coffee": {"Autumn": (6, 6.5, 120, 180, 60, 90, 120, 180)},
        "Sugarcane": {"Summer": (5.5, 6.5, 120, 180, 60, 90, 120, 180)},
        "AppWinter":{"Autumn": (6, 7, 80, 120, 40, 60, 80, 120)},
        "Grapes": {"Summer": (5.5, 7, 80, 120, 40, 60, 80, 120)},
        "Oranges": {"Winter": (6, 7.5, 80, 120, 40, 60, 80, 120)},
        "Bananas": {"Summer": (5.5, 6.5, 120, 180, 60, 90, 120, 180)},
        "Carrots": {"Winter": (5.5, 7, 60, 120, 30, 60, 60, 120)},
        "Onions": {"Winter": (6, 7.5, 60, 120, 30, 60, 60, 120)},
        "Lettuce": {"Winter": (6, 7, 80, 120, 40, 60, 80, 120)},
    
    }

    recommended_crops_seasonal = []

    for crop, season_conditions in crop_conditions.items():
        if current_season in season_conditions:
            conditions = season_conditions[current_season]
            min_ph, max_ph, min_n, max_n, min_p, max_p, min_k, max_k = conditions
            if (
                min_ph <= ph <= max_ph
                and min_n <= n <= max_n
                and min_p <= p <= max_p
                and min_k <= k <= max_k
            ):
                recommended_crops_seasonal.append(crop)

    


    return recommended_crops_seasonal if recommended_crops_seasonal else ["No suitable crops"]

def recommend_crops(ph, n, p, k):
    crop_conditions = {
        "Wheat": (5.5, 7.5, 60, 120, 30, 60, 60, 120),
        "Rice": (5, 7, 80, 120, 40, 60, 80, 120),
        "Corn": (5.8, 7, 120, 180, 60, 90, 120, 180),
        "Soybeans": (6, 7.5, 80, 120, 40, 60, 80, 120),
        "Tomatoes": (6, 7, 120, 180, 60, 90, 120, 180),
        "Potatoes": (4.8, 6.5, 120, 180, 60, 90, 120, 180),
        "Barley": (6, 7.5, 60, 120, 30, 60, 60, 120),
        "Cotton": (5.5, 7, 120, 180, 60, 90, 120, 180),
        "Coffee": (6, 6.5, 120, 180, 60, 90, 120, 180),
        "Sugarcane": (5.5, 6.5, 120, 180, 60, 90, 120, 180),
        "Apples": (6, 7, 80, 120, 40, 60, 80, 120),
        "Grapes": (5.5, 7, 80, 120, 40, 60, 80, 120),
        "Oranges": (6, 7.5, 80, 120, 40, 60, 80, 120),
        "Bananas": (5.5, 6.5, 120, 180, 60, 90, 120, 180),
        "Carrots": (5.5, 7, 60, 120, 30, 60, 60, 120),
        "Onions": (6, 7.5, 60, 120, 30, 60, 60, 120),
        "Lettuce": (6, 7, 80, 120, 40, 60, 80, 120),
        # Add more crops as needed
    }

    recommended_crops = []

    for crop, conditions in crop_conditions.items():
        min_ph, max_ph, min_n, max_n, min_p, max_p, min_k, max_k = conditions
        if (
            min_ph <= ph <= max_ph
            and min_n <= n <= max_n
            and min_p <= p <= max_p
            and min_k <= k <= max_k
        ):
            recommended_crops.append(crop)

    return recommended_crops if recommended_crops else ["No suitable crops"]
@app.route('/')
def index():
    return render_template("w.html", result=None)
    # return render_template("w.html", result_seasonal=None, result_general=None, current_season=current_season, current_month=current_month)

@app.route("/predict", methods=['POST'])
def predict():
    dist = request.form['dist']


    current_season = get_current_season()
    current_month = datetime.now().strftime("%B")



    # Use your logic to get pH, N, P, K values based on the district (dist)
    if dist.lower() == 'beed':
        ph_input, n_input, p_input, k_input = 5.5, 60, 30, 60
    elif dist.lower() == 'akola':
        ph_input, n_input, p_input, k_input = 6, 90, 45, 100
    elif dist.lower() == 'nagpur':
        ph_input, n_input, p_input, k_input = 6.2, 80, 35, 70
    elif dist.lower() == 'nashik':
        ph_input, n_input, p_input, k_input = 5.5, 120, 60, 120
    elif dist.lower() == 'pune':
        ph_input, n_input, p_input, k_input = 5.5, 120, 60, 120          

    recommended_crops_seasonal = recommend_crops_seasonal(ph_input, n_input, p_input, k_input, get_current_season())
    recommended_crops_general = recommend_crops(ph_input, n_input, p_input, k_input)


    print(f"For pH={ph_input}, N={n_input}, P={p_input}, K={k_input} in {dist.capitalize()} during {get_current_season()}: Recommended Seasonal Crops - {', '.join(recommended_crops_seasonal)}")
    print(f"For pH={ph_input}, N={n_input}, P={p_input}, K={k_input} in {dist.capitalize()}: Recommended General Crops - {', '.join(recommended_crops_general)}")


    # return render_template('w.html', result_seasonal=recommended_crops_seasonal, result_general=recommended_crops_general)

    search_result = f"For district {dist.capitalize()}"

    return render_template('w.html', result_seasonal=recommended_crops_seasonal, result_general=recommended_crops_general, current_season=current_season, current_month=current_month,search_result=search_result)

@app.route('/crop_details/<crop_name>')
def crop_details(crop_name):
    # Check if the crop name exists in the crop_details_data dictionary
    crop_description = crop_details_data.get(crop_name, "Details not available for this crop.")
    return render_template('crop_details.html', crop_name=crop_name, crop_description=crop_description)

@app.route('/crop_page/<crop_name>')
def crop_page(crop_name):
    return render_template(f'pages/{crop_name.lower()}.html')

if __name__ == '__main__':
    app.run(debug=True)

















# from flask import Flask, render_template, request
# from datetime import datetime
# import requests

# app = Flask(__name__, template_folder="Template", static_folder="Static")




# # Define crop details
# crop_details_data = {
#     "Wheat": "Wheat is a cereal grain that is a staple food in many countries.",
#     "Rice": "Rice is the seed of the grass species Oryza sativa.",
#     # Add more crop details as needed
# }

# def get_current_season():
#     now = datetime.now()
#     month = now.month

#     if 3 <= month <= 5:
#         return "Spring"
#     elif 6 <= month <= 8:
#         return "Summer"
#     elif 9 <= month <= 11:
#         return "Autumn"
#     else:
#         return "Winter"



# def get_weather_data(api_key, city):
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "appid": api_key,
#         "units": "metric",  # Use "imperial" for Fahrenheit
#     }
#     response = requests.get(base_url, params=params)
#     data = response.json()

#     if response.status_code == 200:
#         temperature = data.get('main', {}).get('temp')
#         humidity = data.get('main', {}).get('humidity')
#         weather_description = data.get('weather', [{}])[0].get('description')

#         return temperature, humidity, weather_description
#     else:
#         print(f"Failed to fetch weather data: {data['message']}")
#         return None, None






# def recommend_crops_seasonal(ph, n, p, k, rainfall, temperature, humidity, current_season):
#     crop_conditions = {
#         "Wheat": {"Spring": (5.5, 7.5, 60, 120, 30, 60, 60, 120, 15, 35)},
#         "Rice": {"Winter": (5, 7, 80, 120, 40, 60, 80, 120, 50, 100)},
#         "Corn": {"Summer": (5.8, 7, 120, 180, 60, 90, 120, 180, 60, 150), "Autumn": (5.8, 7.5, 80, 120, 40, 60, 80, 120, 40, 120)},
#         "Soybeans": {"Summer": (6, 7.5, 80, 120, 40, 60, 80, 120, 40, 80)},
#         "Tomatoes": {"Summer": (6, 7, 120, 180, 60, 90, 120, 180, 50, 120)},
#         "Potatoes": {"Spring": (4.8, 6.5, 120, 180, 60, 90, 120, 180, 30, 80)},
#         "Barley": {"Spring": (6, 7.5, 60, 120, 30, 60, 60, 120, 20, 40)},
#         "Cotton": {"Summer": (5.5, 7, 120, 180, 60, 90, 120, 180, 60, 150)},
#         "Coffee": {"Autumn": (6, 6.5, 120, 180, 60, 90, 120, 180, 30, 80)},
#         "Sugarcane": {"Summer": (5.5, 6.5, 120, 180, 60, 90, 120, 180, 60, 150)},
#         "Apples": {"Autumn": (6, 7, 80, 120, 40, 60, 80, 120, 50, 100)},
#         "Grapes": {"Summer": (5.5, 7, 80, 120, 40, 60, 80, 120, 40, 80)},
#         "Oranges": {"Winter": (6, 7.5, 80, 120, 40, 60, 80, 120, 50, 100)},
#         "Bananas": {"Summer": (5.5, 6.5, 120, 180, 60, 90, 120, 180, 60, 150)},
#         "Carrots": {"Spring": (5.5, 7, 60, 120, 30, 60, 60, 120, 20, 40)},
#         "Onions": {"Autumn": (6, 7.5, 60, 120, 30, 60, 60, 120, 20, 40)},
#         "Lettuce": {"Spring": (6, 7, 80, 120, 40, 60, 80, 120, 30, 80)},
#         # Add more crops and their suitable seasons as needed
#     }

#     recommended_crops_seasonal = []

#     for crop, season_conditions in crop_conditions.items():
#         if current_season in season_conditions:
#             conditions = season_conditions[current_season]
#             min_ph, max_ph, min_n, max_n, min_p, max_p, min_k, max_k, min_rainfall, max_rainfall = conditions
#             if (
#                 min_ph <= ph <= max_ph
#                 and min_n <= n <= max_n
#                 and min_p <= p <= max_p
#                 and min_k <= k <= max_k
#                 and min_rainfall <= rainfall <= max_rainfall
#                 and temperature >= 0  # Adjust the minimum temperature based on the crop's requirement
#                 and humidity >= 0  # Adjust the minimum humidity based on the crop's requirement
#             ):
#                 recommended_crops_seasonal.append(crop)

 
#     return recommended_crops_seasonal if recommended_crops_seasonal else ["No suitable crops"]




# def recommend_crops(ph, n, p, k, rainfall, temperature, humidity):
#     crop_conditions = {
#         "Wheat": (5.5, 7.5, 60, 120, 30, 60, 60, 120, 15, 35),
#         "Rice": (5, 7, 80, 120, 40, 60, 80, 120, 50, 100),
#         "Corn": (5.8, 7, 120, 180, 60, 90, 120, 180, 60, 150),
#         "Soybeans": (6, 7.5, 80, 120, 40, 60, 80, 120, 40, 80),
#         "Tomatoes": (6, 7, 120, 180, 60, 90, 120, 180, 50, 120),
#         "Potatoes": (4.8, 6.5, 120, 180, 60, 90, 120, 180, 30, 80),
#         "Barley": (6, 7.5, 60, 120, 30, 60, 60, 120, 20, 40),
#         "Cotton": (5.5, 7, 120, 180, 60, 90, 120, 180, 60, 150),
#         "Coffee": (6, 6.5, 120, 180, 60, 90, 120, 180, 30, 80),
#         "Sugarcane": (5.5, 6.5, 120, 180, 60, 90, 120, 180, 60, 150),
#         "Apples": (6, 7, 80, 120, 40, 60, 80, 120, 50, 100),
#         "Grapes": (5.5, 7, 80, 120, 40, 60, 80, 120, 40, 80),
#         "Oranges": (6, 7.5, 80, 120, 40, 60, 80, 120, 50, 100),
#         "Bananas": (5.5, 6.5, 120, 180, 60, 90, 120, 180, 60, 150),
#         "Carrots": (5.5, 7, 60, 120, 30, 60, 60, 120, 20, 40),
#         "Onions": (6, 7.5, 60, 120, 30, 60, 60, 120, 20, 40),
#         "Lettuce": (6, 7, 80, 120, 40, 60, 80, 120, 30, 80),
#         # Add more crops and their requirements as needed
#     }

#     recommended_crops = []

#     for crop, conditions in crop_conditions.items():
#         min_ph, max_ph, min_n, max_n, min_p, max_p, min_k, max_k, min_rainfall, max_rainfall = conditions
#         if (
#             min_ph <= ph <= max_ph
#             and min_n <= n <= max_n
#             and min_p <= p <= max_p
#             and min_k <= k <= max_k
#             and min_rainfall <= rainfall <= max_rainfall
#             and temperature >= 0  # Adjust the minimum temperature based on the crop's requirement
#             and humidity >= 0  # Adjust the minimum humidity based on the crop's requirement
#         ):
#             recommended_crops.append(crop)

#     return recommended_crops if recommended_crops else ["No suitable crops"]

# @app.route('/')
# # def index():
# #     return render_template("w.html", result=None)


# @app.route("/predict", methods=['POST'])
# def predict():
#     dist = request.form['dist']


#     api_key = '32187bdcc880be018c7fc27cadbd1411'

#     city = request.form['dist']


#     temperature, humidity, weather_description = get_weather_data(api_key,city)

#     if temperature is None or humidity is None or weather_description is None:
#         # Default values if weather data cannot be fetched
#         temperature, humidity, weather_description = 25, 65, "Clear"




#     current_season = get_current_season()
#     current_month = datetime.now().strftime("%B")

#     # Placeholder for real-time data, replace with actual values from a weather API
#     if dist.lower() == 'beed':
#         ph_input, n_input, p_input, k_input = 5.5, 60, 30, 60
#         temperature, humidity, rainfall = temperature, humidity, 15

#     elif dist.lower() == 'akola':
#         ph_input, n_input, p_input, k_input = 6, 90, 45, 100
#         temperature, humidity, rainfall = temperature, humidity, 20

#     elif dist.lower() == 'nagpur':
#         ph_input, n_input, p_input, k_input = 6.2, 80, 35, 70
#         temperature, humidity, rainfall = 32, 50, 25

#     elif dist.lower() == 'jalna':
#         ph_input, n_input, p_input, k_input = 6.1, 75, 40, 80

#     elif dist.lower() == 'jalgaon':
#         ph_input, n_input, p_input, k_input = 6.0, 85, 42, 90
#         temperature, humidity, rainfall = 29, 62, 17
#     elif dist.lower() == 'satara':
#         ph_input, n_input, p_input, k_input = 5.9, 78, 38, 85
#         temperature, humidity, rainfall = 27, 58, 20

#     elif dist.lower() == 'solapur':
#         ph_input, n_input, p_input, k_input = 6.2, 88, 48, 95
#         temperature, humidity, rainfall = 30, 64, 22

#     elif dist.lower() == 'ahmednagar':
#         ph_input, n_input, p_input, k_input = 5.8, 75, 40, 88
#         temperature, humidity, rainfall = 28, 60, 18

#     elif dist.lower() == 'nashik':
#         ph_input, n_input, p_input, k_input = 6.1, 82, 43, 92
#         temperature, humidity, rainfall = 26, 55, 15

#     elif dist.lower() == 'amravati':
#         ph_input, n_input, p_input, k_input = 6.3, 92, 50, 98
#         temperature, humidity, rainfall = 32, 58, 25

#     elif dist.lower() == 'wardha':
#         ph_input, n_input, p_input, k_input = 6, 120, 60, 120
#         temperature, humidity, rainfall = 50, 120, 10

# # Add more districts as needed
   
# # Add more districts as needed

# # Add more districts as needed
    
#     else:
#         # Default values for unknown district
#         ph_input, n_input, p_input, k_input = 6, 80, 40, 80
#         temperature, humidity, rainfall = 25, 65, 10

#     recommended_crops_seasonal = recommend_crops_seasonal(ph_input, n_input, p_input, k_input, rainfall, temperature, humidity, current_season)
#     recommended_crops_general = recommend_crops(ph_input, n_input, p_input, k_input, rainfall, temperature, humidity)

#     print(f"For pH={ph_input}, N={n_input}, P={p_input}, K={k_input} in {dist.capitalize()} during {get_current_season()}: Recommended Seasonal Crops - {', '.join(recommended_crops_seasonal)}")
#     print(f"For pH={ph_input}, N={n_input}, P={p_input}, K={k_input} in {dist.capitalize()}: Recommended General Crops - {', '.join(recommended_crops_general)}")

#     search_result = f"For district {dist.capitalize()}"

#     return render_template('w.html', result_seasonal=recommended_crops_seasonal, result_general=recommended_crops_general, current_season=current_season, current_month=current_month, search_result=search_result, weather_description=weather_description)

#     # return render_template('w.html', result_seasonal=recommended_crops_seasonal, result_general=recommended_crops_general, current_season=current_season, current_month=current_month, search_result=search_result, weather_description=weather_description)

# @app.route('/crop_details/<crop_name>')
# def crop_details(crop_name):
#     # Check if the crop name exists in the crop_details_data dictionary
#     crop_description = crop_details_data.get(crop_name, "Details not available for this crop.")
#     return render_template('crop_details.html', crop_name=crop_name, crop_description=crop_description)

# @app.route('/crop_page/<crop_name>')
# def crop_page(crop_name):
#     return render_template(f'pages/{crop_name.lower()}.html')

# if __name__ == '__main__':
#     app.run(debug=True)