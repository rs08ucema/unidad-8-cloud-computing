from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def person():

    rsp = {
        'id': 123,
        'name': "Edgard",
        'is_alive': True,
        'favorite_sports': ['cycling', 'tennis', 'swimming'],
        'graduated': None
    }

    return rsp


@app.route("/", methods=['POST'])
def hello_world2():
    print(request.json)
    print(request.method)
    print(request.url)
    print(request.data)

    rsp = {
        'id': 321,
        'name': "Edgard",
        'is_alive': True,
        'favorite_sports': ['cycling', 'tennis', 'swimming'],
        'graduated': None
    }
    return rsp
