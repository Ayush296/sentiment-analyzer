from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'GVJcC6C2bL0BGsktocAoyujmH7GcJ1uQFBSeO6fnYvsrLFwziDx6JQQJ99BDACGhslBXJ3w3AAAaACOGPlss'
ENDPOINT = 'https://ta1452.cognitiveservices.azure.com/' + "/text/analytics/v3.1/sentiment"

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form["text"]
        headers = {"Ocp-Apim-Subscription-Key": API_KEY}
        data = {"documents": [{"id": "1", "language": "en", "text": text}]}
        response = requests.post(ENDPOINT, headers=headers, json=data)
        sentiment = response.json()["documents"][0]["sentiment"]
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)