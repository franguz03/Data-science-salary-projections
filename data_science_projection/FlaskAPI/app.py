import flask
from flask import Flask, jsonify, request
import json
from data_input import data
import numpy as np
import pickle

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, "rb") as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        
        data = request.get_json()  
        
        # validate data
        if not data or 'features' not in data:
            return jsonify({'error': 'Faltan datos en la solicitud'}), 400
        
        # convert to np array
        x = np.array(data['features']).reshape(1, -1)

        # load model
        model = load_models()
        prediction = model.predict(x)
        
        # return prediction in json format
        return jsonify({'response': float(prediction[0])}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  

if __name__ == '__main__':
    app.run(debug=True)
