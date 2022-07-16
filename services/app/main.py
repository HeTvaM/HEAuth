import sys
import os

from Routes.urls import root

BASEDIR = os.path.dirname(os.path.abspath(__file__))

if __name__=="__main__":
    root.run(debug=True, port=6200, host="0.0.0.0")