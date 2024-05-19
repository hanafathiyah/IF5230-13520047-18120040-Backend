import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from praktikum.classification import json_telco
from praktikum.classification import get_confusion_matrix_LR
from praktikum.chatbot import findAnswer

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

@app.route('/chatbot_regex', methods=['POST'])
def handle_chatbot_regex_post():
  question =  json.loads(request.data)
  return jsonify(findAnswer(str(question)))

@app.route('/telco', methods=['GET'])
def get_json_telco():
  return jsonify(json_telco())

if __name__ == "__main__":
  app.run(debug=True)