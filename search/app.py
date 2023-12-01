from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/image")
def image():
    return render_template("/image.html")

@app.route("/advanced")
def advanced():
    return render_template("/advanced.html")

