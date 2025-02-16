from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def transactions_list():
    # group_by = request.args.get('group_by')
    with open('data.json') as f:
        data = json.load(f)
    return data