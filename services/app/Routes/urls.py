import os
import logging

from flask import Flask, request
from datetime import datetime

from Manager.block_manager import BlockManager
from main import update_app


root = Flask(__name__)

@root.route("/input", methods=['POST'])
def input():
    return update_app(request)

@root.route("/output", methods=['GET'])
def output():
    return "300"

    # return self.block_manager.history()
    
@root.route("/restart", methods=['GET'])
def restart():
    pass
     
    #block_manager.restart(db=True, table=True)
