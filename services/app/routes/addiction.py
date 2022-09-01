import os
import logging

from datetime import datetime

from blockchain.blocks import BlockModel
from blockchain.main import CoreManager
from tools.debug_logger import Logger

manager = CoreManager()
logger = Logger()

def reset_connection(key):
    return manager.reset(key)


def history_table_from():
    dicts = manager.get_table()
    for obj in dicts:
        logger.log(obj)
    return 200


def update_app(request):
    try:
        data = request.get_json()
    except:
        logger.log_exception("Request Data Error!")
        return 456

    if data is None:
        return 456

    data["timestamp"] = datetime.now()
    token = data.pop("token", None)

    return check_allocation(token, data)

    #if validate(data):
    #    return check_allocation(status, token, data)
    #
    #return False


def validate(data: dict) -> bool:
    try:
        block = BlockModel(**dict)
    except:
        return False

    return True


def check_allocation(token, data: dict) -> bool:
    if token:
        return manager.check_token(
            token, data.get("action", "check_token")
        )

    status = data.get("status")
    return manager.define_action(token, status, data)
