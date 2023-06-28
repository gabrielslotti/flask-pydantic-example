from flask import Flask, jsonify
import os

app = Flask(__name__)
app.config.from_object('config')

app.route('/', methods=['GET'])
def index():
    return jsonify(status='ok'), 200

if __name__ == '__main__':
    app.run()