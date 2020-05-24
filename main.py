from flask import Flask
from components.excel import excel
from components.example import example

app = Flask(__name__)
app.register_blueprint(excel, url_prefix='/excel')
app.register_blueprint(example, url_prefix='/example')

@app.route('/', methods=['GET', 'POST'])
def heello_world():
    return 'OK'

if __name__ == '__main__':
    app.run()