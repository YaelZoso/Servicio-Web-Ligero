# Import de bibliothèques
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

app.config["DEBUG"] = True

employees = [
    {'id': 0,
	'Nombre': 'Dupont',
	'Funcion': 'Développeur',
	'Antiguedad': '5'}
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Bienvenido</h1>
<p>Hola mundo</p>'''


@app.route('/api/v1/resources/employees/all', methods=['GET'])
def api_all():
    return jsonify(employees)


app.run()