import os

from flask import Flask, request
from werkzeug.wrappers.response import Response

from tools.debug_logger import Logger
from routes.addiction import history_table_from, update_app

BASEDIR = os.path.dirname(os.path.abspath(__file__))
logger = Logger()
app = Flask(__name__)

ExceptionMessages = {
    0: ("Access allowed", 200),
    1: ("The system did not allow access", 401),
    2: ("Wrong Token", 401)
    3: ("POST request required header Content\type: json or request data is None", 401)
    4: ("Unvalid data, system can't create block", 401)
}


def handler(type):
    message, status = ExceptionMessages[type]

    return Response(
        message,
        status=status
    )


@app.route("/input", methods=['POST'])
def input():
    return handler(
        update_app(request)
    )


@app.route("/output/<int:db>", methods=['GET'])
def output(db):
    return handler(
        0
    ) #history_table_from(db)


@app.route("/restart", methods=['GET'])
def restart():
    pass

    #block_manager.restart(db=True, table=True)

@app.route("/health", methods=['GET'])
def check_health():
    return Responce("", status=200)
