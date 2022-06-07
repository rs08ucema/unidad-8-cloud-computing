from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/<user>", methods=['GET'])
def hello_world(user):
    print(request.json)
    print(request.method)
    print(request.args.get('id'))
    print(request.url)
    print(request.data)
    print(user)

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
