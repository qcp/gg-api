from flask import Blueprint, request, jsonify
from flask_cors import CORS
simple = Blueprint('simple', __name__)
CORS(simple)

@simple.route('/', methods=['GET'])
def check():    
    return jsonify(status='OK')


@simple.route('/', methods=['POST'])
def calculate():
    settings = request.json['settings']
    examinee = request.json['examinee']
    answer = request.json['answer']
    parameters = request.json['parameters']

    result = {'comment': 'OKIDOKI', 'parameters': []}
    for parameter in parameters:
        result['parameters'].append({'name': parameter['name'], 'value': 1})

    return jsonify(status='OK', decision=result)