import os
import hashlib
import asyncio

from datetime import datetime
from random import sample, randint

from mongodb.connection import Connection
from blocks import ActionBlockModel, BlockModel, SuperBlockModel, BaseBlock
from tests.debug_loggger import Logger
#from monogodb import connection

logger = Logger()

STR_KEY = os.getenv(UNIQUE_KEY, "qwerty")
LOG_STATUS=os.getenv(LOG_STATUS, "User Action")
DB_NAME = os.getenv(DB_NAME, "BLOCKS")

def define_db_name(db_id:int) -> str:
    return "open" if db_id == 0 else "close"

def plugging(func):
    def wrapper(*args, **kwargs):
        cls = args[0]

        cls._del_last_block()
        block, id = func(*args, **kwargs)
        cls._create_last_block(block)

        return block, id
    return wrapper


class BlockManager:
    hash_table = {}
    db = Connection("mongodb://db:27017/", DB_NAME)
    #print("DB", self.db)
    def __init__(self):
        self._last_block_id = None

    def is_token(self, token):
        logger.log("FIND TOKEN")
        return self._find_token(token)

    def new_request(self, token, data):
        if data.get("status") == "open":
            return self._create_token(
                *self._create_block(data)
            )

        return self._create_superblock(token, data)

    def init_primary_blocks(self):
        first_block = BlockModel(**{
            "timestamp": datetime.now(),
            "login": "admin",
            "ip": "0.0.0.0",
            "status": "primary"
        })

        first_block.hash = sample(STR_KEY, randint(0, len(STR_KEY)) )
        id = asyncio.run(self.db.add(
            define_db_name(0),
            first_block.dict()
        ))

    def get_table(self, db):
        dicts = asyncio.run(self.db.show_table(
            define_db_name(db)
        ))
        return dicts

    def _create_superblock(self, token, data):
        open_block = self.db.get_last_block(
            define_db_name(1)
        )
        close_block = BlockModel(**data)
        log_block = ActionBlockModel(data=self.hash_table[token])
        superblock = SuperBlockModel(
            blocks=[open_block, log_block, close_block]
        )

        # open_block = self.db.get_last_block(self.hash_table.get(token))
        # close_block = Block(CLOSE, *data)
        # log_block = Log(ActionBlogModel)
        # Superblock.update(superblock, self.db._open_table)
        # if self.db.close_table_add(superblock)
        
    @plugging
    def _create_block(self, data):
        logger.log(f"CREATE BLOCK \ \nDATA: {data}")

        block = BlockModel(**data)
        BaseBlock.update(
            block,
            asyncio.run(self.db.get_last_block(
                 define_db_name(0)
            ))
        )
        id = asyncio.run(self.db.add(block))
        # Block.update(block, db.prev())
        # id = self.db.add(block)
        return block, id

    def _create_token(self, block, id):
        logger.log(f"CREATE TOKEN \ \nBLOCK: {block.dict()} \nID: {id}")

        key = f"{str(block.dict())}{id} \
                {sample(STR_KEY, randint(0, len(STR_KEY)))}".encode()

        hash_algo = hashlib.sha512()
        hash_algo.update(key)
        token = hash_algo.hexdigest()
        self.hash_table[token] = [id]

        return token

    def _find_token(self, token):
        logger.log(f"TOKEN \ {self.hash_table.get(token)}")
        return not self.hash_table.get(token) is None

    def _log_action(self, token, action):
        return not self.hash_table[token].append(action) is None

    def _create_last_block(self, block):
        last_block = BlockModel(**{
            "timestamp": datetime.now(),
            "login": "admin",
            "ip": "0.0.0.0",
            "status": "primary"
        })

        BaseBlock.update(last_block, block)
        self.last_block_id = self.db.add(last_block)


    def _del_last_block(self):
        try:
            self.db.delete(self._last_block_id)
        except AttributeError:
            return False

        return True
