import os

from flask import Flask, request
from werkzeug.wrappers.response import Response

from tools.debug_logger import Logger
from routes.addiction import (
    reset_connection,
    history_table_from,
    update_app
)

BASEDIR = os.path.dirname(os.path.abspath(__file__))
logger = Logger()
app = Flask(__name__)

ExceptionMessages = {
    200: ("Access allowed", 200),
    401: ("The system did not allow access", 401),
    410: ("The status is None \ The status is wrong", 401),
    444: ("Logging Error!", 401),
    455: ("Wrong Token", 401),
    456: ("POST request required header Content-type: json or request data is None", 401),
    555: ("Unvalid data, system can't create block", 401),
    503: ("Error in database, Critical lvl. Contact with devops or support", 503)
}


def handler(type):
    logger.log(f"TYPE - {type}")

    try:
        message, status = ExceptionMessages[type]
    except:
        status, message = type

    logger.log(f"HANDLER OUTPUT - {message} = {status}")

    return Response(
        str(message),
        status=status
    )

@app.route("/input", methods=['POST'])
def input():
    logger.log("Input")

    return handler(
        update_app(request)
    )

@app.route("/output/<int:db>", methods=['GET'])
def output(db):
    return handler(
        history_table_from()
    )

@app.route("/restart", methods=['GET'])
def restart():
    pass

@app.route("/reset/<int:close>", methods=['GET'])
def reset(close=0):
    return handler(
        reset_connection(close)
    )

@app.route("/health", methods=['GET'])
def check_health():
    return Response("", status=200)
