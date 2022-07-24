import sys
import os

from routes.urls import app
from setting.setup import set_settings
from blockchain.main import CoreManager

manager = CoreManager()
manager.setup_start()

set_settings(
   username=,
   password=,
   db_name=,
   names_table=[]
)

if __name__=="__main__":
    app.run(debug=False, port=6200, host="0.0.0.0")
