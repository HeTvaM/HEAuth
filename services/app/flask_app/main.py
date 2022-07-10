import os

from flask import Flask, request
from pydantic import BaseModel

BASEDIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route("/input", methods=['GET', 'POST'])
def input():
    return "200"


if __name__=="__main__":
    app.run(debug=False, port=6200, host="0.0.0.0")
