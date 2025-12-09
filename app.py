from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock prediction function
def get_mock_prediction(player_name):
    # Replace this with your actual predictive model logic
    return {
        "player": player_name.title(),
        "yards": round(len(player_name) * 42.3, 1),
        "receptions": round(len(player_name) * 0.7, 1),
        "touchdowns": round(len(player_name) * 0.2, 1),
        "confidence": 75  # Example confidence score
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    player = request.form.get("player")
    prediction = get_mock_prediction(player)
    return render_template("predictions.html", prediction=prediction)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    player = request.json.get("player")
    prediction = get_mock_prediction(player)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
