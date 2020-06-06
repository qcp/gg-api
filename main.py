import os
from flask import Flask, jsonify
from flask_cors import CORS
import importlib

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': [os.environ.get('FRONT_ENDPOINT')]}})

library = []

for module in [x for x in os.listdir('components') if x.endswith(".py")]:
    pkg_name = module[0:-3]
    pkg = importlib.import_module('components.'+pkg_name)
    app.register_blueprint(getattr(pkg, pkg_name), url_prefix='/'+pkg_name)
    library.append({
        'module': pkg_name,
        'available': pkg.metadata['available'],
        'name': pkg.metadata['name'],
        'description': pkg.metadata['description']            
    })
    print('Blueprint module "'+ pkg_name + '" imported')

@app.route('/', methods=['GET'])
def get_main():
    return 'OK'

@app.errorhandler(404)
def page_not_found(e):
    return 'NOK', 404

@app.route('/library', methods=['GET'])
def get_library():
    return jsonify(status='OK', library=library)

if __name__ == '__main__':
    app.run()