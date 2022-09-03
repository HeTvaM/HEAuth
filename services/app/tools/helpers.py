import os
import hashlib

from random import sample, randint

from blockchain.blocks import *
from .config import *

def make_hash(block, id:int):
    try:
        key = f"{str(block.dict())}{id}"
    except:
        key = UNIQUE_KEY

    return hashkey(key)

def check_block_data(open_data, close_data):
    open_block = TEMPLATE_BLOCK
    open_block.login = open_data[1].replace(" ", "")
    open_block.ip = open_data[3].replace(" ", "")

    close_block = BlockModel(**close_data)

    return open_block == close_block

def get_table_name(table):
    return OPEN_TABLE if table else CLOSE_TABLE

def hashkey(key=""):
    key += f"{sample(UNIQUE_KEY, randint(0, len(UNIQUE_KEY)))}"

    hash_algo = hashlib.sha256()
    hash_algo.update(
        key.encode()
    )

    return hash_algo.hexdigest()
