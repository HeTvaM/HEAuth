import os
import hashlib

from datetime import datetime
from random import sample, randint

from .block_manager import BlockManager
from db.connection import Connection
from tools.debug_logger import Logger
from tools.config import UNIQUE_KEY, CREATE_STATUS

logger = Logger()

class CoreManager:
    hash_table = {}

    def __init__(self):
        self.db = Connection()
        self.block_manager = BlockManager()

    def define_action(self, token, status, data):
        if CREATE_STATUS == status:
            return self._create_token(
                *self.block_manager.create_block(data)
            )

        return self.block_manager.create_superblock(token, data)

    def setup_start(self):
        self.block_manager.init_primary_blocks()

    def check_token(self, token, action):
        if self._find_token(token):
            return 200 if self._log_action(token, action) else 444

        return 455

    def reset(self, key=0):
        self.db.reset()
        if key:
            self.db.close_connection()
        else:
            self.block_manager.init_primary_blocks()

        return 200

    def get_table(self):
        return self.db.get_table()

    def _create_token(self, block, id):
        key = f"{str(block.dict())}{id} \
                {sample(UNIQUE_KEY, randint(0, len(UNIQUE_KEY)))}".encode()

        hash_algo = hashlib.sha512()
        hash_algo.update(key)
        token = hash_algo.hexdigest()
        self.hash_table[token] = [id]

        return 200, token

    def _find_token(self, token):
        return not self.hash_table.get(token) is None

    def _log_action(self, token, action):
        time = datetime.now()
        return not self.hash_table[token].append({time:action}) is None
