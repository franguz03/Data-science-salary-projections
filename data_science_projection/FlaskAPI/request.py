import requests
from data_input import data

url = "http://127.0.0.1:5000/predict"
to_predict = {"features": data}

res = requests.get(url, json=to_predict)
print(res.json())  # {'response': 53.01}
