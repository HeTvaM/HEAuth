import os
import logging

from datetime import datetime

from blockchain.blocks import BlockModel
from blockchain.block_manager import BlockManager
from tests.debug_loggger import Logger

manager = BlockManager()
logger = Logger()

def tokens():
    print(manager.hash_table)
    
    return True

    
def history_table_from(db):
    logger.log("HISTORY \ DB: {db}")
    
    return manager.get_table(db)


def update_app(request):
    logger.log("UPDATE")
    
    data = request.get_json()
    data["timestamp"] = datetime.now()
    
    token = data.pop("token", None)
    
    return check_allocation(token, data)

    #if validate(data):
    #    return check_allocation(status, token, data)
    #
    #return False


def validate(data: dict) -> bool:
    try:
        block = BlockModel(*dict)
    except: 
        return False
    
    return True


def check_allocation(token, data: dict) -> bool:
    logger.log(f"ALLOCATION \ \nDATA: {data}")
    
    if token:
        return manager.is_token(token)

    return manager.new_request(token, data)
