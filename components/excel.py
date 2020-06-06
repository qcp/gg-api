from flask import Blueprint, request, jsonify

metadata = {
    'name': 'Excel broken',
    'description': 'Broken test',
    'awailParameters': [{
        'name': 'tt',
        'description': 'tt description'
    }],
    'available': False
}

excel = Blueprint('excel', __name__)

@excel.route('/', methods=['GET'])
def check():
    return jsonify(status='OK', metadata=metadata)