import os

from datetime import datetime
from flask import Flask, request
from werkzeug.wrappers.response import Response

from tests.debug_loggger import Logger 
from routes.addiction import history_table_from, update_app, tokens
from blockchain.block_manager import BlockManager

BASEDIR = os.path.dirname(os.path.abspath(__file__))
logger = Logger()
app = Flask(__name__)

@app.route("/input", methods=['POST'])
def input():
    logger.log("NEW REQUEST")
    
    if update_app(request):
        return Response("Access allowed", status=200)
    
    return Response("The system did not allow access", status=401)

@app.route("/output/<int:db>", methods=['GET'])
def output(db):
    logger.log("SHOW HISTORY")
    
    if history_table_from(db):
        return Response("Success", status=200)
    
    return Response("Error", status=500)
    
@app.route("/restart", methods=['GET'])
def restart():
    logger.log("RESTART")
    pass
     
    #block_manager.restart(db=True, table=True)

@app.route("/tokens")
def token_table():
    if tokens():
        return Response("", status=200)
    
    return Response("", status=500)