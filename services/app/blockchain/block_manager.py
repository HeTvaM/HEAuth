import os

from datetime import datetime, timezone
from random import sample, randint

from blocks import (
    ActionBlockModel,
    BlockModel,
    CloseBlockModel,
    BaseBlock
)

from tools.debug_logger import Logger
from tools.helpers import (
    get_table_name,
    make_hash
)
from tools.config import (
    UNIQUE_KEY,
    SYSTEM_LOGIN,
    SYSTEM_IP
)
from db.connection import Connection

logger = Logger()

TEMPLATE_BLOCK = BlockModel(**{
    "timestamp": datetime.now(),
    "login": SYSTEM_LOGIN,
    "ip": SYSTEM_IP,
    "status": "primary"
})

TEMPLATE_SUPERBLOCK = CloseBlockModel(**{
    "login": SYSTEM_LOGIN,
    "ip": SYSTEM_IP,
    "open_date": datetime.now(),
    "close_date": datetime.now(),
    "activity": {
        datetime.now(): "primary"
    }
})

def use_template_block(template, status):
    if template:
        block = TEMPLATE_BLOCK
        block.timestamp = datetime.now()
        block.status = status
        return block

    block = TEMPLATE_SUPERBLOCK
    block.close_date = datetime.now()
    return block

def plugging(func):
    def wrapper(*args, **kwargs):
        cls = args[0]

        cls._del_last_block()
        block, id = func(*args, **kwargs)
        cls._create_last_block(block)

        return block, id
    return wrapper


class BlockManager:
    def __init__(self):
        self.db = Connection()
        self._last_block_id = None

    def init_primary_blocks(self):
        logger.log("INIT PRIMARY BLOCK")

        for i in range(2,0,-1):
            print(i)
            primary_block = use_template_block(i, "primary")
            primary_block.hash = make_hash(i, 1)
            self.db.add(
                get_table_name(i),
                primary_block.dict()
            )

    @plugging
    def create_block(self, data, table_id):
        logger.log(f"CREATE BLOCK - {table_id}")

        if table_id:
            block = BlockModel(*data)
        else:
            block = CloseBlockModel(**data)

        tablename = get_table_name(table_id)
        BaseBlock.update(
            block,
            self.db.get_last_block(
                tablename
            )
        )
        id = self.db.add(
            tablename, block.dict()
        )

        return block, str(id)

    def _create_last_block(self, block):
        last_block = use_template_block("plug")

        BaseBlock.update(last_block, block)
        self.last_block_id = self.db.add(
            last_block.dict()
        )

    def _del_last_block(self):
        try:
            self.db.delete(self._last_block_id)
        except AttributeError:
            return False

        return True
