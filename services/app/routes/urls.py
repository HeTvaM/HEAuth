import os

from datetime import datetime
from flask import Flask, request
from werkzeug.wrappers.response import Response
from enum import Enum

from tests.debug_loggger import Logger
from routes.addiction import history_table_from, update_app
from blockchain.block_manager import BlockManager

BASEDIR = os.path.dirname(os.path.abspath(__file__))
logger = Logger()
app = Flask(__name__)

ExceptionMessages = {
    0: ("Access allowed", 200),
    1: ("The system did not allow access", 401),
    2: ("POST request heed header Content\type: json", 401)
}


def handler(type):
    message, status = ExceptionMessages[type]

    return Response(
        message,
        status=status
    )


@app.route("/input", methods=['POST'])
def input():
    logger.log("NEW REQUEST")

    return handler(
        update_app(request)
    )


@app.route("/output/<int:db>", methods=['GET'])
def output(db):
    logger.log("SHOW HISTORY")

    return handler(
        0
    ) #history_table_from(db)


@app.route("/restart", methods=['GET'])
def restart():
    logger.log("RESTART")
    pass

    #block_manager.restart(db=True, table=True)

@app.route("/health", methods=['GET'])
def check_health():
    return Responce("", status=200)
