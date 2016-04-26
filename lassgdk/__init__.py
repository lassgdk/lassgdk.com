from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_pyfile("config.py")

@app.route("/")
def index():
    return "hello, world"