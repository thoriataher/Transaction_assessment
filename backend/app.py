from flask import Flask, jsonify
from flask_cors import CORS
from routes.transaction_routes import transaction_bp 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(transaction_bp, url_prefix="/")

# @app.route("/")
# def transactions_list():
#     # group_by = request.args.get('group_by')
#     with open('data.json') as f:
#         data = json.load(f)
#     return data
