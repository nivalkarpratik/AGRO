from flask import Flask, render_template, request

app = Flask(__name__, template_folder="Template", static_folder="Static")

# Define crop details
crop_details_data = {
    "Wheat": "Wheat is a cereal grain that is a staple food in many countries.",
    "Rice": "Rice is the seed of the grass species Oryza sativa.",
    # Add more crop details as needed
}

# ... (your existing code)





def recommend_crops(ph, n, p, k):
    # Your existing crop recommendation logic
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
        if (min_ph <= ph <= max_ph) and (min_n <= n <= max_n) and (min_p <= p <= max_p) and (min_k <= k <= max_k):
            recommended_crops.append(crop)

    return recommended_crops if recommended_crops else ["No suitable crops"]
    # ...






@app.route('/')
def index():
    return render_template("home.html", result=None)

@app.route("/predict", methods=['POST'])
def predict():
    dist = request.form['dist']

    # Use your logic to get pH, N, P, K values based on the district (dist)
    if dist.lower() == 'beed':
        ph_input, n_input, p_input, k_input = 5.5, 60, 30, 60
    elif dist.lower() == 'akola':
        ph_input, n_input, p_input, k_input = 6, 90, 45, 100
    elif dist.lower() == 'nagpur':
        ph_input, n_input, p_input, k_input = 6.2, 80, 35, 70

    recommended_crops = recommend_crops(ph_input, n_input, p_input, k_input)

    print(f"For pH={ph_input}, N={n_input}, P={p_input}, K={k_input} in {dist.capitalize()}: Recommended Crops - {', '.join(recommended_crops)}")

    return render_template('home.html', result=', '.join(recommended_crops))

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
