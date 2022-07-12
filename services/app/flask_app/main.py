import os

from flask import Flask, request
from pydantic import BaseModel
from datetime import datetime

#from block_manager.main import BlockManager

BASEDIR = os.path.dirname(os.path.abspath(__file__))
#block_manager = BlockManager(hash_table={})
app = Flask(__name__)

ARGS_FOR_BLOCK = [, "@timestamp", "login", "ip", "token"]

def create_dict_from(data):
    # values = []
    # for arg in ARGS_FOR_BLOCK:
    #    try:
    #        values.append(request.arg(arg))
    #    except:
    #        pass
    # return values
    dictionary = {"@timestamp": datetime.now()}
    temp = data[1:-1].replace(":", ", ").split(", ")

    for key, value in zip(temp[::2], temp[1::2]):
        dictionary[key] = value

    return dictionary


@app.route("/input", methods=['POST'])
def input():
    data = create_dict_from(request.get_data(as_text=True))
    try:
        status = request.arg("status")
        token = request.arg("token")
        return block_manager.new_request(data, status, token)
    except:
        return block_manager.new_request(data)


@app.route("/output", methods=['GET'])
def output():
    return "300"
    # return self.block_manager.history()

if __name__=="__main__":
    app.run(debug=False, port=6200, host="0.0.0.0")
