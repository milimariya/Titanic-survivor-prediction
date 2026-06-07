from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load("titanic_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_form", methods=["POST"])
def predict_form():

    pclass = int(request.form["Pclass"])
    sex = int(request.form["Sex"])
    age = float(request.form["Age"])
    fare = float(request.form["Fare"])

    passenger = [[pclass, sex, age, fare]]

    prediction = model.predict(passenger)

    if prediction[0] == 1:
        result = "Survived"
    else:
        result = "Did Not Survive"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)