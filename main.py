from flask import Flask
import requests

app = Flask(__name__)

def filt(data: str):
    data = data.replace("Salty", "Fake")
    data = data.replace("salty ", "fake ")
    return data
@app.route("/<path:path>")
def hello_world(path: str):
    data = requests.get(f"https://im.salty.fish/{path}").text
    return filt(data)

@app.route("/")
def empty():
    data = requests.get("https://im.salty.fish/").text
    return filt(data)
