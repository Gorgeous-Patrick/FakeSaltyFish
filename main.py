from flask import Flask, Response, redirect
import requests
import os

app = Flask(__name__)
serverPath = os.environ.get('SERVER_PATH', 'http://localhost:5000')

def filt(data: str):
    data = data.replace("Salty", "Fake")
    data = data.replace("salty ", "fake ")
    data = data.replace("https://im.salty.fish", serverPath)
    data = data.replace("im.salty.fish", "localhost:5000")
    return data
@app.route("/<path:path>")
def hello_world(path: str):
    if path.endswith(".png") or path.endswith(".jpg"):
        return redirect("https://im.salty.fish/" + path)
    data = requests.get(f"https://im.salty.fish/{path}")
    content_type = data.headers["Content-Type"]
    return Response(filt(data.text), content_type=content_type)

@app.route("/")
def empty():
    data = requests.get("https://im.salty.fish/").text
    return filt(data)
