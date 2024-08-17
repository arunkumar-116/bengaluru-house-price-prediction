from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

# Load feature names
X_columns = joblib.load('feature_names.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define the prediction function
def predict_price(location, sqft, bath, bhk):
    # Ensure location is in the model's feature list
    loc_index = np.where(X_columns == location)[0]
    if len(loc_index) == 0:
        return "Location not found in model features"
    loc_index = loc_index[0]

    # Create a feature vector for the input
    x = np.zeros(len(X_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Make prediction
    predicted_price = model.predict([x])[0]

    # Format the price to 3 decimal places
    return f"{predicted_price:.3f}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        location = request.form.get('location')
        sqft = float(request.form.get('sqft'))
        bath = float(request.form.get('bath'))
        bhk = int(request.form.get('bhk'))

        # Predict the price
        price = predict_price(location, sqft, bath, bhk)
        return jsonify({'prediction_text': f'Predicted Price in Lakhs: {price}'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
