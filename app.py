
from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    server_time = datetime.now().strftime("%H:%M:%S")
    return render_template("index.html", server_time=server_time)

from flask import jsonify

@app.route("/api/server-time")
def api_server_time():
    now = datetime.now().strftime("%H:%M:%S")
    return jsonify({"server_time": now})

@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True)

