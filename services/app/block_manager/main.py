import os
import hashlib

from pydantic import BaseModel, Field
from Blocks import Block, SuperBlock
from random import sample, randint
from db.connection import Connection

STR_KEY = os.getenv(UNIQUE_KEY)
LOG_STATUS=os.getenv(LOG_STATUS)

class BlockManager(BaseModel):
    hash_algo = hashlib.sha512()
    hash_table: dict
    db: Optional[Connection] = Connection('mongodb://localhost:27017/', 'blocks')

    def new_request(self, data, status="open", token=None):
        if token:
            return self._find_token(token)
        if status=="close":
            return self._create_superblock(token, data)
        else:
            return self._create_token(
                self._create_block(data, status)
            )

    def _create_superblock(self, token, data):
        # open_block = self.db.get_last_block(self.hash_table.get(token))
        # close_block = Block(CLOSE, *data)
        # log_block = Log(ActionBlogModel)
        superblock = SuperBlock(*blocks)
        # Superblock.update(superblock, self.db._open_table)
        # if self.db.close_table_add(superblock)

    def _create_block(self, data, status):
        block = Block(status, *data)
        # Block.update(block, db.prev())
        # id = self.db.add(block)
        return block, id

    def _create_token(self, block, id):
        str = f"{''.join(data)}{status}
                {sample(STR_KEY, randint(len(STR_KEY)))}"

        self.hash_algo.update(str)
        token = self.hash_algo.hexdigest()
        self.hash_table[token] = [id]

        return token

    def _find_token(self, token):
        return self.hash_table.get(token) is None

    def _log_action(self, token, action):
        return self.hash_table[token].append(action) is None
