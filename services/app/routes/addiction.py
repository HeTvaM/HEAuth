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

    return check_allocation(data)

def validate(data: dict) -> bool:
    try:
        block = BlockModel(**data)
    except:
        return False

    return True

def check_allocation(data):
    token = data.pop("token", None)
    action = data.pop("action", None)

    logger.log(f"TOKEN - {token}\nAction - {action}")

    if action:
        return manager.add_user_action(
            token, action
        )

    data["timestamp"] = datetime.now()
    if validate(data):
        try:
            status = data["status"]
        except AttributeError:
            return 410

        return manager.define_action(token, status, data)

    return 555
