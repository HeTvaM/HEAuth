import os
import hashlib

from datetime import datetime
from random import sample, randint

<<<<<<< HEAD
from db.connection import Connection
from tools.debug_logger import Logger
from tools.config import UNIQUE_KEY, CREATE_STATUS
=======
from blocks import (
    ActionBlockModel,
    BlockModel,
    SuperBlockModel,
    BaseBlock
)

from tools.debug_logger import Logger
from db.main import Connection


try:
    STR_KEY = os.getenv(UNIQUE_KEY)
    DB_NAME = os.getenv(DB)
    CREATE_STATUS=os.getenv(CREATE)
except NameError:
    STR_KEY="qwerty"
    DB_NAME = "BLOCKS"
    CREATE_STATUS="open"
>>>>>>> 080323757c65fcaa15550fece6a4380d92120e1d

logger = Logger()

class CoreManager:
    hash_table = {}
<<<<<<< HEAD
    db = Connection()
    block_manager = BlockManager(db=db)
=======
>>>>>>> 080323757c65fcaa15550fece6a4380d92120e1d
    #db = Connection("mongodb://db:27017/", DB_NAME)
    #print("DB", self.db

    def __init__(self):
        self.db = Connection()
        self.block_manager = BlockManager(db=db)

    # Создаёт новый блок или суперблок
    def define_action(self, token, status, data):
        if CREATE_STATUS == status:
            return self._create_token(
                *self.block_manager.create_block(data)
            )

        return self.block_manager.create_superblock(token, data)

    def setup_start(self):
        self.block_manager.init_primary_block()

    def check_token(self, token, action):
        if self._find_token(token):
            return self._log_action(token, action)

        return 2

    def get_table(self, db):
        return self.db.get_table(db=db)

    def _create_token(self, block, id):
        key = f"{str(block.dict())}{id} \
                {sample(STR_KEY, randint(0, len(STR_KEY)))}".encode()

        hash_algo = hashlib.sha512()
        hash_algo.update(key)
        token = hash_algo.hexdigest()
        self.hash_table[token] = [id]

        return token

    def _find_token(self, token):
        return not self.hash_table.get(token) is None

    def _log_action(self, token, action):
        time = datetime.now()
        return not self.hash_table[token].append({time:action}) is None
