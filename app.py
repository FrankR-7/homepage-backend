from flask import Flask, jsonify
from flask_cors import CORS, cross-origin
import json

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
  with open("projects.json") as stream:
    data = json.load(stream)
  return jsonify(data)

if __name__ == "__main__":
 # Run the app until stopped
 app.run()