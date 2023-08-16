import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the pickled model
model = pickle.load(open("modelV1.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract the features from the JSON data
        age = data['age']
        sex = data['Sex_male']
        cigs_per_day = data['cigsPerDay']
        tot_chol = data['totChol']
        sys_bp = data['sysBP']
        glucose = data['glucose']

        # Make a prediction using the loaded model
        prediction = model.predict([[age, sex, cigs_per_day, tot_chol, sys_bp, glucose]])

        # Convert the prediction to a boolean value (0 or 1) and send the response as JSON
        response = {'prediction': bool(prediction[0])}
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)