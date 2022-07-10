import os

from pydantic import BaseModel, Field
from Blocks import Block, SuperBlock
from random import sample, randint
random.sample(population, k)

import hashlib

STR = os.getenv(unique_key)

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

    def _create_block(self, data, status):
        block = Block(status, *data)

        # Block.update(block, db.prev())
        # id = db.add(block)

        return block, id

    def _create_token(self, block, id):
        str = f"{''.join(data)}
                {status}
                {sample(STR, randint(len(STR)))}"

        self.hash_algo.update(str)
        token = self.hash_algo.hexdigest()

        self.hash_table[token] = id

        return token
