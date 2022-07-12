import os

from flask import Flask, request
from pydantic import BaseModel
from datetime import datetime

#from block_manager.main import BlockManager

BASEDIR = os.path.dirname(os.path.abspath(__file__))
#block_manager = BlockManager(hash_table={})
app = Flask(__name__)

ARGS_FOR_BLOCK = ["status", "@timestamp", "login", "ip"]

def create_dict_from(data):
    # for arg in ARGS_FOR_BLOCK:
    #    lst = request.arg(arg)
    #    
    dictionary = {"@timestamp": datetime.now()}
    temp = data[1:-1].replace(":", ", ").split(", ")

    for key, value in zip(temp[::2], temp[1::2]):
        dictionary[key] = value

    return dictionary


@app.route("/input", methods=['POST'])
def input():
    data = create_dict_from(request.get_data(as_text=True))
    status = data["status"]
    print(data)
    try:
        if data["token"]:
            print(data["token"])
            #block_manager.check_token(data["token"])
        if data["token"] and status:
            print("Close")
            #block_manager.last_request(data, token)
            #block_manager.new_request(data)
    except KeyError:
        pass
        #block_manager.new_request(data)
    return data #block_manager.new_request()


@app.route("/output", methods=['GET'])
def output():
    return "300"
    # return db.show_history()

if __name__=="__main__":
    app.run(debug=False, port=6200, host="0.0.0.0")
