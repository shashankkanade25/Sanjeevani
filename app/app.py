from flask import Flask

app = Flask(__name__)

healthy = True

@app.route("/")
def home():
    return "AI Self-Healing Kubernetes Platform"

@app.route("/health")
def health():
    global healthy

    if healthy:
        return "healthy", 200

    return "unhealthy", 500

@app.route("/fail")
def fail():
    global healthy

    healthy = False

    return "Application marked unhealthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
