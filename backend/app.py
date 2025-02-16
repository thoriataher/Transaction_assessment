from flask import Flask #, request
import json

app = Flask(__name__)

@app.route("/")
def transactions_list():
    # group_by = request.args.get('group_by')
    with open('data.json') as f:
        data = json.load(f)
    return data