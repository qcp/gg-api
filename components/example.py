from flask import Blueprint, request, jsonify
from flask_cors import CORS
example = Blueprint('example', __name__)
CORS(example)

@example.route('/', methods=['GET'])
def check():    
    name = 'Example auto test'
    description = 'Description about autotest for inquirer creating user'

    awailParameters = []
    awailParameters.append({'name': 'tt', 'description': 'tt description'})

    return jsonify(status='OK', metadata={'name': name, 'description': description, 'available':True})


@example.route('/', methods=['POST'])
def calculate():
    settings = request.json['settings']
    examinee = request.json['examinee']
    answer = request.json['answer']
    parameters = request.json['parameters']

    result = {'comment': 'Auto test comment', 'parameters': []}
    for parameter in parameters:
        result['parameters'].append({'name': parameter['name'], 'value': 1})

    return jsonify(status='OK', decision=result)