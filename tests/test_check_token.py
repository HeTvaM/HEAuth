import pytest
import request

from .test_token_create import URL, create_token

def is_token():
    token = create_token()
    data = {
        "token": token,
        "status": "check"
    }

    return request.post(URL, data=data)

def check_token():
    assert "Access allowed" == is_token()
