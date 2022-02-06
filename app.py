from distutils.log import error
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException
from src.services import restaurants

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_error(e):
    print(e)
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
        return jsonify(error=str(e)), code
    return jsonify(error='something went wrong'), code

@app.route('/restaurants', methods=['GET'])
def find_restaurants():
    print('api call')
    args = request.args
    return restaurants.get_nearby_restaurants(args)
