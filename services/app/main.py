import sys
import os

from routes.urls import app
<<<<<<< HEAD
=======
from tools.debug_logger import Logger
>>>>>>> 080323757c65fcaa15550fece6a4380d92120e1d
from blockchain.main import CoreManager

logger = Logger()
logger.log(os.environ)

manager = CoreManager()
manager.setup_start()

if __name__=="__main__":
    app.run(debug=False, port=6200, host="0.0.0.0")
