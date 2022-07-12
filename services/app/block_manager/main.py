import os

from pydantic import BaseModel, Field
from Blocks import Block, SuperBlock
from random import sample, randint
random.sample(population, k)

import hashlib

STR = os.getenv(UNIQUE_KEY)
LOG_STATUS=os.getenv(LOG_STATUS)

class BlockManager(BaseModel):
    hash_algo = hashlib.sha512()
    hash_table: dict
    #db:

    def new_request(self, data, status="open", token=None):
        if token:
            self._find_token(token)
        else:
            return self._create_token(
                self._create_block(data, status)
            )

    def new_action(self, token, action):
        self.hash_table[token].append(action)

    def last_request(self, data, token):
        end_block = Block(status, *data)
        #open_block = self.db.get_open(token)
        #log_block = Block(log_status, )
        #self._create_superblock(end_block, open_block, log_blog)


    def _create_superblock(self, *blocks):


    def _create_block(self, data, status):
        block = Block(status, *data)

        # Block.update(block, db.prev())
        # id = self.db.add(block)

        return block, id

    def _create_token(self, block, id):
        str = f"{''.join(data)}
                {status}
                {sample(STR, randint(len(STR)))}"

        self.hash_algo.update(str)
        token = self.hash_algo.hexdigest()

        self.hash_table[token] = [id]

        return token

    def _check_token(self, token):
        #return self.db.verify(token)
