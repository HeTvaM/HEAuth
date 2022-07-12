import os

from flask import Flask, request
from pydantic import BaseModel

from block_manager.main import BlockManager

BASEDIR = os.path.dirname(os.path.abspath(__file__))
block_manager = BlockManager(hash_table={})
app = Flask(__name__)


@app.route("/input", methods=['POST'])
def input():
    return block_manager.new_request()


@app.route("/output", methods=['GET'])
def output():
    return "300"
    # return db.show_history()

if __name__=="__main__":
    app.run(debug=False, port=6200, host="0.0.0.0")
