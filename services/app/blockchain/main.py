import os
import hashlib

from datetime import datetime
from random import sample, randint

from .block_manager import BlockManager
from db.connection import Connection
from tools.debug_logger import Logger
from tools.config import (
    UNIQUE_KEY,
    CREATE_STATUS,
    CLOSE_STATUS
)

logger = Logger()

def make_hash(block, id:int):
    hash_algo = hashlib.sha512()

    key = f"{str(block.dict())}{id}"
    key += f"{sample(UNIQUE_KEY, randint(0, len(UNIQUE_KEY)))}"

    hash_algo.update(
        key.encode()
    )

    return hash_algo.hexdigest()

def check_block_data(data, block_data):
    open_block = BlockModel(**data)
    close_block == BlockModel(**block_data)

    if open_block == close_block:
        return True
#    else:
#        firing_message()
#        return False


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
        elif CLOSE_STATUS == status:
            return self._create_close_block(data, status, token)
        else:
            return 410

    def setup_start(self):
        self.block_manager.init_primary_blocks()

    def add_user_action(self, token, action):
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
        token = make_hash(block, id)
        self.hash_table[token] = [id]

        logger.log(f"HASH TABLE - {self.hash_table}")

        return 200, token

    def _create_close_block(self, data, status, token):
        token_data = self._del_token(token)
        if token_data == 455:
            return actions
        else:
            id = token_data[0]
            actions = token_data[1:]

            token_block = self.db.search_by_id(id)

            logger.log(f"ID - {id}, actions - {actions}")
            logger.log(f"ID DATA - {token_block}")

            self.block_manager.create_close_block(
                data, token_block, status, actions
            )
            return 200

    def _find_token(self, token):
        return not self.hash_table.get(token) is None

    def _del_token(self, token):
        if self._find_token(token):
            return self.hash_table.pop(token)

        return 455

    def _log_action(self, token, action):
        time = datetime.now()
        try:
            self.hash_table[token].append({time:action})
        except:
            return False

        return True
