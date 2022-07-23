import os
import hashlib

from datetime import datetime
from random import sample, randint

from blocks import ActionBlockModel, BlockModel, SuperBlockModel, BaseBlock
from tests.debug_loggger import Logger
#from monogodb import connection

logger = Logger()

try:
    STR_KEY = os.getenv(UNIQUE_KEY)
    LOG_STATUS=os.getenv(LOG_STATUS, "User Action")
    DB_NAME = os.getenv(DB_NAME, "BLOCKS")
except NameError:
    STR_KEY="qwerty"
    LOG_STATUS="User Action"
    DB_NAME = "BLOCKS"


def define_db_name(db_id:int) -> str:
    return "open" if db_id == 0 else "close"


# Функция для создания блока затычки
def plugging(func):
    def wrapper(*args, **kwargs):
        cls = args[0]

        cls._del_last_block()
        block, id = func(*args, **kwargs)
        cls._create_last_block(block)

        return block, id
    return wrapper


class BlockManager:
    def __init__(self, db):
        self.db = db
        self._last_block_id = None

    def init_primary_blocks(self):
        first_block = BlockModel(**{
            "timestamp": datetime.now(),
            "login": "admin",
            "ip": "0.0.0.0",
            "status": "primary"
        })

        first_block.hash = sample(STR_KEY, randint(0, len(STR_KEY)) )

    @plugging
    def create_block(self, data):
        block = BlockModel(**data)
        BaseBlock.update(
            block,
            self.db.get_last_block(db=0)
        )
        id = self.db.add(block)

        return block, id

    def create_superblock(self, token, data):
        open_block = self.db.get_last_block(db=1)

        close_block = BlockModel(**data)
        log_block = ActionBlockModel(data=self.hash_table[token])
        superblock = SuperBlockModel(
            blocks=[open_block, log_block, close_block]
        )


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
