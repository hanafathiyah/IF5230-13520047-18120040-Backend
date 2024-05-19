import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from praktikum.chatbot import findAnswer

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

@app.route('/members',  methods=['GET'])
def members():
  return jsonify({"members": ["Member1", "Member2", "Member3"]})

@app.route('/chatbot_regex', methods=['POST'])
def handle_chatbot_regex_post():
  question =  json.loads(request.data)
  return jsonify(findAnswer(str(question)))

if __name__ == "__main__":
  app.run(debug=True)