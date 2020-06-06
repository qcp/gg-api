from flask import Blueprint, request, jsonify

metadata = {
    'name': 'Example auto test',
    'description': 'Description about autotest for inquirer creating user',
    'awailParameters': [{
        'name': 'tt',
        'description': 'tt description'
    }],
    'available': True
}

example = Blueprint('example', __name__)

@example.route('/', methods=['GET'])
def check():
    return jsonify(status='OK', metadata=metadata)

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