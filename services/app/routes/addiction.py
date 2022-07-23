import os
import logging

from datetime import datetime

from blockchain.blocks import BlockModel
from blockchain.main import CoreManager
from tests.debug_loggger import Logger

manager = CoreManager()
logger = Logger()

def history_table_from(db):
    dicts = manager.get_table(db)
    return True


def update_app(request):
    data = request.get_json(force=True)
    if data is None:
        return 3

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
