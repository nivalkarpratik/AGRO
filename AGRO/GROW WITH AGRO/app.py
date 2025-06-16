# from flask import Flask,request,render_template
# import numpy as np
# import pandas
# import sklearn
# import pickle
# import requests
# import json






# # importing model
# model = pickle.load(open('model.pkl','rb'))
# sc = pickle.load(open('standscaler.pkl','rb'))
# ms = pickle.load(open('minmaxscaler.pkl','rb'))

# # creating flask app
# app = Flask(__name__,template_folder="Template")


# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods=['POST'])
# def predict():

#     API_KEY = '32187bdcc880be018c7fc27cadbd1411'

# # Replace 'YOUR_CITY' with the name of the city you want to get the weather forecast for
#     # city = request.form['city']
#     city = request.form['city']  

# # Make a request to the OpenWeatherMap API
#     url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
#     response = requests.get(url)

# # Check if the request was successful
#     if response.status_code == 200:
#         data = json.loads(response.text)

#     # # Extract and display the weather forecast for the next 5 days
#     #     for day in data['list'][:5]:
#     #         date = day['dt_txt']
#     #         temperature = day['main']['temp']
#     #         description = day['weather'][0]['description']
#     #         print(f'Date: {date}, Temperature: {temperature}°C, Description: {description}')
#     else:
#         print(f'Failed to retrieve weather data. Status code: {response.status_code}')



#     if city=="beed":
#         N = int(request.form[40])
#         P = int(request.form[50])
#         K = int(request.form[50])
#         temp = float(request.form[day['main']['temp']])
#         humidity = float(request.form[day['main']['humidity']])
#         ph = int(request.form[100])
#         rainfall = float(request.form[100])

#         feature_list = [N, P, K, temp, humidity, ph, rainfall]
#         single_pred = np.array(feature_list).reshape(1, -1)

#         scaled_features = ms.transform(single_pred)
#         final_features = sc.transform(scaled_features)
#         prediction = model.predict(final_features)

#         crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

#     if prediction[0] in crop_dict:
#         crop = crop_dict[prediction[0]]
#         result = "{} is the best crop to be cultivated right there".format(crop)
#     else:
#         result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
#     return render_template('index.html',result = result)




# # python main
# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, render_template
# import numpy as np
# import pickle
# import requests
# import json
# import webbrowser
# import webview

# # Load the machine learning model and scalers
# model = pickle.load(open('model.pkl', 'rb'))
# sc = pickle.load(open('standscaler.pkl', 'rb'))
# ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# # Create a Flask app
# app = Flask(__name__, template_folder="Template")

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods=['POST'])
# def predict():
#     # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
#     API_KEY = '32187bdcc880be018c7fc27cadbd1411'
#     city = request.form['city']

#     # Make a request to the OpenWeatherMap API
#     url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = json.loads(response.text)


#      # Check if the request was successful
# #     if response.status_code == 200:
# #         data = json.loads(response.text)

# #     # # Extract and display the weather forecast for the next 5 days
#         for day in data['list'][:5]:
#             date = day['dt_txt']
#             temperature = day['main']['temp']
#             description = day['weather'][0]['description']
#             print(f'Date: {date}, Temperature: {temperature}°C, Description: {description}')
# #     else:


#         if city == "beed":
#             # N = float(request.form['N'])
#             # P = float(request.form['P'])
#             # K = float(request.form['K'])
#             # temp = float(data['list'][0]['main']['temp'])
#             # humidity = float(data['list'][0]['main']['humidity'])
#             # ph = float(request.form['ph'])
#             # rainfall = float(request.form['rainfall'])

#             N = 40
#             P = 50
#             K = 50
#             temp = day['main']['temp']
#             humidity = day['main']['humidity']
#             ph = 100
#             rainfall = 100

#             feature_list = [N, P, K, temp, humidity, ph, rainfall]
#             single_pred = np.array(feature_list).reshape(1, -1)

#             scaled_features = ms.transform(single_pred)
#             final_features = sc.transform(scaled_features)
#             prediction = model.predict(final_features)

#             crop_dict = {
#                 1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
#                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
#                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
#                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
#             }

#             # if prediction[0] in crop_dict:
#             #     crop = crop_dict[prediction[0]]
#             #     result = f"{crop} is the best crop to be cultivated right there"

#             # if result == "Pigeonpeas":
#             #         webbrowser.open("http://127.0.0.1:5502/Template/weather.html")
#             # return render_template('index.html', city=city, result=result)
#             if prediction[0] in crop_dict:
#                 crop = crop_dict[prediction[0]]
#                 result = f"{crop} is the best crop to be cultivated right there"
#                 if result == "Pigeonpeas":
#                     webbrowser.open("http://127.0.0.1:5502/Template/weather.html")

#                 return render_template('index.html', city=city, result=result)



#             else:
#                 result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
#             return render_template('index.html', result=result)
#         else:
#             return render_template('index.html', result="City not recognized.")
#     else:
#         return render_template('index.html', result="Failed to retrieve weather data.")

# if __name__ == "__main__":
#     app.run(debug=True)
















from flask import Flask, request, render_template
import numpy as np
import pickle
import requests
import json
import webbrowser
import webview

# Load the machine learning model and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Create a Flask app
app = Flask(__name__, template_folder="Template")

@app.route('/')
def index():
    return render_template("ind.html")

@app.route("/predict", methods=['POST'])
def predict():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    API_KEY = '32187bdcc880be018c7fc27cadbd1411'
    city = request.form['city']

    # Make a request to the OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)

        # Extract and display the weather forecast for the next 5 days
        for day in data['list'][:5]:
            date = day['dt_txt']
            temperature = day['main']['temp']
            description = day['weather'][0]['description']
            print(f'Date: {date}, Temperature: {temperature}°C, Description: {description}')

        if city == "beed":
            N = 40
            P = 50
            K = 50
            temp = day['main']['temp']
            humidity = day['main']['humidity']
            ph = 100
            rainfall = 100

            feature_list = [N, P, K, temp, humidity, ph, rainfall]
            single_pred = np.array(feature_list).reshape(1, -1)

            scaled_features = ms.transform(single_pred)
            final_features = sc.transform(scaled_features)
            prediction = model.predict(final_features)

            crop_dict = {
                1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
            }

            if prediction[0] in crop_dict:
                crop = crop_dict[prediction[0]]
                result = f"{crop} is the best crop to be cultivated right there"
                if result == "Muskmelon":
                    def openURL():
                        webview.create_window("Open URL Example", "weather.html")


                    
            else:
                result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
            return render_template('ind.html', result=result)
        else:
            return render_template('ind.html', result="City not recognized.")
    else:
        return render_template('ind.html', result="Failed to retrieve weather data.")

if __name__ == "__main__":
    app.run(debug=True)
    openURL()
    webview.start()

