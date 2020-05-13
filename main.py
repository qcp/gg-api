from flask import Flask
from components.excel import excel
from components.simple import simple

app = Flask(__name__)
app.register_blueprint(excel, url_prefix='/excel')
app.register_blueprint(simple, url_prefix='/simple')

@app.route('/', methods=['GET', 'POST'])
def heello_world():
    return 'OK'

if __name__ == '__main__':
    app.run()