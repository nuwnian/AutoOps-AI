from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    return f"Hello from Mini Azure App!<br>Current server time: {now}"
@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True)

