import os
import hashlib

from datetime import datetime
from random import sample, randint

from db.connection import Connection
from tools.debug_logger import Logger
from tools.config import UNIQUE_KEY, CREATE_STATUS

logger = Logger()

class CoreManager:
    hash_table = {}
    db = Connection()
    block_manager = BlockManager(db=db)
    #db = Connection("mongodb://db:27017/", DB_NAME)
    #print("DB", self.db

    # Создаёт новый блок или суперблок
    def define_action(self, token, status, data):
        if CREATE_STATUS == status:
            return self._create_token(
                *self.block_manager.create_block(data)
            )

        return self.block_manager.create_superblock(token, data)

    def setup_start(self):
        self.block_manager.init_primary_block()

    def get_table(self, db):
        return self.db.show_table(db=db)

    def check_token(self, token, action):
        if self._find_token(token):
            return self._log_action(token, action)

        return 2

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
