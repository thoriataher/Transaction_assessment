from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def transactions_list():
    with open('data.json') as f:
        data = json.load(f)
    return data