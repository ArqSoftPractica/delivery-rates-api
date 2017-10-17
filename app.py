#!flask/bin/python
from flask import Flask, jsonify
import area
from datetime import datetime

app = Flask(__name__)

area.load()


@app.route('/', methods=['GET'])
def index():
    return jsonify({'ok': True}), 200


@app.route('/areas', methods=['GET'])
def areas():
    return jsonify([e.serialize() for e in area.list]), 200


@app.route('/cost', methods=['GET'])
def cost():
    return jsonify({'cost': base_cost()}), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405


def base_cost():
    now = datetime.now()
    magic_factor = float(now.day % 10 + now.hour)
    return magic_factor


if __name__ == '__main__':
    app.run(debug=True)
