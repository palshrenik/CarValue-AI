from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
from datetime import datetime

app = Flask(__name__)

model = pickle.load(open("model/car_price_model.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        brand = data["brand"]
        model_name = data["model"]
        year = int(data["year"])
        km_driven = float(data["km_driven"])
        seller_type = data["seller_type"]
        fuel_type = data["fuel_type"]
        transmission_type = data["transmission_type"]
        mileage = float(data["mileage"])
        engine = float(data["engine"])
        max_power = float(data["max_power"])
        seats = int(data["seats"])

        vehicle_age = datetime.now().year - year

        car_name = f"{brand} {model_name}"

        input_data = pd.DataFrame({
            "car_name": [car_name],
            "brand": [brand],
            "model": [model_name],
            "vehicle_age": [vehicle_age],
            "km_driven": [km_driven],
            "seller_type": [seller_type],
            "fuel_type": [fuel_type],
            "transmission_type": [transmission_type],
            "mileage": [mileage],
            "engine": [engine],
            "max_power": [max_power],
            "seats": [seats]
        })

        categorical_columns = [
            "car_name",
            "brand",
            "model",
            "seller_type",
            "fuel_type",
            "transmission_type"
        ]

        input_data[categorical_columns] = encoder.transform(
            input_data[categorical_columns]
        )

        prediction = model.predict(input_data)[0]

        return jsonify({
            "success": True,
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)