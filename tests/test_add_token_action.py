import pytest
import request


from .test_token_create import URL, create_token

def add_action():
    token = create_token()
    data = {
        "token": token,
        "action": "TEST ACTION"
    }
    
    return request.post(URL, data=data)

def check_add_action():
    assert "Action Added" == add_action()
