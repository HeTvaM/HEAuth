import sys
import os

from routes.urls import app
from blockchain.block_manager import BlockManager

manager = BlockManager()
manager.init_primary_blocks()

if __name__=="__main__":
    app.run(debug=False, port=8000, host="0.0.0.0")
