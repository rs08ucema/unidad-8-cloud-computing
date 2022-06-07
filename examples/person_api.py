from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
persons = []


@app.route("/", methods=['GET'])
def dummy_example():
    rsp = {
        'id': 123,
        'name': "Edgard",
        'is_alive': True,
        'favorite_sports': ['cycling', 'tennis', 'swimming'],
        'graduated': None
    }

    return rsp


@app.route("/persons", methods=['POST', 'GET'])
def persons_operations():

    if request.method == 'POST':
        persons.append(request.json)
        return request.json

    elif request.method == 'GET':
        return jsonify(persons)

    else:
        return jsonify([])


