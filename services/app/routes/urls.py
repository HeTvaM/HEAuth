import os

from datetime import datetime
from flask import Flask, request
from werkzeug.wrappers.response import Response
from enum import Enum

from tools.debug_logger import Logger
from routes.addiction import history_table_from, update_app
from blockchain.block_manager import BlockManager

BASEDIR = os.path.dirname(os.path.abspath(__file__))
logger = Logger()
app = Flask(__name__)

ExceptionMessages = {
    200: ("Access allowed", 200),
    401: ("The system did not allow access", 401),
    455: ("Wrong Token", 401),
    456: ("POST request required header Content\type: json or request data is None", 401),
    555: ("Unvalid data, system can't create block", 401),
    503: ("Error in database, Critical lvl. Contact with devops or support", 503)
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
        200
    ) #history_table_from(db)


@app.route("/restart", methods=['GET'])
def restart():
    pass

    #block_manager.restart(db=True, table=True)

@app.route("/health", methods=['GET'])
def check_health():
    return Responce("", status=200)
