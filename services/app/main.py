import sys
import os

from routes.urls import app
from blockchain.block_manager import BlockManager

manager = BlockManager()
manager.init_primary_blocks()

if __name__=="__main__":
    app.run(debug=True, port=6200, host="0.0.0.0")
