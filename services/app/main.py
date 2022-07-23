import sys
import os

from routes.urls import app
from blockchain.main import CoreManager

manager = CoreManager()
manager.setup_start()

if __name__=="__main__":
    app.run(debug=True, port=6200, host="0.0.0.0")
