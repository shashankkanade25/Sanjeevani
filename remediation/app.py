from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Remediation Service Running"

@app.route("/webhook", methods=["POST"])
def webhook():

    payload = request.json

    print("=" * 60)
    print("ALERT RECEIVED")
    print(json.dumps(payload, indent=2))
    print("=" * 60)

    alerts = payload.get("alerts", [])

    for alert in alerts:

        name = alert.get("labels", {}).get("alertname")

        print(f"Processing alert: {name}")

    return {"status": "received"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
