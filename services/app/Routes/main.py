import os

from datetime import datetime

from Manager.blocks import BlockModel
from Manager.block_manager import BlockManager

manager = BlockManager()


ARGS_FOR_BLOCK = ["@timestamp", "login", "ip", "token"]  

def create_dict_from(data: str) -> dict:
    # values = []
    # for arg in ARGS_FOR_BLOCK:
    #    try:
    #        values.append(request.arg(arg))
    #    except:
    #        pass
    # return values
    
    dictionary = {"@timestamp": datetime.now()}
    temp = data[1:-1].replace(":", ", ").split(", ")

    for key, value in zip(temp[::2], temp[1::2]):
        dictionary[key] = value

    return dictionary

def validate(data: dict) -> bool:
    try:
        block = BlockModel(*dict)
    except: 
        return False
    
    return True

def check_allocation(status, token, data: dict) -> bool:
    if token:
        return manager.is_token(token)

    return manager.new_request(data, status, token)

def update_app(request):
    status = request.arg("status", "open")
    token = request.arg("token", None)
    
    data = create_dict_from(
        request.get_data(as_text=True)
    )
    
    return check_allocation(status, token, data)

    #if validate(data):
    #    return check_allocation(status, token, data)
    #else:
    #    return False
    
def render_table_from(request):
    db = request.arg("DB", 0)
    
    return manager.get_table(db)