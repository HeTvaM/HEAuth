import os
import hashlib

from datetime import datetime
from random import sample, randint

from .block_manager import BlockManager
from db.connection import Connection
from tools.debug_logger import Logger
from tools.helpers import (
    check_block_data,
    get_table_name
)

from tools.config import (
    UNIQUE_KEY,
    CREATE_STATUS,
    CLOSE_STATUS,
    OPEN_TABLE,
    CLOSE_TABLE
)

logger = Logger()


def check_input_data(open_data, close_data):
    return check_block_data(open_data, close_data)

#def check_input_data(open_data, close_data):
#    if not check_block_data(open_data, close_data):
#        return firing_message(message="Close data is false")
#
#    return True

class CoreManager:
    hash_table = {}

    def __init__(self):
        self.db = Connection()
        self.block_manager = BlockManager()

    def define_action(self, token, status, data):
        if CREATE_STATUS == status:
            return self._create_token(
                *self.block_manager.create_block(data, table_id=1)
            )
        elif CLOSE_STATUS == status:
            return self.check_code(
                *self.block_manager.create_block(data, table_id=0)
            )
        else:
            return 410

    def setup_start(self):
        self.block_manager.init_primary_blocks()

    def add_user_action(self, token, action):
        if self._find_token(token):
            return 200 if self._log_action(token, action) else 444

        return 455

    def reset(self, table_id, key=0):
        self.db.reset(
            get_table_name(table_id)
        )
        if key:
            self.db.close_connection()
        else:
            self.block_manager.init_primary_blocks()

        return 200

    def get_table(self, table_id):
        tablename = get_table_name(table_id)
        return self.db.get_table(tablename)

    def _create_token(self, block, id):
        #token = make_hash(block, id)
        token = "111"
        self.hash_table[token] = [id]

        logger.log(f"HASH TABLE - {self.hash_table}")

        return 200, token

    def _create_close_block(self, data, token):
        token_data = self._del_token(token)
        if token_data == 455:
            return actions
        else:
            id = token_data[0]
            actions = token_data[1:]

            token_block_data = self.db.search_by_id(
                get_table_name(0), id
            )

            if not check_input_data(token_block_data, data):
                return 555

            self.block_manager.create_close_block(
                token_block_data, data, CLOSE_STATUS, actions
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
