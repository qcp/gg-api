from flask import Blueprint, request, jsonify
excel = Blueprint('excel', __name__)

@excel.route('/', methods=['GET', 'POST'])
def excel1():
    return jsonify(args=request.args, json=request.json)